

from typing import Optional
from enums.tipe_enum import TransactionType
from configs.app import body
from configs.database import transactions_collection
from bson import json_util
import json

#@app.get("/transactions")
def get_transaction(item: str = None, tipe: TransactionType = None):
    
    result = [1,2,3]

    if item != None:
        result = transactions_collection.find({"item": item})
    
    if tipe != None:
        result = transactions_collection.find({"type": tipe})

    if tipe == None and item == None:
        result = transactions_collection.find({})
    
    # print("item:", item)
    # print("type:", tipe)
    # print(result)
    result_list = list(result) # ini kursor anyiiinggg , dia bakal kosong lagi 
    # print(result_list)
    # print(json_util.dumps(result_list, indent=4))
    # print(json.loads(json_util.dumps(result_list)))

    return {
        "message": "transactions successfully retrieved",
        "data": json.loads(json_util.dumps(result_list))
    }
    

# @app.get("/transaction/{transaction_id}")
def get_transaction_by_id(transaction_id:int):
    print(transaction_id)
    return {
        "message":"This is a transaction endpoint with ID",
        "data": {
            "transaction_id": transaction_id   
        }
    }

# @app.post("/transaction")
def create_transaction(item: str = body(...), amount: float = body(...), description: Optional[str] = body(None), tipe: TransactionType = body(...)):
    
    # transactions.append({"item": item, "amount": amount, "description": description, "type": tipe})
    transactions_collection.insert_one({"item": item, "amount": amount, "description": description, "type": tipe})
    return {
        "message":"Transaction created successfully",
        "data":{"item": item, "amount": amount, "description": description, "type": tipe}
    }