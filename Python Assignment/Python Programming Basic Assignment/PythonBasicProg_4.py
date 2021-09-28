def factorial_number_q1():
    def factorial_number(number):
        global fact_dct
        fact = 1
        idx = 1
        while idx <= number:
            fact *= idx
            idx += 1
        return fact

    print(factorial_number(5))


def multiplication_table_q2():
    def multiplication_table(number):
        for i in range(1,11):
            print(f"{number} * {i} = {number*i}")

    multiplication_table(5)


def fibonacci_sequence_q3():
    def fibonacci_sequence(number):
        a,b = 0,1
        idx,sum = 1,0

        while idx <= number:
            print(sum, end=', ')
            a,b = b,sum
            sum = a+b
            idx += 1

    print(fibonacci_sequence(8))


def check_armstrong_number_q4(num=None):
    def check_armstrong_number(number):
        if number is None:
            return None
        f = tuple(map(int, str(number)))
        value = 0
        for val in f:
            value += val ** 3
        return value == number
    # print(check_armstrong_number(153))
    # print(check_armstrong_number(25))
    return check_armstrong_number(num)


def find_armstrong_number_interval_q5():
    def armstrong_number_interval(start=1, end=999):
        for number in range(start, end+1):
            is_arm = check_armstrong_number_q4(number)
            if is_arm:
                print(number, end=', ')
        print()

    # armstrong_number_interval(1,9848021237)
    armstrong_number_interval(1,9999)


def natural_number_sum_q6():
    def sum_natural_numbers(number):
        return number * (number+1) * 0.5

    print(sum_natural_numbers(5))
    print(sum_natural_numbers(50))
    print(sum_natural_numbers(100))


if __name__ == '__main__':
    factorial_number_q1()
    multiplication_table_q2()
    fibonacci_sequence_q3()
    check_armstrong_number_q4()
    find_armstrong_number_interval_q5()
    natural_number_sum_q6()
