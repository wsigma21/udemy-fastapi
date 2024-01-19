from fastapi import FastAPI

# インスタンス化
app = FastAPI()

# HTTPメソッドのGETで"/"にアクセスがあったら、その下の関数を処理する
@app.get("/") # パスオペレーション
async def index():
  return {"message": "Hello World"}