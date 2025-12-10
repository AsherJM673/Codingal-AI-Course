import requests
from config import API_KEY, MODEL_URL
from services.logger import getLogger

logger = getLogger()

def classify_text(text):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    paylod = {"inputs": text}

    try:
        logger.info("Sending requests to huggingFace API")
        response = requests.post(MODEL_URL, headers=headers, json= payload, timeout=20)

