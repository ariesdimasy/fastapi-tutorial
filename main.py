from configs.app import app, JSONResponse
from configs.app import HTTPException as HttpException
from routers.transaction_route import transaction_router
 
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.exception_handler(HttpException)
def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )

app.include_router(transaction_router)