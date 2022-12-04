import json

class Transaction:
    def __init__(self, transaction_data: dict):
        self.transaction_data: dict = transaction_data
        self.seller_signature: bytes = None
        self.buyer_signature: bytes = None
        
    def convertstring(self):
        return json.dumps({"transaction_data": self.transaction_data,"seller_signature": self.seller_signature.hex(),"buyer_signature": self.buyer_signature.hex(),"amount": self.amount})
    
    def converttoprint(self):
        return json.dumps({"transaction_data": self.transaction_data})