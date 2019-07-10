import random
import re
import nltk
import json
import string
import sys
import argparse
from nltk.chat.util import Chat, reflections
import AlgebraProblem
from algebra_helper import *
from Chatbot.responses import *
import discord
import discord.ext.commands
from discord.ext.commands.errors import *





operations = ['+','*','/','(',')','-']


class ChatBot():
    def __init__(self):
        self.name = "MathU"
        self.introduced = False
        self.current_prob = AlgebraProblem.AlgebraProblem()
        self.user_name = ''
        self.math_steps = list()

    def respond(self, statement):
        if not self.introduced:
            return self.introduction()
        else:
            response = self.analyze_question(statement)
            return response

    def reflect(self,fragment):
        tokens = fragment.lower().split()
        for i, token in enumerate(tokens):
            if token in reflections:
                tokens[i] = reflections[token]
        return ' '.join(tokens)

    def analyze_question(self, statement):
        if self.current_prob.get_expression() is None:
            self.current_prob.set_expression(self.extract_problem(statement))

        if statement in self.current_prob.get_vars() and self.current_prob.get_type() is not 'solve':
            self.current_prob.set_var_to_solve(statement)

        if not self.current_prob.have_all_info():
            if statement in self.current_prob.get_vars():
                self.current_prob.set_var_to_solve(statement)
                pass
            for pattern, responses in conversationals:
                match = re.search(pattern.lower(), statement.lower().rstrip(".!"))
                if match:
                    for group in match.groups():
                        if group in ['solv','equat']:
                            self.current_prob.set_type('solve')
                        if group in ['simpl','express']:
                            self.current_prob.set_type('simplify')
            return get_problem_info_response(self.current_prob)

        else:
            if len(self.current_prob.get_vars()) < 2:
                if self.current_prob.get_type() is 'solve':
                    math_steps = solve_for_var_algebra(self.current_prob)
                else:
                    math_steps = simplify_expression(self.current_prob)
            if self.current_prob.get_type() is 'simplify':
                return simplify_expression(self.current_prob)

    @staticmethod
    def extract_problem(sentence):
        problem = ''
        for item in sentence:
            if item.isdigit()  or item in operations:
                return sentence[sentence.index(item):].replace(" ", "")

    def introduction(self):
        self.introduced = True
        return "Hi there! My name is MathU. I'm your personal math tutor for your basic algebra problems. How can I help you?"
