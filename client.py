import requests

BASE_URL = "http://localhost:8080"

# 測試取得所有商品
response = requests.get(f"{BASE_URL}/products")
print("取得商品清單:", response.json())

# 測試新增商品
new_product = {"name": "iPad Pro", "price": 40000}
response = requests.post(f"{BASE_URL}/products", json=new_product)
print("新增商品:", response.json())

# 測試刪除商品
response = requests.delete(f"{BASE_URL}/products/1")
print("刪除商品:", response.json())

# 測試建立訂單
new_order = {"user_id": 1, "product_id": 2}
response = requests.post(f"{BASE_URL}/orders", json=new_order)
print("建立訂單:", response.json())

# 測試取得所有訂單
response = requests.get(f"{BASE_URL}/orders")
print("取得所有訂單:", response.json())
