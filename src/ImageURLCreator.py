import requests
import payload

def createImageURL(resourceURI, payloadCreator):
    characterRequest = requests.get(resourceURI, params=payloadCreator.create_auth_payload())
    data = characterRequest.json()
    thumbnail = data['data']['results'][0]['thumbnail']

    return thumbnail['path'] + "/" + "portrait_xlarge." + thumbnail['extension'] 

if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    import pprint
    pp = pprint.PrettyPrinter()
    load_dotenv()

    private_key = os.getenv('PRIVATE_KEY')
    public_key = os.getenv('PUBLIC_KEY')

    payloadCreator = payload.PayloadCreator(private_key, public_key)
    pp.pprint(createImageURL('https://gateway.marvel.com:443/v1/public/characters/1009351', payloadCreator))