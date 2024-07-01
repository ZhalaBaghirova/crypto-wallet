import hashlib
import json

 
def proof_of_work(previous_nonce):
            new_nonce = 1
            check_nonce = False
            while check_nonce is False:
                hash_operation = hashlib.sha256(str(new_nonce**2 - previous_nonce**2).encode()).hexdigest()
                if hash_operation[:4] == '0000':
                    check_nonce = True
                else:
                    new_nonce += 1
            return new_nonce

def hash(block):
            encoded_block = json.dumps(block, sort_keys = True).encode()
            return hashlib.sha256(encoded_block).hexdigest()