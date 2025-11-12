import pyrfc

#ASHOST = '10.86.100.98'
#CLIENT = '300'
#SYSNR = '00'
#USER = 'BL14'
#PASSWD = 'bl123'

conn_params = {
    "ashost": "10.86.100.98",
    "sysnr": "00",
    "client": "300",
    "user": "BL12",
    "passwd": "bl654321",
    "lang": "ZH"
}


# 创建链接Connection方法的参数 ashost=应用服务器 sysnr=实例编号 client=客户端 user=登录对应客户端的用户名 passwd=密码
#conn = pyrfc.Connection(ashost=ASHOST, sysnr=SYSNR, client=CLIENT, user=USER, passwd=PASSWD)
conn = pyrfc.Connection(**conn_params)

# 使用call方法调用RFC 第一个参数是需要调用的函数模块，后面是RFC导入的参数，注意一定要用参数名=参数值的方式
# call方法的返回值是字典形式键值对是:{'ET_DATA':[],'DATA':[], 'FIELDS': [],'OPTIONS':[]}
try:
    # 3. 定义参数（MATERIAL和PLANT为必填）
    material = "000000001201000657"  # 替换为实际物料号
    plant = "1142"  # 替换为实际工厂代码

    # 4. 调用BAPI_MATERIAL_PLANTDATA_GET
    result = conn.call(
        "BAPI_MATERIAL_GET_DETAIL",
        MATERIAL=material,  # 物料号
        PLANT=plant  # 工厂代码
    )
#    return = result["MATERIAL_GENERAL_DATA"]
#    for mat in materials:
#        print(f"物料号：{mat['MATNR']}，描述：{mat['MAT_DESC']}")
    # 5. 解析返回结果（根据需要提取字段）
    # 5.1 基本数据
    general_data = result.get("MATERIAL_GENERAL_DATA", {})
    print(f"物料描述：{general_data.get('MATL_DESC')}")
    print(f"物料类型：{general_data.get('MATL_TYPE')}")
    print(f"产品组：{general_data.get('DIVISION')}")
    print(f"物料组：{general_data.get('MATL_GROUP')}")

    plant_data = result.get("MATERIALPLANTDATA", {})
    print(f"采购组：{plant_data.get('PUR_GROUP')}")


except Exception as e:
    print(f"调用失败：{str(e)}")
finally:
    # 6. 关闭连接
    conn.close()

#result = conn.call("RFC_READ_TABLE", QUERY_TABLE='MARA')
# print(result)
# 数据简单展示一下
#for i in result['DATA']:
#    print(i)