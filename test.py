import pytest
from market import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    print(response.json)  # 調試用
    assert response.status_code == 200
    assert response.json == {"message": "Hello, API is running!"}


# 測試獲取商品清單
def test_get_products(client):
    response = client.get("/products")
    assert response.status_code == 200
    assert isinstance(response.json, list)

# 測試新增商品
def test_add_product(client):
    new_product = {"name": "iPad Pro", "price": 40000}
    response = client.post("/products", json=new_product)
    assert response.status_code == 201
    assert response.json["name"] == "iPad Pro"
    assert response.json["price"] == 40000

# 測試獲取單一商品
def test_get_single_product(client):
    response = client.get("/products/1")
    assert response.status_code == 200
    assert response.json["id"] == 1

# 測試刪除商品
def test_delete_product(client):
    response = client.delete("/products/1")
    assert response.status_code == 200
    assert response.json == {"message": "Product deleted"}

# 測試建立訂單
def test_create_order(client):
    new_order = {"user_id": 1, "product_id": 2}
    response = client.post("/orders", json=new_order)
    assert response.status_code == 201
    assert response.json["user_id"] == 1
    assert response.json["product_id"] == 2
