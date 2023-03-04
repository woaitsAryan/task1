from fastapi import FastAPI

app = FastAPI()


@app.get('/{a:int}+{b:int}')
def add(a: int, b: int):
    sum = a + b
    return {"x" : a, "y": b, "operation" : "addition", "answer" : sum}

@app.get("/{a:int}-{b:int}")
def subtract(a: int, b: int):
    subtract = abs(a - b)
    return {"x" : a, "y" : b, "operation": "subtraction", "answer" : subtract}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)
