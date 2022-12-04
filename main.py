import rsa
from BlockChain import BlockChain
from Transaction import Transaction
from User import User

block_chain = BlockChain()

(publicKeyForUser1, privateKeyForUser1) = rsa.newkeys(1024)
(publicKeyForUser2, privateKeyForUser2) = rsa.newkeys(1024)
(publicKeyForUser3, privateKeyForUser3) = rsa.newkeys(1024)
(publicKeyForUser4, privateKeyForUser4) = rsa.newkeys(1024)
(publicKeyForUser5, privateKeyForUser5) = rsa.newkeys(1024)

user1 = User("Alice", publicKeyForUser1, privateKeyForUser1)
user2 = User("Bob", publicKeyForUser2, privateKeyForUser2)
user3 = User("Clive", publicKeyForUser3, privateKeyForUser3)
user4 = User("Donna", publicKeyForUser4, privateKeyForUser4)
user5 = User("Evan", publicKeyForUser5, privateKeyForUser5)

transaction_data1 = {"from": user1.name,"to": user2.name,"amount": 100}

transaction_data2 = {"from": user2.name,"to": user3.name,"amount": 50}

transaction_data3 = {"from": user3.name,"to": user4.name,"amount": 75}

transaction_data4 = {"from": user4.name,"to": user5.name,"amount": 25}

transaction_data5 = {"from": user5.name,"to": user1.name,"amount": 2}

transaction_data6 = {"from": user2.name,"to": user4.name,"amount": 1.5}

transaction1 = Transaction(transaction_data1)
transaction1.seller_signature = user1.signature(transaction1)
transaction1.buyer_signature = user2.signature(transaction1)

transaction2 = Transaction(transaction_data2)
transaction2.seller_signature = user2.signature(transaction2)
transaction2.buyer_signature = user3.signature(transaction2)

transaction3 = Transaction(transaction_data3)
transaction3.seller_signature = user3.signature(transaction2)
transaction3.buyer_signature = user4.signature(transaction2)

transaction4 = Transaction(transaction_data4)
transaction4.seller_signature = user4.signature(transaction2)
transaction4.buyer_signature = user5.signature(transaction2)

transaction5 = Transaction(transaction_data5)
transaction5.seller_signature = user5.signature(transaction2)
transaction5.buyer_signature = user1.signature(transaction2)

transaction6 = Transaction(transaction_data6)
transaction6.seller_signature = user2.signature(transaction1)
transaction6.buyer_signature = user4.signature(transaction1)

block_chain.new_transaction(transaction1)
block_chain.new_transaction(transaction2)
block_chain.new_transaction(transaction3)
block_chain.new_transaction(transaction4)

block_chain.new_block()

block_chain.new_transaction(transaction5)
block_chain.new_transaction(transaction6)

block_chain.new_block()

print("_________________________________________________________________________________\n")
for block in block_chain.block_chain:
    print(block.convertstring(),"\n")
