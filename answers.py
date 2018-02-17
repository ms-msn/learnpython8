def get_answer(question, answers):
	question = question.lower()
	answer = answers[question]
	return print(answer)

answers = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
question = input( "Введите вопрос: ")

get_answer(question, answers)