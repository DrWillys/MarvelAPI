import requests
import payload
import random
import os
import sys
import ImageURLCreator
import HTMLCreator
from dotenv import load_dotenv
load_dotenv()

private_key = os.getenv('PRIVATE_KEY')
public_key = os.getenv('PUBLIC_KEY')
payloadCreator = payload.PayloadCreator(private_key, public_key)

storiesRequest = requests.get('https://gateway.marvel.com:443/v1/public/characters/1009351/stories',
                              params=payloadCreator.create_payload(limit=1, offset=0))
data = storiesRequest.json()

if (data['code'] != 200):
    print(f"Oops! Bad request {data['code']}: {data['status']}")
    sys.exit()


numberOfStories = data['data']['total']
randomStoryNumber = random.randint(0, numberOfStories - 1)

storiesRequest = requests.get('https://gateway.marvel.com:443/v1/public/characters/1009351/stories',
                              params=payloadCreator.create_payload(limit=1, offset=randomStoryNumber))

data = storiesRequest.json()
result = data['data']['results'][0]

characters = [{'name': character['name'], "url": ImageURLCreator.createImageURL(
    character['resourceURI'], payloadCreator)} for character in result['characters']['items']]

description = result['description'] if result['description'] != "" else "No description for this story."
outputData = {
    "title": result['title'],
    "description": description,
    "characters": characters,
    "attributiontext": data['attributionText']
}

HTMLCreator.create_output_file(outputData)