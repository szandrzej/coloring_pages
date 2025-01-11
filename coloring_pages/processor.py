from PIL import Image, ImageFilter, ImageOps

def convert_to_coloring_page(input_path, output_path):
    image = Image.open(input_path).convert("L")
    edges = image.filter(ImageFilter.FIND_EDGES)
    inverted = ImageOps.invert(edges)
    inverted.save(output_path)
    print(f"Coloring page saved to {output_path}")

def create_a4_coloring_page(input_image_path, output_a4_path):
    # A4 dimensions at 300 DPI (in pixels)
    a4_width, a4_height = 2480, 3508

    # Open the generated image
    input_image = Image.open(input_image_path)

    # Calculate the scaling to fit the A4 canvas without changing the aspect ratio
    aspect_ratio = input_image.width / input_image.height
    if a4_width / a4_height > aspect_ratio:
        # Fit to height
        new_height = a4_height
        new_width = int(a4_height * aspect_ratio)
    else:
        # Fit to width
        new_width = a4_width
        new_height = int(a4_width / aspect_ratio)

    # Resize the image
    resized_image = input_image.resize((new_width, new_height))

    # Create a blank A4 canvas in white
    a4_canvas = Image.new("RGB", (a4_width, a4_height), "white")

    # Calculate position to center the resized image on the A4 canvas
    offset_x = (a4_width - new_width) // 2
    offset_y = (a4_height - new_height) // 2

    # Paste the resized image onto the canvas
    a4_canvas.paste(resized_image, (offset_x, offset_y))

    # Save the final A4-sized image
    a4_canvas.save(output_a4_path)
    print(f"Image stretched and saved to {output_a4_path}")
