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
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=imagePrompt,
        tools=[{"type": "image_generation"}]
    )
    print("OpenAI response:", response)

    image_data = [
        output.result
        for output in response.output
        if output.type == "image_generation_call"
    ]

    saved_files = []
    if image_data:
        image_base64 = image_data[0]
        if not isinstance(image_base64, str):
            raise TypeError("Expected base64 string, got something else.")
        filename = f"Generated Images/{uuid.uuid4().hex}.png"
        with open(filename, "wb") as f:
            f.write(base64.b64decode(image_base64))
        saved_files.append(filename)
    else:
        raise ValueError("No image data returned in response.")

    return saved_files

# generate_image("animated batman")