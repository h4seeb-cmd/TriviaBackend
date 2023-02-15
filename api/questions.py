from flask import Flask, Blueprint, jsonify, request

app = Flask(__name__)

questions_api = Blueprint('question_api', __name__,
                   url_prefix='/api/questions')


@app.route('/api/questions', methods = ['GET'])
def qRetrieve():
    if(request.method == 'GET'):
        questions = "what is 1 + 1?"
        return jsonify({'questions': questions})
    
if __name__ == "__main__": 
    # server = "http://127.0.0.1:5000" # run local
    server = 'https://flask.nighthawkcodingsociety.com' # run from web
    url = server + "/api/questions"
    questions = []  # responses list