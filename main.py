from fastapi import FastAPI

# インスタンス化
app = FastAPI()

# HTTPメソッドのGETで"/"にアクセスがあったら、その下の関数を処理する
# @app.get("/") # パスオペレーション
# async def index():
#   return {"message": "Hello World"}

@app.get("/countries/japan") 
async def country():
  return {"message": "This is Japan"}

@app.get("/countries/{country_name}") 
async def country(country_name: str):
  return {"country_name": country_name}