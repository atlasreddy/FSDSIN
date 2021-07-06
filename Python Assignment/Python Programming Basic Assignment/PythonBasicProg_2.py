import math


def convert_km_to_miles_q1():
    def convert_km_to_miles(value):
        """
        Converts Kilometers to miles
        :param value: kilometer value
        :return: miles value
        """
        if isinstance(value, str):
            value = float(value)
        if not isinstance(value, float) and not isinstance(value, int):
            return "Only numeric values can be converted from km to miles"
        miles = 0.621371 * value
        return f"{value} Kilometers converted to miles: {miles}"

    print(convert_km_to_miles(3))
    print(convert_km_to_miles("3"))
    print(convert_km_to_miles(3.0))


def convert_celsius_to_fahrenheit_q2():
    def convert_celsius_to_fahrenheit(value):
        """
        Converts the celsius to fahrenheit value
        :param value: celsius value
        :return: fahrenheit value corresponding to the given celsius value
        """
        if isinstance(value, str):
            value = float(value)
        if not isinstance(value, float) and not isinstance(value, int):
            return "Only numeric values can be converted"

        fahrenheit = 32 + (value*9/5)
        return f"{value} celsius = {fahrenheit} fahrenheit"

    print(convert_celsius_to_fahrenheit(0))
    print(convert_celsius_to_fahrenheit(50))


def display_calendar_q3():
    import calendar

    def display_calendar(yr, mnt):
        """
        This function prints the calendar of the month to the console.
        :param yr: Year
        :param mnt: Month
        :return: None
        """
        print(calendar.month(yr,mnt))
    display_calendar(2021, 6)
    display_calendar(2021, 7)


def quadratic_equation_solver_q4():
    def quadratic_equation_solver(x2=0,x=0,const=0):
        """
        This function is to solve the quadratic equation.
        :param x2: coefficient of x**2
        :param x: coefficient of x
        :param const: constant term
        :return: roots of quadratic equation
        """
        a,b,c = map(float, (x2,x,const))
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            return f"The roots of {x2}x**2 + {x}x + {const} = 0 are  imaginary"
        else:
            root1 = (-b + math.sqrt(discriminant)) / (2*a)
            root2 = (-b - math.sqrt(discriminant)) / (2*a)
            return f"The roots of {x2}x**2 + {x}x + {const} = 0 are {root1}, {root2}"

    print(quadratic_equation_solver(4,4,1))
    print(quadratic_equation_solver(4,4,6))


def swap_two_variables_q5():
    def swap_two_variables(a,b):
        """
        This function swaps two variables.
        :param a: variable a
        :param b: variable b
        :return: swap a and b
        """
        a,b = b,a
        return a,b

    print(swap_two_variables(4,5))
    print(swap_two_variables(5,5))
    print(swap_two_variables(5,4))


if __name__ == "__main__":
    convert_km_to_miles_q1()
    convert_celsius_to_fahrenheit_q2()
    display_calendar_q3()
    quadratic_equation_solver_q4()
    swap_two_variables_q5()
