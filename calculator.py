def calculator():
   while True:
      print("Выберите желаемое действие:\n"
            "Сложение: +\n"
            "Вычитание: -\n"
            "Умножение: *\n"
            "Деление: /\n"
            "Выход из калькулятора: q\n")
      action = input("действие: ")
      if action == "q":
            print("Закрытие программы. . . . .")
            break
      if action in ("+", "-", "*", "/"):
            x = float(input("x = "))
            y = float(input("y = "))
            if action == "+":
               print("%.2f + %.2f = %.2f" % (x, y, x+y))
            elif action == "-":
               print("%.2f - %.2f = %.2f" % (x, y, x-y))
            elif action == "*":
                print("%.2f * %.2f = %.2f" % (x, y, x*y))
            elif action == "/":
               if y != 0:
                  print("%.2f / %.2f = %.2f" % (x, y, x/y))
               else:
                  print("Деление на ноль запрещено!")


calculator()
