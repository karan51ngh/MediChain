from itertools import chain
import json
import hashlib
from helperFunctions import *


class Blockchain:
    def __init__(self):
        self.chain = []
        db_list = get_patient_list()
        for i in db_list:
            block = {
                'patient_id': i[0],
                'f_name': i[1],
                'l_name': i[2],
                'age': i[3],
                'timestamp': i[4],
                'previous_hash': i[5],
                'proof': i[6],
            }
            self.chain.append(block)

    def display(self):
        for i in self.chain:
            print(i)

    def get_last_block(self):
        return self.chain[-1]

    def hash(self, block):
        # returns string
        encoded_block = json.dumps(block).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def mining(self, pid, fn, ln, age, ts, phv):
        new_proof = 1
        block = {
            'patient_id': pid,
            'f_name': fn,
            'l_name': ln,
            'age': age,
            'timestamp': ts,
            'previous_hash': phv,
            'proof': str(new_proof),
        }

        check_proof = False

        while check_proof is False:
            block['proof'] = str(new_proof)
            print(block)
            hash_val = self.hash(block)
            if hash_val[:3] == '000':
                print(f'the hash is {hash_val}')
                check_proof = True
            else:
                new_proof += 1

        return new_proof, hash_val

    def is_chain_valid(self, chain):
        pass
