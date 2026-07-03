# Проект FitLife - MVP версия 1.0

WATER_PER_KG = 30
ML_IN_LITER = 1000


def calc_bmi(user_weight, user_height):
    """Расчёт индекса массы тела
    user_weight: вес человека
    user_height: рост человека
    """
    return round(user_weight / (user_height ** 2), 1)


def calc_water(user_weight):
    """Расчёт нормы воды в л
    user_weight: вес человека
    """
    return user_weight * WATER_PER_KG / ML_IN_LITER


def input_name(message):
    """Запрашивает у пользователя имя"""
    while True:
        user_name = input(message).strip()
        if user_name.isalpha():
            return user_name
        else:
            print("Ошибка: имя должно содержать только буквы")


def input_weight_float(message, min_weight, max_weight):
    """Запрашивает у пользователя корректный вес"""
    while True:
        try:
            weight = float(input(message))
            if min_weight < weight < max_weight:
                return weight
            print(
                "Ошибка: вес должен быть в пределе от 0 до 400")
        except ValueError:
            print("Ошибка: вес должен быть числом")


def input_height_float(message, min_height, max_height):
    """Запрашивает у пользователя корректный рост"""
    while True:
        try:
            height = float(input(message))
            if min_height < height < max_height:
                return height
            print(
                "Ошибка: рост должен быть в пределе от 0 до 2.3")
        except ValueError:
            print("Ошибка: рост должен быть числом")


def input_age_int(message, min_value, max_value):
    """Запрашивает у пользователя корректное число возраста"""
    while True:
        try:
            value = int(input(message))
            if min_value < value < max_value:
                return value
            print("Ошибка: возраст должен быть в пределе от 0 до 100")
        except ValueError:
            print("Ошибка: возраст должен быть числом")


user_name = input_name("Введите пожалуйста ваше имя ")
user_age = input_age_int("Введите пожалуйста ваш возраст ", 0, 100)
user_weight = input_weight_float("Введите ваш вес в кг ", 0, 400)
user_height = input_height_float(
    "Введите пожалуйста ваш рост в метрах, например 1.75 ", 0, 2.3)

bmi = calc_bmi(user_weight, user_height)
water_l = calc_water(user_weight)

print(f"Отчет для пользователя: {user_name} ({user_age} г.)")
print(f"Твой Индекс Массы Тела(ИМТ): {bmi}")
print(
    "ИМТ показывает, насколько вес соотвествует росту, "
    "при этом ИМТ не учитывает индивидуельные особенности огранизма")
print(f"Рекомендуемая норма воды: {water_l} л. в день")
print("Расчет окончен. Будьте здоровы!")
