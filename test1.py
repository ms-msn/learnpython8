a = {"Masha":{"city":"Piter","temperature": 10, "wind": "северный"},"Dima":{"city":"Penza","temperature": 30, "wind": "южный"}, "Kate": {"city":"Moscow","temperature": 20, "wind": "west"}}
name = input("Введите имя: ")
print(a.get(name))