import requests

from config import conf

def get_open_ai_key():
    url = conf().get("open_ai_api_key_get_url")
    if url:
        response = requests.get(url)
        result = response.text.strip()
        return result
    else:
        return conf().get("open_ai_api_key")
