"""
7. Пирожок в столовой стоит `a` гривен и `b` копеек. Определите, сколько гривен и копеек нужно заплатить за `n`
пирожков. Программа получает на вход три числа: `a`, `b`, `n`, и должна вывести два числа: стоимость покупки - гривен
и копеек.
"""
a = int(input("гривны "))
b = int(input("копейки "))
a = a*100  # гривны перевожу в копейки и с ними делаю расчёты
ab = (a+b)  # цена в копейках
n = int(input("количество пирожков "))
ab = ab*n  # стоимость всех пирожков
print(ab//100, 'гривен', ab % 100, 'копеек')
