from flask import render_template, jsonify, request, Flask
from AlgebraProblem import AlgebraProblem
import algebra_helper
from Chatbot.Chatbot import ChatBot

app = Flask(__name__)
# chatbot = ChatBot()

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/algebra/solve')
def input_form():
    return render_template('expression_input.html')





@app.route('/algebra/solve', methods=['POST'])
def solve_algebraic_expression():
    expression = request.form['text']
    # type_of_problem = request.form['type']
    problem = AlgebraProblem(expression, "solve")


    return render_template('expression_input.html', result = algebra_helper.do_problem(problem))


# @app.route('/algebra/simplify')
# def solve_algebraic_expression():
#     return "Simplify Algebra"
#
#
# @app.route('/algebra/evaluate')
# def solve_algebraic_expression():
#     return "Evaluate Algebra"
#
#
# @app.route('/math/solve')
# def solve_algebraic_expression():
#     return "Solve Math"



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
