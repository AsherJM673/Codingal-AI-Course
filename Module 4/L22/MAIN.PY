import requests 
from config import API_KEY


def classifyText(text):
    API_URL = 'https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english'
    headers = {"Athorization"}