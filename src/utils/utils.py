import requests


def generate_schema(url):
    return requests.get(url=url).json()[0]
