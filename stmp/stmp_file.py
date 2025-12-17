import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.application import MIMEApplication

# 第三方 SMTP 服务
smtp_server = 'smtp.qq.com'   # SMTP服务器地址
port = 465                    # 端口（SSL加密）
sender = '574048868@qq.com'   # 发件人邮箱
password = 'hadpnxlktxtdbfgf' # 授权码（非登录密码）
receiver = '574048868@qq.com'

#创建一个带附件的实例
message = MIMEMultipart()
message['From'] = '574048868@qq.com'
message['To'] =  Header("测试", 'utf-8')
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
# 读取文件
with open('test.txt', 'rb') as f:
    file_data = f.read()
#邮件正文内容
message.attach(MIMEText('这是W3Cschool教程Python 邮件发送测试……', 'plain', 'utf-8'))
# 构造附件1，传送当前目录下的 test.txt 文件
# 创建 MIMEApplication 对象
att1 = MIMEApplication(file_data, _subtype="txt")  # _subtype 指定文件类型
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1.add_header('Content-Disposition', 'attachment; filename="test.txt"')

# 将附件添加到邮件中
message.attach(att1)

try:
    # 使用正确的SMTP服务器和端口
    smtpObj = smtplib.SMTP_SSL(smtp_server, port)
    # 登录SMTP服务器
    smtpObj.login(sender, password)
    # 发送邮件
    smtpObj.sendmail(sender, receiver, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPAuthenticationError as e:
    print(f"认证失败：{e}")
except smtplib.SMTPConnectError as e:
    print(f"连接失败：{e}")
except smtplib.SMTPException as e:
    print(f"SMTP异常：{e}")
except Exception as e:
    print(f"其他错误：{e}")
