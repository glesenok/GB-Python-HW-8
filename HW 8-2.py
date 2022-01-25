class NotDivideToZero(Exception):
    def __init__(self):
        self.txt = "Нельзя делить на ноль"

try:
    dividend = int(input("ВВедите 1 число:"))
    divider = int(input("Введите 2 число:"))
    if divider == 0:
        raise NotDivideToZero()
except NotDivideToZero as err:
    print(err.txt)

else:
    print(f"Результат : {dividend / divider}")