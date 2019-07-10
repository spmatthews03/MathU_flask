import random

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

more_information = False


def get_more_information():
    return more_information

def set_more_information(tmp):
    global more_information
    more_information = tmp

def get_problem_info_response(problem):
    if problem.get_type() is None:
        if get_more_information() is True:
            return random.choice(type_response)
        else:
            set_more_information(True)
            return random.choice(need_information) + random.choice(type_response)

    if problem.get_expression() is None:
        if get_more_information() is True:
            return random.choice(expression_responses)
        else:
            set_more_information(True)
            return random.choice(need_information) + random.choice(expression_responses)
    if problem.get_var_to_solve() is None:
        if get_more_information() is True:
            return random.choice(variable_response)
        else:
            set_more_information(True)
            return random.choice(need_information) + random.choice(variable_response)


need_information = [
    'I will need some more information...'
]

type_response = [
    'Are you solving or simplifying?',
    'Will it be an expression or an equation?'
]

variable_response = [
    'What variable are you solving for?'
]

expression_responses = [
    'Alright What is the problem?',
    'What problem are you working through?',
    'Cool, Cool. Lets get started. What is the problem?'
]



conversationals = [
    [r'(.*)(solv)|(equat)(.*)',
        [
            "{0}",
        ]
    ],
    [r'(.*)(simpl)|(express)(.*)',
        [
            "{0}",
        ]
    ],
    [r'(.*)(homework)|(problem)(.*)',
        [
            "Yeah. What is the problem you're working with",
        ]
    ],
    [r'(.*)(can you help)|(will you help)|(please help)(.*)',

        [
         "I can sure try! Lets take a look...",
         "Lets see, I think we can figure this out...",
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
]



def get_response():
    return True
