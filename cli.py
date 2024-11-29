import os
import argparse
import openai

# Default configuration
defaults = {
    "api_key": os.getenv('OPENAI_API_KEY'),
    "size": "1024x1024",
    "number": 1,
}

# Parse arguments
parser = argparse.ArgumentParser(description="Generate images using OpenAI's DALL-E.")
parser.add_argument('-k', '--api-key', type=str, default=defaults["api_key"], help='OpenAI API key.')
parser.add_argument('-p', '--prompt', type=str, required=True, help='Prompt for image generation.')
parser.add_argument('-s', '--size', type=str, default=defaults["size"], help='Image size (e.g., 1024x1024).')
parser.add_argument('-n', '--number', type=int, default=defaults["number"], help='Number of images to generate.')
args = parser.parse_args()

# Validate API key
if not args.api_key:
    raise ValueError("API key is required. Set OPENAI_API_KEY environment variable or use --api-key.")

# Set the API key for OpenAI
openai.api_key = args.api_key

# Generate images
try:
    response = openai.Image.create(
        prompt=args.prompt,
        n=args.number,
        size=args.size,
    )
    print("Generated Images:")
    for idx, image in enumerate(response['data']):
        print(f"{idx + 1}: {image['url']}")
except openai.error.OpenAIError as e:
    print(f"Error while generating images: {e}")
