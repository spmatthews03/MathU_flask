import random
import re
import nltk
import json
import string
import argparse
from nltk.chat.util import Chat, reflections
import AlgebraProblem
from algebra_helper import *


reflections = {
    "am": "are",
    "was": "were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "are": "am",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

conversationals = [
    [r'(.*)(homework)|(problem)(.*)',
        [
            "Yeah. What the problem you're working with",
        ]
    ],
    [r'(.*)(can you help)|(will you help)|(please help)(.*)',

        [
         "I can sure try! Lets take a look...",
         "Lets see, I think we can figure this out...",
        ]
    ],
    [r'(.*)(solve)(.*)',
        [
            "{0}",
        ]
    ],
    [r'(.*)(simplify)(.*)',
        [
            "{0}",
        ]
     ],
    [r'(.*)(help)(.*)',
         [
             "{0}",
         ]
    ],
    [r'(.*)(The problem is)(.*)',
         [
             "{0}",
         ]
    ],
    [r'(.*)(project)|( groups )|(group)(.*)',
        [
            "{0}",
        ]
    ],
    [r'(.*)(test)|(exam)|(proctortrack)(.*)',
        [
            "{0}",
        ]
    ],
]

operations = ['+','*','/','(',')','-']


class ChatBot:
    def __init__(self):
        self.name = "MathU"
        self.introduced = False
        self.current_prob = AlgebraProblem.AlgebraProblem()
        self.user_name = ''
        self.math_steps = list()


    def respond(self, statement, problem=''):
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
        if self.current_prob.get_expression() is '':
            self.current_prob.set_expression(self.extract_problem(statement))

        for pattern, responses in conversationals:
            match = re.search(pattern.lower(), statement.lower().rstrip(".!"))
            if match:
                response = random.choice(responses)

                for group in match.groups():
                    if group == 'solve':
                        self.current_prob.set_type('solve')
                    if group == 'simplify':
                        self.current_prob.set_type('simplify')



                if self.current_prob.get_type() is not None:
                    if len(self.current_prob.get_vars()) < 2:
                        if self.current_prob.get_type() is 'solve':
                            math_steps = solve_for_var_algebra(self.current_prob)
                        else:
                            math_steps = simplify_expression(self.current_prob)
                    if self.current_prob.get_type() is 'simplify':
                        return simplify_expression(self.current_prob)



    def extract_problem(self, sentence):
        problem = ''
        for item in sentence:
            if item.isdigit()  or item in operations:
                return sentence[sentence.index(item):].replace(" ", "")





    def introduction(self):
        self.introduced = True
        return "Hi there! My name is MathU. I'm your personal math tutor for your basic algebra problems. How can I help you?"

