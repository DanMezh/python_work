# Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами X и Y

X = float(input("Введите координату X:"))
Y = float(input("Введите координату Y:"))
if X > 0 and Y > 0:
    print('1 четверть')
elif X < 0 and Y > 0:
    print('2 четверть')
elif X < 0 and Y < 0:
    print('3 четверть')
elif X > 0 and Y < 0:
    print('4 четверть')
else:
    if X == 0:
        print('на оси OX')
    if Y == 0:
        print('на оси OY')
