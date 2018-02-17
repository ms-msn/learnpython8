
def get_vat(price, vat_rate):
	if price > 0 and vat_rate > 0:
		vat = price / 100 * vat_rate
		price_no_vat = price - vat

		return print(price_no_vat)
	else:
		return print("Ошибка данных")

price1 = 100
vat_rate1 = 18
get_vat(price1,vat_rate1)
#get_vat(50, '5')
get_vat(-100, 18)