def f_q1():
    def f(number):
        # if odd >> return 2
        # if even >> return 8
        lst = (8, 2)
        return lst[number%2]
    print(f(1))
    print(f(2))
    print(f(3))


def majority_vote_q2():
    def majority_vote(lst):
        winner = None
        elements = set(lst)
        w = {} # counter dictionary
        for ele in elements:
            w[ele] = lst.count(ele)
        tmp = 0
        for k,v in w.items():
            if v >= len(lst)/2 and v > tmp:
                winner = k
                tmp = v
        return winner

    print(majority_vote(["A", "A", "B"]) )
    print(majority_vote(["A", "A", "A", "B", "C", "A"]) )
    print(majority_vote(["A", "B", "B", "A", "C", "C"]) )


def censor_string_q3():
    # ##?
    def censor_string(input_string, lst, char):
        words = input_string.split(" ")
        target_string = []
        lsts = list(map(str.lower, lst))
        for word in words:
            if word.lower() in lsts:
                target_string += [char*len(word)]
            else:
                target_string += [word]
        return " ".join(target_string)
    print(censor_string("Today is a Wednesday !", ["Today", "a"], "-") )
    print(censor_string("The cow jumped over the moon .", ["cow", "over"], "*"))
    print(censor_string("Why did the chicken cross the road ?", ["Did", "chicken", "road"], "*") )


def is_polydivisible_q4():
    def is_polydivisible(number):
        isp = False
        lst_str = list(str(number))
        for n in range(1,len(lst_str)+1):
            ndig_num = int("".join(lst_str[:n]))
            if ndig_num % n != 0:
                isp = False
                break
        else:
            # This block is executed when the break did not execute in the for loop.
            isp = True
        return isp

    print(is_polydivisible(1232))
    print(is_polydivisible(123220))


def sum_primes_q5():
    from math import sqrt, ceil

    def prime(num):
        # prime numbers are greater than 1
        if num > 1:
            # check for factors
            if num % 2 == 0:
                if num != 2:
                    # even numbers other than two are not prime
                    return False
                else:
                    return True
            for i in range(3, ceil(sqrt(num))+1, 2):  # skip all even numbers.
                if (num % i) == 0:
                    return False
                    # break
            else:
                return True
        else:
            return False

    def sum_primes(lst):
        if len(lst) == 0:
            return None
        primes = list(filter(prime, lst))
        return sum(primes)

    print(sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) )
    print(sum_primes([2, 3, 4, 11, 20, 50, 71]) )
    print(sum_primes([]))


if __name__ == "__main__":
    f_q1()
    majority_vote_q2()
    censor_string_q3()
    is_polydivisible_q4()
    sum_primes_q5()
