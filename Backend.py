from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
app = FastAPI()

class CalcRequest(BaseModel):
    a: float
    b: float
    operation: str

@app.post("/calculate")
def calculate(req: CalcRequest):
    a, b, op = req.a, req.b, req.operation
    if op == "add":
        result = a + b
    elif op == "subtract":
        result = a - b
    elif op == "multiply":
        result = a * b
    elif op == "divide":
        if b == 0:
            return {"error": "Division by zero"}
        result = a / b
    else:
        return {"error": "Invalid operation"}
    return {"result": result}

# if __name__ == "__main__":
#     uvicorn.run(
#         "Backend:app",           # "module_name:app_instance"
#         host="127.0.0.1",     # or "0.0.0.0" to expose publicly
#         port=8000,
#         reload=True           # auto-reload on code changes (dev only)
#     )

