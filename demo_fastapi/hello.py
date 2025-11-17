from fastapi  import FastAPI
app = FastAPI()  # 注意类名是FastAPI（首字母大写）

@app.get("/")  # 定义根路径接口
def read_root():
    return {"message": "Hello, FastAPI!"}
#根路径：http://127.0.0.1:8000 → 显示 {"message": "Hello, FastAPI!"}
@app.get("/items/{item_id}")  # 带参数的接口
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}
#- 带参数接口：http://127.0.0.1:8000/items/123?q=test → 显示 {"item_id": 123, "query": "test"}。
#- 自动文档：http://127.0.0.1:8000/docs → 可交互式测试所有接口。