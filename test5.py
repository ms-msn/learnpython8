groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
n = 0
for i in groups:
	n += 1
	print("Группа " + str(n) + ":" , ",".join(i))
	