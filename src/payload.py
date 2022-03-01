import hashlib
import time

class PayloadCreator:
    def __init__(self, private_key, public_key):
        self.private_key = private_key
        self.public_key = public_key

    def create_auth_payload(self):
        time_stamp = int(time.time())
        hash = hashlib.md5((str(time_stamp) + self.private_key + self.public_key).encode('utf-8')).hexdigest()
        return {'ts': time_stamp, 'apikey': self.public_key, 'hash': hash}

    def create_payload(self, limit, offset):
        payload = self.create_auth_payload()
        payload['limit'] = limit
        payload['offset'] = offset
        return payload