def greet():
    print("                   ")
    print(" Добро пожаловать  ")
    print("     в игру        ")
    print(" Крестики-нолики   ")
    print(" Формат ввода x,y  ")
    print("   x - строка      ")
    print("   y - столбец     ")
    print("                   ")



def show():
    print(f"    | 0 | 1 | 2 |")
    print("-----------------")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("-----------------")

def ask():
    while True:
        cords = input("    Ваш ход: ").split()
        if len(cords) !=2:
            print("Введите 2 координаты (x, y)")
            continue
        x, y = cords
        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите только числа")
            continue
        x, y = int(x), int(y)
        if x < 0 or x > 2 or y < 0 or y > 2:
            print("Координаты вне поля")
            continue
        if field[x][y] != " ":
            print("Клетка заполнена")
            continue
        return x, y

def check_win():
    win_cord = [((0,0),(0,1),(0,2)), ((1,0),(1,1),(1,2)), ((2,0),(2,1),(2,2)),
                ((0,2),(1,1),(2,0)), ((0,0),(1,1),(2,2)), ((0,0),(1,0),(2,0)),
                ((0,1),(1,1),(2,1)), ((0,2),(1,2),(2,2))]
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Крестики победили")
            return True
        if symbols == ["O", "O", "O"]:
            print("Нолики победили")
            return True
    return False

greet()
field = [[" "] * 3 for i in range(3)]
num = 0
while True:
    num += 1

    show()

    if num % 2 == 1:
        print("Ход крестика")
    else:
        print("Ход нолика")

    x, y = ask()

    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "O"

    if check_win():
        break
    if num == 9:
        print("Ничья")
        break