from fastapi import FastAPI
from typing import Optional

# インスタンス化
app = FastAPI()

# HTTPメソッドのGETで"/"にアクセスがあったら、その下の関数を処理する
# @app.get("/") # パスオペレーション
# async def index():
#   return {"message": "Hello World"}

# @app.get("/countries/") 
# async def country(country_name: str = 'Japan', country_no: int = 1):
#   return {
#     "country_name": country_name,
#     "country_no": country_no,
#   }

@app.get("/countries/") 
async def country(country_name: Optional[str] = None, country_no: Optional[int] = None):
  return {
    "country_name": country_name,
    "country_no": country_no,
  }

