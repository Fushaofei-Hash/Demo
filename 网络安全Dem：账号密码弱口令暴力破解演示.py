# 网络安全Dem：账号密码弱口令暴力破解演示


# 预设正确账号密码（模拟网站后台）
correct_user = "admin"
correct_pwd = "123456"

# 弱密码字典（常见高危弱口令）
pwd_list = ["123456","666666","888888","admin","123123","000000"]

print("===== 弱口令暴力破解模拟演示 =====")
print("正在尝试破解后台密码...\n")

# 遍历字典爆破
for pwd in pwd_list:
    print(f"尝试密码：{pwd}")
    if pwd == correct_pwd:
        print(f"破解成功！正确密码为：{pwd}")
        print("【安全风险】网站使用弱口令，极易被攻击者入侵！")
        break
else:
    print("字典内密码全部尝试失败")
