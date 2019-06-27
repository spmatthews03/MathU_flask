import random
import re
import nltk
import json
import string
import argparse
from nltk.chat.util import Chat, reflections


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
    [r'(.*)(difficult)|(hard)|(easy)|(challenging)|(rigorous)(.*)',

        [
         "According to my data, it is an average difficulty of {0} out of 5.",
         "The average response is {0} out of 5.",
         "Depends, do you think {0}/5 is manageable?"
        ]
    ],
    [r'(.*)(how fun)|( fun )|(rating)|( like )|(.*)',
         [
             "{0}",
         ]
    ],
    [r'(.*)(time)|(spend)|(how long)|(long)|(workload)|(how much)|(work)(.*)',
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



class ChatBot:
    def __init__(self, reviews):
        self.name = "MathU"


    def respond(self, statement):
        response = self.analyze_question(statement)
        if response is None:
            return "I'm sorry I couldn't find any information. Did you enter the Course ID?"
        else:
            return response

    def reflect(self,fragment):
        tokens = fragment.lower().split()
        for i, token in enumerate(tokens):
            if token in reflections:
                tokens[i] = reflections[token]
        return ' '.join(tokens)

    def analyze_question(self, statement):
        self.extract_class(statement)
        if self.classID is not None:
            for pattern, responses in conversationals:
                match = re.search(pattern.lower(), statement.lower().rstrip(".!"))
                if match:
                    response = random.choice(responses)
                    return response.format(self.get_class_info(self.classID, match.group(0)))


    def extract_class(self, statement):
        tokens = statement.lower().split()
        for i, token in enumerate(tokens):
            token = token.translate(str.maketrans('', '', string.punctuation))
            if token[-4:].isdigit():
                self.classID = token[-4:]


    def get_class_info(self, class_id, indicator):
        if any(item in indicator for item in ['easy','hard','difficult','challenging','rigorous']):
            return get_difficulty(class_id, self.reviews)
        elif any(item in indicator for item in ['fun','rating','good']):
            return get_rating(class_id, self.reviews)
        elif any(item in indicator for item in ['time','how long','spend','long','workload','work']):
            return get_workload(class_id, self.reviews)
        elif any(item in indicator for item in ['test','exam','proctor']):
            return get_exam_info(class_id, self.reviews)
        elif any(item in indicator for item in ['projects','groups','group']):
            return get_project_info(class_id, self.reviews)
        else:
            return respond()