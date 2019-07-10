from algebra_helper import *
import re

import urllib.parse

class AlgebraProblem:
    def __init__(self, expression=None, type_of_problem=None):
        self.expression = self.clean_expression(expression) if expression is not None else None
        self.type = type_of_problem
        self.all_info = self.have_all_info()
        self.updated_expression = ''
        self.steps = list()
        self.vars = self.get_vars() if expression is not None else None
        self.var_to_solve = self.var_to_solve_method()

    def have_all_info(self):
        if self.type is not None and self.expression is not None and self.var_to_solve is not None:
            return True
        else:
            return False

    def var_to_solve_method(self):
        if self.type is 'solve':
            if len(self.vars) == 1:
                return self.vars.pop()
            else:
                return None
        else:
            return None

    def get_var_to_solve(self):
        return self.var_to_solve

    def set_var_to_solve(self, var):
        self.var_to_solve = var

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
        self.vars = self.get_vars() if expression is not None else None

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

    def clean_expression(self, expression):
        exp = expression.replace(" ", "")
        return exp




