import requestDecorator


def create_image_url(resourceURI, payloadCreator):
    characterResponse = requestDecorator.make_get_request(
        resourceURI, payloadCreator.create_auth_payload())
    data = characterResponse.json()
    thumbnail = data['data']['results'][0]['thumbnail']

    return f"{thumbnail['path']}/standard_large.{thumbnail['extension']}"
