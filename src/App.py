import payload
import os
import htmlcreator
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()
    privateKey = os.getenv('PRIVATE_KEY')
    publicKey = os.getenv('PUBLIC_KEY')
    characterId = '1009351'  # Hulk ID
    payloadBuilder = payload.PayloadBuilder(privateKey, publicKey)
    htmlcreator.create_output_file(characterId, payloadBuilder)
