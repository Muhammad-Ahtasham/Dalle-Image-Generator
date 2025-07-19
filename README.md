# Dalle-Image-Generator

A web application that allows users to generate images using OpenAI's DALL·E model by entering a text prompt. Generated images are saved, can be viewed in a gallery, and are available for download.

## Features

- Generate AI images from text prompts using OpenAI's DALL·E (via the OpenAI API)
- View all generated images in a gallery
- Download any generated image
- Simple, modern web interface built with Flask and HTML/CSS/JS

## Demo

- Home: Enter a prompt and generate images
- Gallery: Browse all previously generated images
- About: Learn more about the app and the author

## Technologies Used

- Python 3
- Flask (web framework)
- OpenAI API (DALL·E)
- HTML, CSS, JavaScript (frontend)

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Muhammad-Ahtasham/Dalle-Image-Generator.git
   cd Dalle\ App
   ```

2. **Install dependencies:**
   Create a `requirements.txt` file with the following content:
   ```
   flask
   python-dotenv
   openai
   requests
   ```
   Then install with:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your OpenAI API key:**
   - Create a `.env` file in the project root:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```
   - (The `.env` file is already in `.gitignore`.)

4. **Run the app:**
   ```bash
   python main.py
   ```
   The app will be available at `http://127.0.0.1:5000/`.

## Usage

- On the home page, enter a prompt describing the image you want to generate and click "Generate Image".
- Wait for the image to be generated and displayed.
- Visit the Gallery to see all generated images.
- Click the download icon on any image to save it.

## Project Structure

```
.
├── main.py                # Flask app entry point
├── generate_image.py      # Image generation logic using OpenAI API
├── templates/             # HTML templates (index, gallery, about)
├── Generated Images/      # Folder where generated images are saved
├── .env                   # Your OpenAI API key (not committed)
├── .gitignore             # Ignores .env
└── README.md              # Project documentation
```

## About

Created by Muhammad Ahtasham — an Artificial Intelligence specialist and Software Engineer.  
Learn more: [atiiisham.vercel.app](https://atiiisham.vercel.app)