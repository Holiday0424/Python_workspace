import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
smtp_server = 'smtp.qq.com'   # SMTP服务器地址
port = 465                    # 端口（SSL加密）
sender = '574048868@qq.com'   # 发件人邮箱
password = 'hadpnxlktxtdbfgf' # 授权码（非登录密码）
receiver = '574048868@qq.com'

# 创建邮件内容
message = MIMEText('hello, send by Python...', 'plain', 'utf-8')
message['From'] = '574048868@qq.com'  # 直接使用你的发件邮箱
message['To'] = Header('邮件测试', 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP_SSL(smtp_server, port)
    smtpObj.login(sender, password)
    smtpObj.sendmail(sender, receiver, message.as_string())
    print("邮件发送成功")

except smtplib.SMTPAuthenticationError as e:
    print(f"认证失败：请检查邮箱账号和授权码是否正确。错误代码：{e}")
    print("提示：授权码是不是填成了QQ密码？或者授权码填错了？")

except smtplib.SMTPConnectError as e:
    print(f"连接失败：无法连接到SMTP服务器。错误代码：{e}")
    print("提示：可能是网络防火墙问题，或者端口填错了。")

except smtplib.SMTPException as e:
    print(f"SMTP 协议异常：{e}")

except Exception as e:
    print(f"未知错误：{e}")
