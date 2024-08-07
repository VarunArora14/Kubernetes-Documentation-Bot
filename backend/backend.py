import time
from flask import Flask, request, jsonify
from decomposition_model import getUserQuery
from global_vars import llm, embedding_function, retriever, init
from hyde_model import answerUserQuery

print("loading llm and vector db")
llm, embedding_function, retriever = init()
print("init called")
print(llm)

app = Flask(__name__)

@app.route("/decomposition/generate/", methods=["POST"])
def generate_text_decompose():
    start = time.time()
    data =request.json
    question = data.get("question")
    response = getUserQuery(question=question, llm=llm, retriever=retriever)
    end = time.time()
    net = round(end-start,2)
    res = {
        "time_taken": net, 
        "response":response
    }
    return jsonify(res)

@app.route("/hyde/generate/", methods=["POST"])
def generate_text_hyde():
    start = time.time()
    data =request.json
    question = data.get("question")
    answer, sources = answerUserQuery(query=question, llm=llm, retriever=retriever)
    end = time.time()
    net = round(end-start,2)
    res = {
        "time_taken": net, 
        "response":answer,
        "sources": sources
    }
    return jsonify(res)

if __name__ == '__main__':
    print("hello")
    app.run(host='0.0.0.0', port=5000, debug=True)
