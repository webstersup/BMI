#計算BMI
m = input('請輸入體重(單位:公斤)')
h = input('請輸入身高(單位:公尺)')
m = float(m)
h = float(h)
B = m / (h * h)

if B < 18.5 :
	print('BMI為', B, '結果為:體重過輕')
elif B >= 18.5 and B < 24 :
	print('BMI為', B, '結果為:正常範圍')
elif B >= 24 and B < 27 :
	print('BMI為', B, '結果為:過重')
elif B >= 27 and B < 30 :
	print('BMI為', B, '結果為:輕度肥胖')
elif B >= 30 and B < 35 :
	print('BMI為', B, '結果為:中度肥胖')
#else後面不需要再接條件,第一次寫這題錯在這邊
#else B >= 35 :
else:
	print('BMI為', B, '結果為:重度肥胖')



