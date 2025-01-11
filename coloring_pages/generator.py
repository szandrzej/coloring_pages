from openai import OpenAI
import requests

def generate_image(prompt, output_path, api_key):
    client = OpenAI(
        api_key=api_key,  # this is also the default, it can be omitted
    )

    response = client.images.generate(
        prompt=f"Generuj kolorowanke dla dziecka, czarny obrys, nie wypełniaj kolorem: tylko krawedzie i kontury, mozliwe do pokolorowania, mało detali:  {prompt}", 
        n=1, 
        size="1024x1024", 
        response_format="url",
        model="dall-e-3"
    )
    # print(response)
    # exit()
    image_url = response.data[0].url #['data'][0]['url']

    # Download and save the image
    img_data = requests.get(image_url).content
    with open(output_path, 'wb') as handler:
        handler.write(img_data)
    print(f"Image saved to {output_path}")

