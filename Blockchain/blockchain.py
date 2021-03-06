import hashlib
import json
from time import time
class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        #genesis block
        self.new_block(previous_hash = 1, proof = 100)
    def new_block(self):
        """
        Create a new Block in the Blockchain
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self):
         self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    def hash(block):
        #hashes a block
        pass

    def last_block(self):
        #return last block in chain
        pass
