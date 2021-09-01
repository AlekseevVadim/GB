"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя:
    имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. 
Реализовать вывод данных о пользователе одной строкой.
"""

def param_user(name, surname, year, city, email, phone):
    print(f'Имя пользователя: {name}, Фамилия пользователя: {surname}, год рождения: {year}, город проживания: {city}, email: {email}, телефон: {phone}.')


param_user(name = 'Vadim', surname = 'Alekseev', year = 1996, city = 'Perm', email = 'gmail.com', phone='8916')
print()
print("Введите через пробел в следующей последовательности:  Имя, Фамилию, год рождения, город проживания, email, телефон.\n")
name, surname, year, city, email, phone = list(input().split())
param_user(name, surname, year, city, email, phone)

