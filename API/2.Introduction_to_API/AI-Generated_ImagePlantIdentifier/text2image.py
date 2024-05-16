import json
import requests

# Illusion Diffusion API for generating plant images

class IllusionDiffusion:
    def __init__(self, ILLUSION_DIFFUSION_API_KEY, prompt):
        self.url= 'https://fal.run/fal-ai/illusion-diffusion'
        self.headers={
                    "Authorization": ILLUSION_DIFFUSION_API_KEY,
                    "Content-Type": "application/json"
}
        self.payload= {
                    "image_url": "https://storage.googleapis.com/falserverless/illusion-examples/pattern.png",
                    "prompt": f"(masterpiece:1.4), (best quality), (detailed), {prompt}",
                    "negetive_prompt": "(worst quality, poor details:1.4), lowres, (artist name, signature, watermark:1.4), bad-artist-anime, bad_prompt_version2, bad-hands-5, ng_deepnegative_v1_75t"}
                    
        self.response= requests.post(self.url, headers=self.headers, json=self.payload)


    def get_status_code(self):
        return self.response.status_code
    
    def get_image_url(self):
        return self.response.json()['image']['url']