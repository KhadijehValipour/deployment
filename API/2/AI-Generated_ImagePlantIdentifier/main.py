import requests
import os
import dotenv
import argparse
from text2image import IllusionDiffusion
from identifier import PlantIdentifier




def main():
    dotenv = dotenv.load_dotenv()
    ILLUSION_DIFFUSION_API_KEY = os.getenv("ILLUSION_DIFFUSION_API_KEY")
    PLANTNET_API_KEY = os.getenv("PLANTNET_API_KEY")

    parser = argparse.ArgumentParser(description='Recognize a flower or plant')
    parser.add_argument('--plant_name', type=str, default='Easter Cactus', help='Name of the flower or plant')
    args= parser.parse_args()
    

    try:
        text2image_obj = IllusionDiffusion(ILLUSION_DIFFUSION_API_KEY=ILLUSION_DIFFUSION_API_KEY, prompt=args.prompt)
        if text2image_obj.get_status_code != 200:
            raise Exception("Connecting to server!There is a problem in producing the photo of the plant")
        response= requests.get(text2image_obj.get_image_url, allow_redirects=True) # https://webscraping.ai/faq/requests/what-is-the-purpose-of-the-allow_redirects-parameter-in-requests
        open(f"{args.plant_name}.png", 'wb').write(response.content)
        
        plant_identifier_obj = PlantIdentifier(PLANTNET_API_KEY=PLANTNET_API_KEY, IMG_PATH=f'{args.plant_name}.png')
        if plant_identifier_obj.get_status_code != 200:
            raise Exception("Connecting to server!There is a problem in identifying the photo of the plant")

    except Exception as e:
        print(f"Error: {e}")
    
    else:
        print(plant_identifier_obj.get_flower_plant_name())




if __name__=="__main__":
    main()