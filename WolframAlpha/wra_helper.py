import urllib.parse
from flask import render_template, jsonify, request, Flask
import requests
import wolframalpha
import json
from collections import OrderedDict


WOLFRAM_URL = "https://api.wolframalpha.com/v2/query?"


def get_wolfram_key():
    return 'LAL7RE-VYLLR9VQHR'

def ask_wra_step_by_step(question):
    params = {
        'appid': get_wolfram_key(),
        'input': question,
        'podstate': 'Step-by-step solution',
        'format': 'plaintext',
        'output': 'json'
    }

    response = requests.get(WOLFRAM_URL + urllib.parse.urlencode(params))
    json_obj = json.loads(response.text)
    steps = {}
    for pod in json_obj['queryresult']['pods']:
        if pod['title'] == 'Results':
            for subpod in pod['subpods']:
                if 'Possible' in subpod['title']:
                    steps = subpod['plaintext'].splitlines()
    return steps


def ask_wra_solve(question):
    response = {
        'answer': [],
        'steps': {}
    }
    steps = list()


    if 'graph' in question.lower().split():
        params = {
            'appid': get_wolfram_key(),
            'input': question,
            'output': 'json',
        }

        response = requests.get(WOLFRAM_URL + urllib.parse.urlencode(params))
        json_obj = json.loads(response.text)
        answer = list()
        for pod in json_obj['queryresult']['pods']:
            if "Implicit" in pod['title']:
                for subpod in pod['subpods']:
                    answer = subpod['img']['src']
        return answer
    else:
        solve_params = {
            'appid': get_wolfram_key(),
            'input': question,
            'output': 'json',
            'includepodid': 'Result'
        }
        steps_params = {
            'appid': get_wolfram_key(),
            'input': question,
            'podstate': 'Step-by-step solution',
            'format': 'plaintext',
            'output': 'json'
        }

        solve_response = requests.get(WOLFRAM_URL + urllib.parse.urlencode(solve_params))
        steps_response = requests.get(WOLFRAM_URL + urllib.parse.urlencode(steps_params))

        json_obj_solve = json.loads(solve_response.text)
        json_obj_steps = json.loads(steps_response.text)

        for pod in json_obj_solve['queryresult']['pods']:
            for subpod in pod['subpods']:
                if subpod['title'] == "":
                    response['answer'] = subpod['img']['src']

        for pod in json_obj_steps['queryresult']['pods']:
            if pod['title'] == 'Results':
                for subpod in pod['subpods']:
                    if 'Possible' in subpod['title']:
                        response['steps'] = subpod['plaintext'].splitlines()

        return response


def parse_steps(steps):
    new_steps = {}
    explanation = []
    actual_step_string = ''
    for step in steps:
        if step[0].isupper():
            new_steps[actual_step_string] = explanation
            explanation.clear()
            actual_step_string = step
        else:
            explanation.append(step)

    return new_steps
