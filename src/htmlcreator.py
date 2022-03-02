import chevron
import os
import imageurlcreator
import requestdecorator
import random
import sys
from pathlib import Path


def get_story_data(characterId, payloadBuilder, limit, offset):
    storiesResponse = requestdecorator.make_get_request(
        f'https://gateway.marvel.com:443/v1/public/characters/{characterId}/stories', payloadBuilder.build_payload(limit=limit, offset=offset))
    data = storiesResponse.json()

    if (data['code'] != 200):
        status = {data['status']} if 'status' in data else ""
        print(f"Oops! Bad request {data['code']}: {status}")
        sys.exit()
    return data


def get_random_story_number(characterId, payloadBuilder):
    data = get_story_data(characterId, payloadBuilder, limit=1, offset=0)

    numberOfStories = data['data']['total']
    return random.randint(0, numberOfStories - 1)


def create_template_data(characterId, payloadBuilder):
    data = get_story_data(characterId, payloadBuilder, limit=1,
                          offset=get_random_story_number(characterId, payloadBuilder))
    result = data['data']['results'][0]

    characters = [{'name': character['name'], 'url': imageurlcreator.create_image_url(
        character['resourceURI'], payloadBuilder)} for character in result['characters']['items']]

    description = result['description'] if result['description'] != '' else 'No description for this story.'
    return {
        'title': result['title'],
        'description': description,
        'characters': characters,
        'attributionHTML': data['attributionHTML']
    }


def create_output_file(characterId, payloadBuilder):
    templateData = create_template_data(characterId, payloadBuilder)
    with open('index.mustache', 'r') as f:
        output = chevron.render(f, templateData)

    filename = Path('../output/index.html')
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf8') as f:
        f.write(output)
