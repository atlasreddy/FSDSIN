def find_the_difference_q1():
    def find_the_difference(s,t):
        s,t = list(s), list(t)
        s.sort()
        t.sort()

        chars_counter = {}
        chart_counter = {}
        for char_s in s:
            chars_counter[char_s] = s.count(char_s)
        for char_t in t:
            chart_counter[char_t] = t.count(char_t)

        for k,v in chart_counter.items():
            if v == chars_counter.get(k, 0):
                # same character is present in t
                pass
            else:
                return k
    print(find_the_difference("abcd", "abcde"))
    print(find_the_difference("", "y") )
    print(find_the_difference("ae", "aea") )


def count_datatypes_q2():
    def count_datatypes(*args):
        # [int, str, bool, list, tuple, dictionary]
        ret_lst = [0]*6
        for ele in args:
            if isinstance(ele, bool):
                ret_lst[2] += 1
            elif isinstance(ele, str):
                ret_lst[1] += 1
            elif isinstance(ele, int):
                ret_lst[0] += 1
            elif isinstance(ele, list):
                ret_lst[3] += 1
            elif isinstance(ele, tuple):
                ret_lst[4] += 1
            elif isinstance(ele, dict):
                ret_lst[5] += 1
        return ret_lst

    print(count_datatypes(1, 45, "Hi", False))
    print(count_datatypes([10, 20], ("t", "Ok"), 2, 3, 1) )
    print(count_datatypes("Hello", "Bye", True, True, False, {"1": "One", "2": "Two"}, [1, 3], {"Brayan": 18}, 25, 23) )
    print(count_datatypes(4, 21, ("ES", "EN"), ("a", "b"), False, [1, 2, 3], [4, 5, 6]) )


def fib_str_q3():
    def fib_str1(n, lst):
        if n == 0:
            return lst[0]
        elif n == 1:
            return lst[1]
        else:
            return fib_dct[n - 1] + fib_dct[n - 2]

    def fib_str(number, lst):
        global fib_dct
        fib_dct = {0: lst[0], 1: lst[1]}
        for i in range(2, number):
            fib_dct[i] = fib_str1(i, lst)
        target_str = []
        for i in range(number):
            target_str += [fib_dct[i]]
        # for k,v in fib_dct.items():
        #     target_str += [v]
        return ",".join(target_str)
    print(fib_str(3, ["j", "h"]) )
    print(fib_str(5, ["e", "a"]) )
    print(fib_str(6, ["n", "k"]) )


def ones_threes_nines_q4():
    def ones_threes_nines(number):
        nines = number // 9
        number = number % 9
        threes = number // 3
        number = number % 3
        ones = number
        return f"nines: {nines}, threes:{threes}, ones:{ones}"
    print(ones_threes_nines(10))
    print(ones_threes_nines(15))
    print(ones_threes_nines(22))


def fib_q5():
    def fib(number):
        fib_dct = {0: 1, 1: 1}
        for i in range(2, number):
            fib_dct[i] = fib_dct[i-1] + fib_dct[i-2]
        return fib_dct[number-1]
    print(fib(6))
    print(fib(1))
    print(fib(2))


if __name__ == "__main__":
    find_the_difference_q1()
    count_datatypes_q2()
    fib_str_q3()
    ones_threes_nines_q4()
    fib_q5()