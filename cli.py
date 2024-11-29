import openai
import os
import argparse

# Ensure that your API key is correctly set in your environment
openai.api_key = os.getenv('OPENAI_API_KEY')  # Make sure you have set your API key

def generate_image(prompt, num_images=1, size="1024x1024"):
    try:
        # Use the old OpenAI Image generation method (compatible with SDK v0.28.0)
        response = openai.Image.create(
            prompt=prompt,
            n=num_images,
            size=size
        )

        # Print the URLs of the generated images
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
