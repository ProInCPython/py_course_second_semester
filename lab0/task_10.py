command = input("Введите число или слово 'стоп'. ")

while command != "стоп":
    try:
        print(float(command))
        command = input("Введите число или слово 'стоп'. ")
    except:
        command = input("Ошибка: Введите число или слово 'стоп'. ")