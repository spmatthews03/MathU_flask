import urllib.parse
from flask import render_template, jsonify, request, Flask
import requests
import wolframalpha
import json

WOLFRAM_URL = "http://api.wolframalpha.com/v2/query?"


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
    steps = list()
    for pod in json_obj['queryresult']['pods']:
        if pod['title'] == 'Results':
            for subpod in pod['subpods']:
                if 'Possible' in subpod['title']:
                    steps = subpod['plaintext'].splitlines()
    return steps


def ask_wra_solve(question):
    params = {
        'appid': get_wolfram_key(),
        'input': question,
        'output': 'json',
        'includepodid': 'Result'
    }

    response = requests.get(WOLFRAM_URL + urllib.parse.urlencode(params))
    json_obj = json.loads(response.text)
    answer = list()
    for pod in json_obj['queryresult']['pods']:
        for subpod in pod['subpods']:
            if subpod['title'] == "":
                answer = subpod['img']['src']
    return answer


def get_solve_image(question):
    params = {
        'appid': get_wolfram_key(),
        'input': question,
        'format': 'plaintext'
    }
    response = requests.get(WOLFRAM_URL + urllib.parse.urlencode(params))
    trimmed_subpod = response.text[response.text.index('Possible'):]
    trimmed_plaintext = trimmed_subpod[trimmed_subpod.index('<plaintext>'):]
    trimmed_plaintext = trimmed_plaintext.split('<plaintext>')
    new_plaintext = list(filter(None, trimmed_plaintext))
    result = (new_plaintext[0].split('</'))[0].splitlines()

