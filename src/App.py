import requests
import payload
import random
import pprint
import os
import sys
import ImageURLCreator
from dotenv import load_dotenv
load_dotenv()

private_key = os.getenv('PRIVATE_KEY')
public_key = os.getenv('PUBLIC_KEY')
pp = pprint.PrettyPrinter()

payloadCreator = payload.PayloadCreator(private_key, public_key)

# characterRequest = requests.get('https://gateway.marvel.com:443/v1/public/characters/1009351', params=payloadCreator.create_auth_payload())

storiesRequest = requests.get('https://gateway.marvel.com:443/v1/public/characters/1009351/stories', params=payloadCreator.create_payload(limit=1, offset=0))
data = storiesRequest.json()

if (data['code'] != 200):
    print(f"Oops! Bad request {data['code']}: {data['status']}")
    sys.exit()


numberOfStories = data['data']['total']
randomStoryNumber = random.randint(0, numberOfStories - 1)

storiesRequest = requests.get('https://gateway.marvel.com:443/v1/public/characters/1009351/stories', params=payloadCreator.create_payload(limit=1, offset=randomStoryNumber))

data = storiesRequest.json()
# pp.pprint(data)
attribution = data['attributionText']
result = data['data']['results'][0]

print(storiesRequest.url)
pp.pprint(result['description'])
# pp.pprint(result['characters']['items'])
for character in result['characters']['items']:
    pp.pprint(ImageURLCreator.createImageURL(character['resourceURI'], payloadCreator))
# pp.pprint(result)
print(attribution)