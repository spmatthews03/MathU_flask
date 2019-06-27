import re

operations = ['+','*','/']

def do_problem(problem):
    if problem.get_type() is 'simplify':
        return simplify_expression(problem)
    elif problem.get_type() is 'solve':
        return solve_for_var_algebra(problem)
    return "No solution Here!"


def next_step():
    return True



def simplify_expression():
    return True

def understand_review_of_step(problem, review):
    problem.add_step(review)


def switch_sides(term, terms):
    terms.remove(term)
    terms.insert(0,term)
    return terms


def get_variables_on_same_side(problem):
    terms = get_terms(problem.get_expression())

    for variable in problem.get_variables():
        left_count = 0
        right_count = 0
        left_side = True
        for term in terms:
            if term is '=':
                left_side = False
                pass
            elif left_side:
                if variable in term:
                    left_count += 1
            else:
                if variable in term:
                    right_count += 1
        if left_count != 0 and right_count != 0:
            pass
    return True


def solve_for_var_algebra(problem):
    # solve implies an equal sign
    expression = clean_expression(problem.expression)
    terms = get_terms(expression)

    simplified_terms, review_of_step = combine_like_terms(terms)
    # understand_review_of_step(problem, review_of_step)
    upd_exp = print_new_equation(simplified_terms)
    problem.set_updated_expression(upd_exp)

    return print_new_equation(simplified_terms)


def isolate_variable(problem):
    terms = get_terms(problem.get_expression())


def combine_like_terms(terms):
    counter = {}
    what_was_combined = set()
    for term in terms:
        if term not in operations:
            try:
                counter[get_variable_of_term(term)] += get_value_of_term(term)
                what_was_combined.add(get_variable_of_term(term))
            except KeyError:
                counter[get_variable_of_term(term)] = get_value_of_term(term)
    return counter, what_was_combined


def print_new_equation(counter):
    expression = ''
    for item in counter:
        expression = expression + (str('+' + str(counter[item])) if counter[item] > 0 else str(counter[item])) + item
    if expression[0] is '+':
        expression = expression[1:]
    return expression

def get_variable_of_term(term):
    value = ''
    for item in term:
        if item.isalpha():
            value = value + item
    return value

def get_value_of_term(term):
    value = ''
    for item in term:
        if item.isdigit():
            value = value + item
        if item is '-':
            value = value + item
    if value is '-':
        value = -1
    if value is '':
        value = 1
    return float(value)


def get_terms(expression):
    terms = list(re.split("([-+/*])", expression))
    signed_terms = list()
    isNegative = False
    for term in terms:
        if term is '-':
            isNegative = True
        else:
            if isNegative:
                negative_term = '-' + term
                signed_terms.append(negative_term)
                isNegative = False
            else:
                signed_terms.append(term)
    return signed_terms


def check_power():
    return True


def evaluate_expression(expression):
    expression = clean_expression(expression)
    expression_ass_list = list(expression)
    new_expression = ''
    number_stack = list()

    for item in expression_ass_list:
        if item.isdigit():
            new_expression = new_expression + item
        else:
            if len(new_expression) > 0:
                number_stack.append(new_expression)
                new_expression = ''
            if item != ')':
                number_stack.append(item)
            else:
                t = list()
                while len(number_stack) is not 0:
                    top = number_stack.pop()
                    if top is "(":
                        break
                    else:
                        t.append(0, top)
                temp = 0
                if len(t) is 1:
                    temp = t.index(0)





    return True

def clean_expression(expression):
    expression = expression.replace(" ","")
    return expression

