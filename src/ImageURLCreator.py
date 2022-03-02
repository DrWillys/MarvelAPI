import requestdecorator


def create_image_url(resourceURI, payloadBuilder):
    characterResponse = requestdecorator.make_get_request(
        resourceURI, payloadBuilder.build_auth_payload())
    data = characterResponse.json()
    thumbnail = data['data']['results'][0]['thumbnail']

    return f"{thumbnail['path']}/standard_large.{thumbnail['extension']}"
