
def fib_fast_q1():
    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            # return fib(n-1) + fib(n-2)
            return fib_dct[n-1] + fib_dct[n-2]

    def fib_fast(number):
        global fib_dct
        fib_dct = {0: 0, 1: 1}
        for i in range(2,number+1):
            fib_dct[i] = fib(i)
        return fib(number)

    print(fib_fast(5))
    print(fib_fast(10))
    print(fib_fast(20))
    print(fib_fast(50))


def convert_to_hex_q2():
    def convert_to_hex(inp_string):
        return " ".join([hex(ord(f))[2:] for f in inp_string])
    print(convert_to_hex("hello world"))
    print(convert_to_hex("Big Boi"))
    print(convert_to_hex("Marty Poppinson"))


def uncensor_q3():
    def uncensor(inp_string, vow):
        if len(vow) < 1:
            vow = ["" for i in range(len(inp_string))]
        star_count = 0
        lst_string = list(inp_string)
        for char_idx in range(len(lst_string)):
            char = lst_string[char_idx]
            if char == "*":
                lst_string[char_idx] = vow[star_count]
                star_count += 1
        return "".join(lst_string)

    print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))
    print(uncensor("abcd", ""))
    print(uncensor("*PP*RC*S*", "UEAE") )


def get_domain_q4():
    # !pip install dnspython
    import dns.resolver

    def get_domain(ip_addr):
        try:
            result = dns.resolver.resolve(ip_addr, 'PTR')

            for val in result:
                print('PTR Record : ', val.to_text())
        except Exception as exception:
            print(exception)

    print(get_domain("8.8.8.8"))
    print(get_domain("8.8.4.4"))


def fact_of_fact_q5():
    def factorial(number):
        if 0 < number < 2:
            return 1
        elif number < 0:
            return "Factorial does not exists."
        else:
            # return number * factorial(number-1)
            return number * fact_dct[number-1]

    def fact_of_fact(number):
        global fact_dct
        fact_dct = {0:1, 1:1}
        for i in range(1,number+1):
            fact_dct[i] = factorial(i)
        prod = 1
        for i in range(number+1):
            prod *= fact_dct[i]
        return prod

    print(fact_of_fact(4))
    print(fact_of_fact(5))
    print(fact_of_fact(6))


if __name__ == "__main__":
    fib_fast_q1()
    convert_to_hex_q2()
    uncensor_q3()
    get_domain_q4()
    fact_of_fact_q5()
