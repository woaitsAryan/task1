from fastapi import FastAPI

app = FastAPI()

@app.get("/{a:int}*{b:int}")
def multiply(a: int, b: int):
    multiply = a * b
    return {"x" : a, "y" : b, "operation" : "multiplication", "answer" : multiply}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8081)
