def number_checker_q1():
    def number_check(num):
        """
        Check whether the number is positive / negative / zero
        :param num: integer
        :return: +'ve / -'ve / 0
        """
        base_str = f"The number {num} is "
        if num > 0:
            return base_str+"Positive"
        elif num < 0:
            return base_str+"Negative"
        else:
            return base_str+"Zero"

    print(number_check(5))
    print(number_check(-5))
    print(number_check(0))


def odd_even_checker_q2():
    def odd_even_checker(val):
        """
        Odd Even Check
        :param val: integer
        :return: Odd / Even
        """
        base_str = f"The value {val} is "
        if val % 2 == 0:
            return base_str + "Even"
        else:
            return base_str + "Odd"

    print(odd_even_checker(5))
    print(odd_even_checker(4))


def leap_year_checker_q3():
    def leap_year_check(year):
        """
        Leap year check.
        :param year: integer
        :return: LEAP / Not a leap year
        """

        if year % 100 == 0:
            if year % 400 == 0:
                return f"{year} is a Leap Year"
            else:
                return f"{year} is NOT a Leap Year"
        if year % 4 == 0 :
            return f"{year} is a Leap year"
        else:
            return f"{year} is NOT a Leap Year"

    print(leap_year_check(2016))
    print(leap_year_check(2015))
    print(leap_year_check(1500))
    print(leap_year_check(2000))


def prime_check_q4(number=None):
    from math import sqrt, ceil

    def is_prime(num):
        """
        Checks whether the number is prime or not
        :param num: integer
        :return: True if num is prime else False
        """
        if num is None:
            return None

        # prime numbers are greater than 1
        if num > 1:
            # check for factors
            if num % 2 == 0:
                if num != 2:
                    # even numbers other than two are not prime
                    return False
                else:
                    return True
            for i in range(3, ceil(sqrt(num)) + 1, 2):  # skip all even numbers.
                if (num % i) == 0:
                    return False
                    # break
            else:
                return True
        else:
            return False

    # print(is_prime(5))
    # print(is_prime(6))
    # print(is_prime(7))
    # print(is_prime(2))
    return is_prime(number)


def print_primes_interval_q5():
    def print_primes_interval(start=1, end=10000):
        """
        Prints the prime numbers in the interval specified inclusive
        :param start: start of the number
        :param end: end of the number
        :return: None
        """
        for num in range(start, end+1):
            if prime_check_q4(num):
                print(num, end=', ')
        print()

    print_primes_interval(1, 10000)


if __name__ == '__main__':
    number_checker_q1()
    odd_even_checker_q2()
    leap_year_checker_q3()
    prime_check_q4()
    print_primes_interval_q5()
