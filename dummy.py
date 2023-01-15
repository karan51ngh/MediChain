import socket
from constants import *
from wrapper_funcs import *
from blockchain import *
from helperFunctions import *
import datetime


bc = Blockchain()
# prev_block = bc.get_last_block()
bc.display()

idx = "1"
fn = "Government"
ln = "of India"
age = "75"
dt = str(datetime.datetime.now())
# phv = str(bc.hash(prev_block))
phv = "0"
new_proof, hash_val = bc.mining(idx, fn, ln, age, dt, phv)


print(
    f'the new nonce is {new_proof} and the hash value of our block is {hash_val}')
update_patient_record(idx, fn, ln, age, dt, phv, new_proof)
