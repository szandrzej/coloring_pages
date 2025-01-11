import argparse
from datetime import datetime
from coloring_pages.generator import generate_image
from coloring_pages.processor import convert_to_coloring_page, create_a4_coloring_page
from coloring_pages.printer import print_file

def main():
    parser = argparse.ArgumentParser(description="Generate and print coloring pages.")
    parser.add_argument("--prompt", type=str, help="Text prompt for image generation.")
    parser.add_argument("--print", action="store_true", help="Send the output to the printer.")
    parser.add_argument("--api-key", type=str, required=True, help="OpenAI API key.")
    args = parser.parse_args()

    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    raw_file = f"images/raw/cp_{current_time}.png"
    output_file = f"images/final/cp_{current_time}.png"
    output_a4_file = f"images/final/a4/cp_{current_time}.png"
    if args.prompt:
        generate_image(args.prompt, raw_file, args.api_key)
        # convert_to_coloring_page(raw_file, output_file)
        create_a4_coloring_page(raw_file, output_a4_file)
    else:
        print("Please provide either a text prompt")
        return

    if args.print:
        print_file(output_a4_file)

if __name__ == "__main__":
    main()
