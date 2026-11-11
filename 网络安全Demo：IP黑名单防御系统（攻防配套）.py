#网络安全Demo：IP黑名单防御系统（攻防配套）
# 模拟服务器拦截攻击IP、恶意访问拦截

# 服务器黑名单（攻击IP）
black_ip = ["192.168.1.100","127.0.0.55","10.0.0.66"]

def access_check(ip):
    print(f"\n客户端IP：{ip} 发起访问请求")
    if ip in black_ip:
        print("【防御拦截成功】该IP为恶意攻击IP，已拒绝访问！")
    else:
        print("【访问正常】合法IP，允许通行")

print("===== 服务器安全防御系统 =====")
# 模拟3次访问（包含恶意IP + 正常IP）
access_check("192.168.1.100")  # 恶意IP（被拦截）
access_check("127.0.0.1")      # 正常IP（放行）
access_check("10.0.0.66")      # 恶意IP（被拦截）
