def get_les1(a:str):
    """Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр"""
    res=0
    for x in str(a):
        res+=int(x) if x.isdigit() else 0
    print(res)


def get_les2(a:str):
    """Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N."""
    if a.isdigit():
        res = 1
        for x in range(1, int(a) + 1):
            res *= x
        print(res)
    else:
        print('error')


def get_les3(a:str):
    """Задайте список из n чисел последовательности (1 + 1 / n)**n и выведите на экран их сумму."""
    if a.isdigit():
        mas=[round((1+1/n)**n,2) for n in range(1,int(a)+1)]
        print(mas,sum(mas),sep=' -> ')
        print
    else:
        print('Error')

def check(s:str):
    res=None
    if 'q' not in s and s.isdigit():
        return int(s)
    return res

def get_les4(a:str):
    """Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры."""
    if a.isdigit():
        interval = [x for x in range(-int(a), int(a) + 1)]
        print(interval)
        x, y = map(check, input('input x,y: ').split(','))
        if x is not None and y is not None and 0 <= x < len(interval) and 0 <= y < len(interval):
            print(interval[x]*interval[y])
        else:
            print('--error--')
    else:
        print('Error')


def get_les5(a: str):
    """ Реализуйте алгоритм перемешивания списка. Из библиотеки random использовать можно только randint"""
    if a.isdigit():
        from random import randint

        def masGenerate(l: int):
            return [randint(0, 9) for x in range(int(a))]

        def shuffle(tmp):
            mas = tmp[:]
            for i in range(len(mas)):
                j = randint(0,len(mas)-1)
                mas[i], mas[j] = mas[j], mas[i]
            return mas

        arr = masGenerate(int(a))

        print('Исходный массив', arr)
        print('Перемешанный массив', shuffle(arr))
    else:
        print('--error--')


if __name__ == '__main__':

    a=input('input nums: ')
    while (a!='qqq'):

        get_les1(a)
        # get_les2(a)
        # get_les3(a)
        # get_les4(a)
        # get_les5(a)

        a = input('input nums: ')
    else:
        print('By')