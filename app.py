from flask import render_template, jsonify, request, Flask, send_file
from AlgebraProblem import AlgebraProblem
import algebra_helper
from Chatbot.Chatbot import ChatBot
from threading import Thread
from WolframAlpha import wra_helper

app = Flask(__name__)
chatbot = ChatBot()
problem = ''
questions = list()


@app.route('/')
def MathU():
    return render_template('mathu_screen.html')


@app.route('/chatbot_question/', methods=['GET','POST'])
def get_chatbot_question():
    question = request.args.get('msg')
    step = request.args.get('step')
    if step == '1':
        return 'True'
    else:
        return 'False'


@app.route('/solve', methods=['GET','POST'])
def solve_algebraic_expression():
    question = request.args.get('msg')
    global problem
    problem = question
    return jsonify(wra_helper.ask_wra_solve(question))


@app.route('/ask_mathu', methods=['GET','POST'])
def ask_mathu():
    question = request.args.get('msg')
    global problem
    problem = question
    if problem != '':
        tmp = jsonify(wra_helper.ask_wra_step_by_step(question))
        return tmp
    else:
        tmp = jsonify(wra_helper.ask_wra_step_by_step(question))
        return tmp


@app.route('/begin_talking_to_mathu')
def chat_with_mathu():
    return chatbot.simple_talking()


@app.route('/past_problems')
def past_problems():
    return problem


def run():
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    t = Thread(target=run)
    t.start()

