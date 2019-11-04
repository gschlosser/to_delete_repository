from flask import Blueprint, request
from custom_log import logger

calculator = Blueprint('calculator_api', __name__)

@calculator.route('/add', methods=['POST'])
@logger
def add_nunmbers():
    body = request.json
    num1 = body['num1']
    num2 = body['num2']

    return {
        'answer' : num1 + num2
        }

@calculator.route('/subtract', methods=['POST'])
def subtract_numbers():
    body = request.json
    num1 = body['num1']
    num2 = body['num2']
    return {
        'answer' : num1 - num2
        }

@calculator.route('/mult', methods=['POST'])
def mult_numbers():
    body = request.json
    num1 = body['num1']
    num2 = body['num2']
    return {
        'answer' : num1 * num2
        }

@calculator.route('/div', methods=['POST'])
def div_numbers():
    body = request.json
    num1 = body['num1']
    num2 = body['num2']
    return {
        'answer' : num1 / num2
        }