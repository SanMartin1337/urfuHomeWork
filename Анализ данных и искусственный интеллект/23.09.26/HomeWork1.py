import pytest
import numpy as np

"""
задание 1
"""
def test_1():

    mass = np.array([150, 80, 320, 45, 200, 90])
    limit = 100
    result = mass[mass > limit]
    print(f'\n покупки что дороже ста :{result}')

"""
задание 2
"""
def test_2():

    assessments = [2,3,5,4,2,5]
    passs = 4
    for x in assessments:
        if x >= passs:
            print(f'{x}-зачет')
        else:
            print(f'{x}-незачет')

"""
задание 3
"""
def test_3():
    arr1 = np.arange(5, 15)
    print(f'\n{arr1}')
    arr2 = np.linspace(0, 1, 5)
    print(arr2)

"""
задание 4
"""
def test_4():
    vector = np.zeros(5)
    print('--------------------')
    print(vector)
    print('--------------------')
    matrix = np.ones((2, 3), dtype=int)
    print(matrix)
    print('-------------------')
    matrix1 = np.eye(3)
    print(matrix1)

"""
задание 5
"""
def test_5():
    arr = np.array([1, 2, 3, 4, 5, 6])
    table = arr.reshape(2, 3)
    print("Таблица 2х3:")
    print(table)
    print("\nShape таблица:")
    print(table.shape)
    print("\nтрранспонированная таблица:")
    print(table.T)

"""
задание 6
"""
def test_6():
    A = np.array([[10, 20, 30],
                  [40, 50, 60],
                  [70, 80, 90]])
    elements = A[[1],[1]]
    print(f'\n{elements}')

"""
задание 7
"""
def test_7():
    x = np.array([10, 12, 9, 15, 11, 8])

    mean_val = np.mean(x)
    std_val = np.std(x)
    median_val = np.median(x)
    min_val = np.min(x)
    max_val = np.max(x)

    print(f"\ncреднее: {mean_val},"
          f"\nстандартное отклонение: {std_val:.2f}"
          f"\nмедиана: {median_val}"
          f"\nминимум: {min_val}"
          f"\nмаксимум: {max_val}")

"""
задание 8
"""
def test_8():
    price = np.array([350, 420, 200, 500, 390, 450])
    priceInThousand = price / 1000
    print(f"\n{priceInThousand}")

    days = np.where(price > 400)[0]
    print(f"дни когда обед выше 400 : {days}")

    mean_price = np.mean(price)
    print(f'средняя цена за обед {mean_price}')









