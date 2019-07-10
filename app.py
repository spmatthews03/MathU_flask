from flask import render_template, jsonify, request, Flask, send_file
from AlgebraProblem import AlgebraProblem
import algebra_helper
from Chatbot.Chatbot import ChatBot
from threading import Thread
from WolframAlpha import wra_helper

app = Flask(__name__)
chatbot = ChatBot()
problems = list()
questions = list()


@app.route('/')
def MathU():
    return render_template('mathu_screen.html')


@app.route('/solve')
def solve_algebraic_expression():
    expression = request.args.get('msg')
    problems.append(expression)
    return wra_helper.get_solve_image(expression)


@app.route('/ask_mathu')
def ask_mathu():
    question = request.args.get('msg')
    questions.append(question)
    if problems:
        return jsonify(wra_helper.ask_wra_solve(question))
    else:
        return jsonify(wra_helper.ask_wra_step_by_step(question))


@app.route('/begin_talking_to_mathu')
def chat_with_mathu():
    return chatbot.simple_talking()


@app.route('/past_problems')
def past_problems():
    return problems


def run():
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    t = Thread(target=run)
    t.start()

