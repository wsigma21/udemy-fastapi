# ローカル内で立てたサーバでAPIに対してリクエストを送る
import requests
import json

def main():
  # エンドポイント
  url = 'http://127.0.0.1:8000/item/'
  body = {
    "name": "White T-shirts",
    "description": "Good Item",
    "price": 500,
    "tax": 1.1
  }
  res = requests.post(url, json.dumps(body))
  print(res.json())


if __name__ == "__main__":
  main()