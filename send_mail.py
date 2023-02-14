from smtplib import SMTP
from email.message import EmailMessage
import json

# 获取必要数据
with open("./account.json", "r", encoding='utf-8') as f:
	account = json.load(f)

with open("./info.json", "r", encoding='utf-8') as f:
	info = json.load(f)

# 构造邮件
msg = EmailMessage()

msg["Subject"] = '“TFTS”播客字幕--{}'.format(info["title"])
msg["From"] = account["address"]
msg["To"] = "lingjiangxu@qq.com"
msg.set_content(info["summary"])

with open("subscript.pdf", "rb") as f:
	msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename="subscript.pdf")

# 发送邮件
server = SMTP(host="smtp.126.com", port='25')
server.login(account["address"], account["password"])
server.send_message(msg)
print("发送成功！")
server.quit()
