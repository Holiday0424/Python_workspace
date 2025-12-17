# FindSeaGoods.py
from fastapi import FastAPI
import uvicorn

app = FastAPI()
goods_table = {'野生大黄鱼': [20, '斤', 168],
               '对虾': [100, '斤', 48],
               '比目鱼': [200, '斤', 69],
               '黄花鱼': [500, '斤', 21]}


@app.get("/goods/{name}")  # 注册路由路径
async def findGoods(name):  # 定义路径操作函数
    if name in goods_table:
        return {
            "商品名称": name,
            "库存": goods_table[name][0],
            "单位": goods_table[name][1],
            "单价(元)": goods_table[name][2]
        }
    else:
        return {"错误": f"商品'{name}'不存在"}


if __name__ == '__main__':
    uvicorn.run(app=app)