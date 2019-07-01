from flask import render_template, jsonify, request, Flask
from AlgebraProblem import AlgebraProblem
import algebra_helper
from Chatbot.Chatbot import ChatBot

app = Flask(__name__)
chatbot = ChatBot()
problems = list()
questions = list()


@app.route('/')
def MathU():
    return render_template('mathu_screen.html')


@app.route('/algebra/solve')
def solve_algebraic_expression():
    expression = request.args.get('msg')

    # type_of_problem = request.form['type']
    problem = AlgebraProblem(expression, "solve")
    problems.append(expression)
    return algebra_helper.do_problem(problem)


@app.route('/ask_mathu')
def ask_mathu():
    question = request.args.get('msg')
    questions.append(question)
    if problems:
        return chatbot.respond(question, problems.pop())
    else:
        return chatbot.respond(question)


@app.route('/begin_talking_to_mathu')
def chat_with_mathu():
    return chatbot.simple_talking()


@app.route('/past_problems')
def past_problems():
    return problems


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
