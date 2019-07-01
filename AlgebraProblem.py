from algebra_helper import *
import re



class AlgebraProblem:
    def __init__(self, expression='', type_of_problem=None):
        self.expression = clean_expression(expression)
        self.type = type_of_problem
        self.updated_expression = ''
        self.steps = list()
        self.vars = self.get_vars()

    def set_type(self, tp):
        self.type = tp

    def add_step(self, step):
        self.steps.append(step)

    def get_steps(self):
        return self.steps

    def get_expression(self):
        return self.expression

    def get_type(self):
        return self.type

    def set_expression(self, expression):
        self.expression = expression
        self.vars = self.get_vars()

    def set_updated_expression(self, expression):
        self.updated_expression = expression

    def get_variables(self):
        return self.vars

    def get_vars(self):
        variables = set()
        for char in self.expression:
            if char.isalpha():
                variables.add(char)
        return variables





