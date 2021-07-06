def pentagonal_q1():
    # source: https://en.wikipedia.org/wiki/Centered_pentagonal_number
    # Pn = (5*n*n - 5*n + 2) // 2
    # Pn = 3(Pn-1 - Pn-2) + Pn-3, P1 = 1; P2=6; P3=16
    def pentagonal(n):
        pent_number = 0
        if n > 0:
            pent_number = (5*n*n - 5*n + 2) // 2
        return pent_number
    print(pentagonal(1))
    print(pentagonal(2))
    print(pentagonal(3))
    print(pentagonal(8))


def encrypt_q2():
    def encrypt(string):
        rev_str = string[::-1]
        vowel_dct = {"a": '0',
                     "e": '1',
                     "i": '2',
                     "o": '2',
                     "u": '3'}
        tmp_str = "".join([vowel_dct.get(a,a) for a in rev_str])
        return tmp_str + "aca"
    print(encrypt("apple") == "1lpp0aca")
    print(encrypt("banana") == "0n0n0baca")
    print(encrypt("karaca") == "0c0r0kaca")
    print(encrypt("burak") == "k0r3baca")
    print(encrypt("alpaca") == "0c0pl0aca")


def has_friday_13_q3():
    import datetime

    def has_friday_13(mm, yyyy):
        mm,yyyy = str(mm), str(yyyy)
        return (
            True if datetime.datetime.strptime('13 ' + ' ' + mm + ' ' + yyyy, '%d %m %Y').weekday() == 4 else False)
    print(has_friday_13(3,2020))
    print(has_friday_13(10,2017))
    print(has_friday_13(1,1985))


def bad_cookie_regex_q4():
    import re

    def negative_look_behind_cookie_regex(lst):
        lst = map(str.lower, lst)
        pattern = re.compile("(?<!(good) )cookie")

        return len(re.findall(pattern, ", ".join(lst)))

    print(negative_look_behind_cookie_regex(
        lst=['bad cookie', 'good cookie', 'bad cookie', 'good cookie', 'good cookie']
    ))


def pluralize_q5():
    def pluralize(lst):
        return_set = set()
        counter = {}
        for ele in lst:
            counter[ele] = counter.get(ele, 0) + 1
        for ele, count in counter.items():
            if count < 2:
                return_set.add(ele)
            else:
                if ele.endswith("y"):
                    return_set.add(ele[:-1]+"ies")
                else:
                    return_set.add(ele+"s")
        return return_set

    print(pluralize(["cow", "pig", "cow", "cow"]) )
    print(pluralize(["table", "table", "table"]) )
    print(pluralize(["chair", "pencil", "arm"]) )
    print(pluralize(["category", "category"]) )


if __name__ == "__main__":
    pentagonal_q1()
    encrypt_q2()
    has_friday_13_q3()
    bad_cookie_regex_q4()
    pluralize_q5()
