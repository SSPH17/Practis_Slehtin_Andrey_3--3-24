# app.py

def calculate_discount(price, discount):
    # Ошибка 1: забыли преобразовать discount в число (может быть строкой)
    return price - price * discount

def get_user_name():
    # Ошибка 2: опечатка в переменной (user_nme вместо user_name)
    user_nme = "Alex"
    return user_nme

def main():
    price = 100
    discount = "0.2"  # Ошибка 3: передаём строку вместо числа
    final_price = calculate_discount(price, discount)
    
    name = get_user_name()
    print(f"{name}, ваша итоговая цена: {final_price}")

    # Ошибка 4: лишний вывод, который позже захочется убрать
    print("Спасибо за покупку!")

if __name__ == "__main__":
    main()
