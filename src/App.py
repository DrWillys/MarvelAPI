import requestDecorator
import payload
import random
import os
import sys
import imageURLCreator
import htmlCreator
from dotenv import load_dotenv


def get_story_data(characterId, payloadCreator, limit, offset):
    storiesResponse = requestDecorator.make_get_request(
        f'https://gateway.marvel.com:443/v1/public/characters/{characterId}/stories', payloadCreator.create_payload(limit=limit, offset=offset))
    data = storiesResponse.json()

    if (data['code'] != 200):
        status = {data['status']} if 'status' in data else ""
        print(f"Oops! Bad request {data['code']}: {status}")
        sys.exit()
    return data


def get_random_story_number(characterId, payloadCreator):
    data = get_story_data(characterId, payloadCreator, limit=1, offset=0)

    numberOfStories = data['data']['total']
    return random.randint(0, numberOfStories - 1)


def create_template_data(characterId, payloadCreator, randomStoryNumber):
    data = get_story_data(characterId, payloadCreator,
                          limit=1, offset=randomStoryNumber)

    result = data['data']['results'][0]

    characters = [{'name': character['name'], 'url': imageURLCreator.create_image_url(
        character['resourceURI'], payloadCreator)} for character in result['characters']['items']]

    description = result['description'] if result['description'] != '' else 'No description for this story.'
    return {
        'title': result['title'],
        'description': description,
        'characters': characters,
        'attributionHTML': data['attributionHTML']
    }


if __name__ == '__main__':
    load_dotenv()
    privateKey = os.getenv('PRIVATE_KEY')
    publicKey = os.getenv('PUBLIC_KEY')
    characterId = '1009351'  # Hulk ID
    payloadCreator = payload.PayloadCreator(privateKey, publicKey)
    randomStoryNumber = get_random_story_number(characterId, payloadCreator)
    htmlCreator.create_output_file(create_template_data(
        characterId, payloadCreator, randomStoryNumber))
