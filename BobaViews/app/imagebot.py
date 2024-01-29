import os
import requests
from dotenv import load_dotenv
import openai

load_dotenv()
OPENAI_API_KEY_BOBA = os.getenv('OPENAI_API_KEY_BOBA')

openai.api_key = OPENAI_API_KEY_BOBA

def ai_response():
    response = openai.Image.create(
        prompt="Generate a bubble tea mascot logo for a website, make it cute!",
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url

    # Download the image
    image_data = requests.get(image_url).content

    # Save the image to a local file
    with open('generated_image.jpg', 'wb') as f:
        f.write(image_data)

    return 'generated_image.jpg'

generated_image_path = ai_response()
print(f"Generated image saved to: {generated_image_path}")
