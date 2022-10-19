import math

# определение функции декоратора
def select(input_func):
    def output_func():      # определяем функцию, которая будет выполняться вместо оригинальной
        print("********************************")  # перед выводом оригинальной функции выводим всякую звездочки
        input_func()                # вызов оригинальной функции
        print("********************************")  # после вывода оригинальной функции выводим всякую звездочки
    return output_func

@select
def calculating_discriminant_positive():

    discriminant = (b**2) - (4*a*c)

    def discriminant_positive():
        x1 = (-b - math.sqrt(discriminant)) / 2 * a
        x2 = (-b + math.sqrt(discriminant)) / 2 * a
        print(f"Коэффициенты a = {a}; b = {b}; c = {c}")
        print(f"X1 = {x1}, X2 = {x2}")

    def discriminant_null():
        print(f"Коэффициенты a = {a}; b = {b}; c = {c}")
        x = -b / 2 * a
        print(f"X1 = {x}, X2 = {x}")

    def  discriminant_nonD():
        print("Действительных корней нет")

    if discriminant > 0:
        discriminant_positive()

    if discriminant == 0:
        discriminant_null()

    if discriminant < 0:
        discriminant_nonD()

@select
def coefficients_null_a():
    print("Значений нет. На 0 делить нельзя")

@select
def coefficients_null():
    print("Х может принимать любые значения")


if __name__ == '__main__':
    a = float(input())
    b = float(input())
    c = float(input())

    if a == 0 and b !=0 and c !=0:
        coefficients_null_a()
    else:
        if a or b or c > 0:
            calculating_discriminant_positive()

        if (a == 0 and b == 0 and c == 0) :
            coefficients_null()

