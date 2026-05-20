from configs.app import router
from controllers.transaction_controller import get_transaction, get_transaction_by_id, create_transaction

transaction_router = router(prefix="/api/v1", tags=["transactions"])

transaction_router.get("/transactions")(get_transaction)
transaction_router.get("/transaction/{transaction_id}")(get_transaction_by_id)
transaction_router.post("/transaction")(create_transaction)
