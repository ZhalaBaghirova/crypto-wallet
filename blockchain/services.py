from .models import Blockchain
from .utils import proof_of_work, hash
from django.http import JsonResponse, HttpResponse, HttpRequest
import datetime
from uuid import uuid4


    # Mining a new block
def mine_block(blockchain):
        # Creating an address for the node running our server
        node_address = str(uuid4()).replace('-', '') 
        root_node = 'e36f0158f0aed45b3bc755dc52ed4560d' 
      

        previous_block = blockchain.get_last_block()
        previous_nonce = previous_block['nonce']
        nonce = proof_of_work(previous_nonce)
        previous_hash = hash(previous_block)
        blockchain.add_transaction(sender = root_node, receiver = node_address, amount = 1.15, time=str(datetime.datetime.now()))
        block = blockchain.create_block(nonce, previous_hash)
        response = {'message': 'Congratulations, you just mined a block!',
                        'index': block['index'],
                        'timestamp': block['timestamp'],
                        'nonce': block['nonce'],
                        'previous_hash': block['previous_hash'],
                        'transactions': block['transactions']}
        return JsonResponse(response)
    
def add_transaction(blockchain, sender, receiver, amount, time):
        blockchain.add_transaction(sender = sender, receiver = receiver, amount = amount, time = time)

