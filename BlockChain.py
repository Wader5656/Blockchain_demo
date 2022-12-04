import hashlib
import time
from Block import Block, build_merkel_tree
from Transaction import Transaction

def standard_block():
    return Block(0, {"None"}, [], time.time(), 0, 1000)

class BlockChain:

    def __init__(self):
        self.block_chain: list[Block] = [standard_block()]
        self.pending_transaction: list[Transaction] = []
        self.nonce: str = "0000"

    def new_transaction(self, transaction: Transaction):
        if transaction.buyer_signature and transaction.seller_signature:
            self.pending_transaction.append(transaction)
        else:
            print("Signature failed!")

    def last_block(self):
        return self.block_chain[-1]

    def new_block(self):
        new_block = Block(len(self.block_chain), self.pending_transaction, build_merkel_tree(self.pending_transaction),
                          time.time(),
                          self.last_block().hash, self.proof_of_work(self.last_proof()))
        self.block_chain.append(new_block)
        self.pending_transaction = []

    def last_proof(self):
        return self.last_block().proof

    def valid_proof(self, last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()

        return guess_hash[:len(self.nonce)] == self.nonce

    def proof_of_work(self, last_proof):
        proof = 0

        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof