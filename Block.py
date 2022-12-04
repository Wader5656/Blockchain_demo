import hashlib
import json

def calculate_hash(serial, previous_hash, timestamp, data):
    return hashlib.sha256(
        (str(serial) + str(previous_hash) + str(timestamp) + json.dumps(data)).encode('utf-8')).hexdigest()

class Block:

    def __init__(self, serial, transaction_list, merkelTreeRoot, timestamp, previous_hash, proof):
        self.serial = serial
        self.timestamp = timestamp
        self.transaction_list = transaction_list
        self.merkelTreeRoot = merkelTreeRoot
        self.previous_hash = previous_hash
        self.hash = calculate_hash(serial, timestamp, merkelTreeRoot, previous_hash)
        self.proof = proof

    def convertstring(self):
        return json.dumps({"serial": self.serial, "timestamp": self.timestamp, "merkelTreeRoot": self.merkelTreeRoot, "previous_hash": self.previous_hash, "hash": self.hash, "proof": self.proof, })

def hash_t(transaction):
    return hashlib.sha256(str(transaction).encode('utf8')).hexdigest()

def build_merkel_tree(transactions):
    tmp = []
    counter = 1

    for i in range(0, len(transactions)):
        transactions[i] = hash_t(transactions[i])
    print("---------Merkel tree---------\n")
    while (len(transactions) >= 2):
        print(f"Level: ",counter)
        for i in range(0, len(transactions), 2):
            tmp.append(hash_t(transactions[i] + transactions[i+1]))  
        print("child")
        print(transactions)
        transactions = tmp
        if(len(tmp)==1):
            print("root")
            print(transactions)
            counter+=1
            print("")
            print("This tree has {} levels with the root level".format(counter))
        else:
            print("parent")
            print(transactions)
            counter+=1
        tmp = []
    return transactions[0]


