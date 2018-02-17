is_male = {
  'Оля': False,  # если True, то пол мужской
  'Петя': True,
  'Вася': True,
  'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']
for i in names:
	if is_male[i] == True:
		p = 'male'
	else:
		p = 'female'
	print(i, p)