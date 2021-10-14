DAYS_OF_YEAR = 365  # количество дней в году

start_year = int(input("Ваш год рождения? "))
current_year = int(input("Какой сейчас год? "))  # TODO запросить у пользователя текущий год

summ = current_year - start_year
koll = summ * DAYS_OF_YEAR
print(koll)
