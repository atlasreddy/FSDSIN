def check_score_q1():
    def unravel_list(lsts):
        a = []
        for lst in lsts:
            if isinstance(lst, list):
                a.extend(lst)
            else:
                a.extend([lst])
        return a

    def check_score(lsts):
        scores_init = {"#": 5,
                       "O": 3,
                       "X": 1,
                       "!": -1,
                       "!!": -3,
                       "!!!": -5
                       }
        score = 0
        symbols_lst = unravel_list(lsts=lsts)
        for symbol in symbols_lst:
            score += scores_init.get(symbol, 0)
        if score < 0:
            score = 0
        return score

    print(check_score([["#", "!"], ["!!", "X"]]))
    print(check_score([["!!!","O", "!"], ["X", "#", "!!!"], ["!!", "X", "O"]]))


def combinations_q2():

    def combinations(*args):
        prod = 1
        for value in args:
            prod *= value
        return prod

    print(combinations(2,3))
    print(combinations(3,7,4))
    print(combinations(2,3,4,5))


def encode_morse_q3():
    def encode_morse(query_string):
        char_to_dots = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
            '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..', '9': '----.',
            '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
            ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
            '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
        }
        encoded_string = ""
        for char in query_string:
            encoded_string += char_to_dots.get(char.upper(), '')
            encoded_string += " "
        return encoded_string[:-1]

    print(encode_morse("HELP ME 5 !"))
    print(encode_morse("EDABBIT CHALLENGE"))


def prime_q4():
    def prime(number):
        from math import sqrt,ceil

        num = number
        print(ceil(sqrt(num)))

        # prime numbers are greater than 1
        if num > 1:
            # check for factors
            if num % 2 == 0:
                if num !=2 :
                    print(num, "is not a prime number")
                    print(f"2 x {num//2} = {num}")
                    return False
                else:
                    print("2 is a prime number")
                    return True
            for i in range(3, ceil(sqrt(num))+1, 2):  # skip all even numbers.
                if (num % i) == 0:
                    print(num, "is not a prime number")
                    print(i, "times", num // i, "is", num)
                    break
            else:
                print(num, "is a prime number")

        # if input number is less than
        # or equal to 1, it is not prime
        else:
            print(num, "is not a prime number")
    import time
    stime = time.time()
    # n = 2**103-1
    n = 3976656429941438590393
    n = 9407
    print(f"Number is {n} and calculation time is {time.time()  - stime}")
    prime(n)
    # prime(5151512515524)
    etime = time.time()
    print(f"Execution time is {etime-stime} seconds")


def to_boolean_list_q5():
    def word_to_bitstring(query_string):
        bit_string = ""
        for char in query_string:
            if ord(char) % 2 != 0:
                bit_string += "1"
            else:
                bit_string += "0"
        return bit_string

    def to_boolean_list(query_string):
        bit_string = word_to_bitstring(query_string)
        dct = {"0":False, "1":True}
        lst = [dct.get(x, None) for x in bit_string]
        return lst

    print(to_boolean_list("deep"))
    print(to_boolean_list("loves"))
    print(to_boolean_list("tesh"))


if __name__ == "__main__":
    check_score_q1()
    combinations_q2()
    encode_morse_q3()
    prime_q4()
    to_boolean_list_q5()
