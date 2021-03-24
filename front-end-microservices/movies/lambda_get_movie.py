__author__ = 'mrivas'

from main.lambda_get_movie_handler import lambda_get_movie_handler

def handler(event, context):
    hdl = lambda_get_movie_handler()
    return hdl.handle(event, context)