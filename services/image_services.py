import os
import requests
from dotenv import load_dotenv

load_dotenv()
KEY = os.getenv('KEY')

def generate_image_service(prompt, model, filename):

    url = f"https://gen.pollinations.ai/image/{prompt}?model={model}"
    headers = {
        "Authorization": f"Bearer {KEY}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        with open(filename, "wb") as f:
            f.write(response.content)

            return filename

    except Exception as e:
        print("Error:", e)
        return None