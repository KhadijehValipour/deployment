import json
import requests


# PlantNet API for recognizing plant names

class PlantIdentifier():
    def __init__(self,PLANTNET_API_KEY, IMG_PATH):
        self.url= "https://my-api.plantnet.org/v2/identify/all"
        self.headers={}
        self.payload= {
            "api_key": PLANTNET_API_KEY}
        self.file= IMG_PATH
        self.files={
            'images': open(f'{self.file}','rb')}
        self.response=requests.post(self.url, headers=self.headers, params=self.payload, files=self.files)


    def get_status_code(self):
        return self.response.status_code

    def get_flower_plant_name(self):
        return self.response.json().get('results')[0]['spacies']['commonNames']    