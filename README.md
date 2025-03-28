# Flask Market API

這是一個使用 Flask 建立的 RESTful API，模擬簡單的商品與訂單管理系統，支援商品的新增、查詢、刪除，以及訂單的建立與查詢。

## 📌 專案結構
```
├── market.py    # Flask API 主程式
├── test.py      # 使用 pytest 進行 API 測試
└── README.md    # 專案說明文件
```

## 📦 主要功能
- **商品管理**
  - 查詢所有商品
  - 查詢單一商品
  - 新增商品
  - 刪除商品

- **訂單管理**
  - 建立訂單
  - 查詢所有訂單
  - 查詢單一訂單

## 🛠️ 環境需求
- Python 3.13 以上
- Flask
- pytest（用於測試）

### 安裝依賴
```bash
pip install Flask pytest
```

## 🚀 快速開始
### 1. 啟動 Flask API 伺服器
```bash
python market.py
```
> 預設會啟動在 `http://localhost:8080`

### 2. 執行測試
```bash
pytest test.py
```

## 📊 API 介面說明

### 1. 首頁檢測
**GET /**
- 回應範例：
```json
{
    "message": "Hello, API is running!"
}
```

### 2. 商品管理
#### 取得所有商品
**GET /products**
- 回應範例：
```json
[
    {"id": 1, "name": "iPhone 15", "price": 30000},
    {"id": 2, "name": "MacBook Pro", "price": 60000}
]
```

#### 取得單一商品
**GET /products/<product_id>**
- 回應範例：
```json
{"id": 1, "name": "iPhone 15", "price": 30000}
```

#### 新增商品
**POST /products**
- 請求格式：
```json
{
    "name": "iPad Pro",
    "price": 40000
}
```
- 回應範例：
```json
{"id": 3, "name": "iPad Pro", "price": 40000}
```

#### 刪除商品
**DELETE /products/<product_id>**
- 回應範例：
```json
{"message": "Product deleted"}
```

### 3. 訂單管理
#### 建立訂單
**POST /orders**
- 請求格式：
```json
{
    "user_id": 1,
    "product_id": 2
}
```
- 回應範例：
```json
{
    "id": 1,
    "user_id": 1,
    "product_id": 2,
    "status": "pending"
}
```

#### 取得所有訂單
**GET /orders**
- 回應範例：
```json
[
    {
        "id": 1,
        "user_id": 1,
        "product_id": 2,
        "status": "pending"
    }
]
```

#### 取得單一訂單
**GET /orders/<order_id>**
- 回應範例：
```json
{
    "id": 1,
    "user_id": 1,
    "product_id": 2,
    "status": "pending"
}
```

## 📌 注意事項
- 請確保 Flask 伺服器已啟動，且測試程式與 API 路徑對應正確。

## 📚 延伸學習
- [Flask 官方文件](https://flask.palletsprojects.com/)
- [Pytest 官方文件](https://docs.pytest.org/en/latest/)

---
✍️ 由林詠傑製作，歡迎交流與改進！

