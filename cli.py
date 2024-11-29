import openai
import os
import argparse

# Ensure that your API key is correctly set in your environment
openai.api_key = os.getenv('OPENAI_API_KEY')  # Ensure you have a valid API key set

def generate_image(prompt, num_images=1, size="1024x1024"):
    try:
        # Create image using the new OpenAI API method
        response = openai.Image.create(
            prompt=prompt,
            n=num_images,
            size=size
        )
        
        print("Generated Image URL(s):")
        for idx, image in enumerate(response['data']):
            print(f"{idx + 1}: {image['url']}")

    except openai.error.OpenAIError as e:
        print(f"Error while generating images: {e}")

def main():
    parser = argparse.ArgumentParser(description="Generate images using OpenAI API")
    parser.add_argument('-p', '--prompt', type=str, required=True, help="Prompt for image generation")
    parser.add_argument('-n', '--number', type=int, default=1, help="Number of images to generate")
    parser.add_argument('-s', '--size', type=str, default="1024x1024", help="Size of the image (e.g., 1024x1024)")

    args = parser.parse_args()

    # Call the image generation function
    generate_image(prompt=args.prompt, num_images=args.number, size=args.size)

if __name__ == "__main__":
    main()
