from operator import itemgetter
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain_chroma import Chroma
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain import hub
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel


def getWebResponseLLM(query, llm):
    '''
    this method takes in user question and gives LLM generated output
    based on it's data trained from web
    '''
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful assistant who gives concise summary on inputs provided by human. Your response should be comprehensive and include all key points that would be found in the top search result and total length less than 250 words.",
            ),
            ("human", "{query}"),
        ]
    )

    chain = prompt | llm
    response =  chain.invoke(
        {
            "query": query
        }
    )
    return response.content


def format_docs(docs):
    # print("docs:", docs)
    return "\n\n".join(doc.page_content for doc in docs)


def answerUserQuery(query, llm, retriever):
    print(query)
    # use hyde chromaDB as retriever

    # Get LLM response for question and find similar docs for the LLM response
    hypo_web_search_text = getWebResponseLLM(query=query, llm=llm)
    matched_docs = retriever.get_relevant_documents(query=hypo_web_search_text)

    prompt = ChatPromptTemplate.from_template("""You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use five sentences maximum and keep the answer concise.
        Question: {question} 
        Context: {context} 
        Answer:""")

    rag_chain_from_docs = (
        RunnablePassthrough.assign(context=(lambda x: format_docs(x["context"]))) # x is dict passed and calls method format_docs on matched_docs
        | prompt
        | llm
        | StrOutputParser()
    )


    # here we pass the input values parallely to both
    # here we create dictionary with keys => context and question and assign them 
    # values as passed via invoke method on RunnableParallel
    # we also assign this dictionary object 'answer' once it gets computed from
    # chain 'rag_chain_from_docs'
    rag_chain_with_source = RunnableParallel(
    {"context": itemgetter("context"), "question": itemgetter("question")}
    ).assign(answer=rag_chain_from_docs)


    conversation = rag_chain_with_source.invoke({
        "question": query,
        "context": matched_docs # pass matched docs instead of retriever
    })
    
    sources = list(set([doc.metadata['source'] for doc in conversation['context']]))
    answer = conversation['answer']
    return answer, sources

