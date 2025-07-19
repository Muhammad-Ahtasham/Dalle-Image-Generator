from dotenv import load_dotenv
import os
import base64
from openai import OpenAI
import requests
import uuid

# Load environment variables
load_dotenv()

# Get the API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if OPENAI_API_KEY is None:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables.")

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Generate the image
def generate_image(imagePrompt):
    print("generate image called with prompt", imagePrompt)
    response = client.images.generate(
        model="dall-e-3",  # correct model name for image generation
        prompt=imagePrompt,
        size="1024x1024",
        quality="standard",
        n=1,  # Only one image allowed
    )

    image_urls = []
    saved_files = []
    if response.data and len(response.data) > 0:
        data = response.data[0]
        image_url = data.url
        image_urls.append(image_url)
        if image_url is not None:
            img_data = requests.get(image_url).content
            filename = f"Generated Images/{uuid.uuid4().hex}.png"
            with open(filename, "wb") as f:
                f.write(img_data)
            saved_files.append(filename)
    else:
        raise ValueError("No image data returned in response.")

    return saved_files

# generate_image("animated batman")