import math


def fibonacci_sequence_rec_q1():
    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            # return fib(n-1) + fib(n-2)
            return fib_dct[n - 1] + fib_dct[n - 2]

    def fibonacci_sequence(number):
        global fib_dct
        fib_dct = {0: 0, 1: 1}
        for i in range(2, number + 1):
            fib_dct[i] = fib(i)
        for val in fib_dct.values():
            print(val, end=', ')
        print()

    print(fibonacci_sequence(8))


def factorial_number_rec_q2():
    def factorial(number):
        if 0 < number < 2:
            return 1
        elif number < 0:
            return "Factorial does not exists."
        else:
            return number * fact_dct[number - 1]

    def factorial_number(number):
        global fact_dct
        fact_dct = {0:0, 1:1}
        for i in range(1,number+1):
            fact_dct[i] = factorial(i)
        return fact_dct[number]

    print(factorial_number(5))
    print(factorial_number(125))


def bmi_calculator_q3():
    def bmi_calc(height, weight):
        """
        Bmi calculation
        :param height: in cms
        :param weight: in kgs
        :return: bmi
        """
        height, weight = tuple(map(float, (height,weight)))
        bmi = weight / (height/100) ** 2
        print("BMI value: ", bmi)
        if bmi <= 18.4:
            return ("You are underwight")
        elif bmi <= 24.9:
            return ("You are healthy")
        elif bmi <= 29.9:
            return ("You are over weight.")
        elif bmi <= 34.9:
            return ("You are severely over weight.")
        elif bmi <= 39.9:
            return ("You are obese.")
        else:
            return ("You are severely obese.")
    print(bmi_calc(height=173, weight=78))


def natural_logarithm_q4():
    import math

    def natural_logarithm(number):
        if number <= 0:
            return math.inf
        else:
            return math.log(number)
    print(natural_logarithm(2.719))


def sum_cube_natutal_numbers_q5():
    def sum_cube_natural_numbers(number):
        return (number * (number + 1)/2) **2
    print(sum_cube_natural_numbers(5))


if __name__ == '__main__':
    fibonacci_sequence_rec_q1()
    factorial_number_rec_q2()
    bmi_calculator_q3()
    natural_logarithm_q4()
    sum_cube_natutal_numbers_q5()
