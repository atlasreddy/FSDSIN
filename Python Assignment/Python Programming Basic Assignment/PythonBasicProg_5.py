def lcm_q1_gcd_d2():
    def gcd(a,b):
        a,b = max(a,b), min(a,b)
        while b:
            a,b = b,a%b
        return a

    def lcm(a,b):
        return a*b // gcd(a,b)

    print(lcm(4,5))
    print(lcm(20,80))
    print(lcm(37,73))
    print(gcd(37,73))
    print(gcd(4,3))


def number_base_conversion_q3():
    def number_base_conversion(number):
        print(f"Binary of a number {number}: {bin(number)}")
        print(f"Octal of a number {number}: {oct(number)}")
        print(f"Hexadecimal of a number {number}: {hex(number)}")
    number_base_conversion(45)
    number_base_conversion(8)


def ascii_char_value_q4():
    def ascii_char_value(char):
        return ord(char)
    print(ascii_char_value('5'))
    print(ascii_char_value('a'))
    print(ascii_char_value('A'))


def calculator_q5():
    class Calculator:
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def add(self):
            print(f"Add of the two numbers {self.a} + {self.b} = {self.a + self.b}")

        def subtract(self):
            print(f"Difference of the two numbers {self.a} - {self.b} = {self.a - self.b}")

        def mul(self):
            print(f"Product of the two numbers {self.a} * {self.b} = {self.a * self.b}")

        def div(self):
            print(f"Division of the two numbers {self.a} / {self.b} = {self.a / self.b}")

    calc = Calculator(3,4)

    calc.add()
    calc.subtract()
    calc.mul()
    calc.div()


if __name__ == '__main__':
    lcm_q1_gcd_d2()
    number_base_conversion_q3()
    ascii_char_value_q4()
    calculator_q5()
