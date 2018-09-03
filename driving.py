country = input('請輸入您的國家:')
age = input('請輸入您的年齡:')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('您可以去報考駕照了!')
	else:
		print('您還無法考駕照!')
elif country == '美國':
	if age >= 16:
		print('您可以去報考駕照了!')
	else:
		print('您還無法考駕照!')
else:
	print('程式目前僅支援判別台灣及美國,請勿輸入其它國家,謝謝!')