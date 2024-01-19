from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
  # データ構造を明記
  name: str
  description: Optional[str] = None
  price: int
  tax: Optional[float] = None


# インスタンス化
app = FastAPI()

@app.post("/item/")
async def create_item(item: Item):
  return {"message": f"{item.name}は税込価格{int(item.price * item.tax)}円です"}