from fastapi import FastAPI, Body
from typing import Optional
from enum import Enum
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["cashflow_db"]
transactions_collection = db["transactions"]

class TransactionType(str, Enum):
    def __str__(self):
        return str(self.value)
    INCOME = "income"
    EXPENSE = "expense"
    INVEST = "invest"

app = FastAPI()

transactions = []

client 
 
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/transaction")
def get_transaction(item: str = None, tipe: TransactionType = None):
    
    result = transactions_collection

    if item != "":
       result.find({"item": item})
    
    if tipe != None:
       result.find({"type": tipe})

    if tipe == None and item == "":
        result.find({})
    
    return {
        "message": "transactions successfully retrieved",
        "data": list(result)
    }

@app.get("/transaction/{transaction_id}")
def get_transaction_by_id(transaction_id:int):
    print(transaction_id)
    return {
        "message":"This is a transaction endpoint with ID",
        "data": {
            "transaction_id": transaction_id   
        }
    }

@app.post("/transaction")
def create_transaction(item: str = Body(...), amount: float = Body(...), description: Optional[str] = Body(None), tipe: TransactionType = Body(...)):
    
    # transactions.append({"item": item, "amount": amount, "description": description, "type": tipe})
    transactions_collection.insert_one({"item": item, "amount": amount, "description": description, "type": tipe})
    return {
        "message":"Transaction created successfully",
        "data":{"item": item, "amount": amount, "description": description, "type": tipe}
    }