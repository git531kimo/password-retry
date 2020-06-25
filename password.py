# 密碼重設程式
# password = 'a123456'
# 讓使用者重複輸入密碼
# 最多輸入3次
# 如果正確就印出'登入成功!'
# 如果錯誤就印出'密碼錯誤，還有  次機會'

password = 'a123456'
i = 3
while True:
	pwd = input('請輸入蜜碼: ')
	if pwd == password:
		print('登入成功')
		break
	else:
		i = i - 1
		print('密碼錯誤! 還有', i, '次機會')
		if i == 0:
			print('請洽系統管理人')
			break