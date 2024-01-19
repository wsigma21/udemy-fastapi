from fastapi import FastAPI
from typing import Optional, List
from pydantic import BaseModel

class ShopInfo(BaseModel):
  name: str
  location: str

class Item(BaseModel):
  # データ構造を明記
  name: str
  description: Optional[str] = None
  price: int
  tax: Optional[float] = None

class Data(BaseModel):
  shop_info: Optional[ShopInfo] = None
  items: List[Item]

# インスタンス化
app = FastAPI()

@app.post("/")
async def index(data: Data):
  return {"data": data}