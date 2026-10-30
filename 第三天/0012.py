has_ticket = False
age = 16
if has_ticket:
    if age >= 18:
        print("凭票进场（成人票）")
    else:
        print("凭票进场（儿童票）")
else:
    print("没有票，不能入场")