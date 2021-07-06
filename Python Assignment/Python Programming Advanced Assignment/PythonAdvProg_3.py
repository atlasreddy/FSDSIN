import math


def arithmetic_operations_q1():
    def split_operator(que_str, ope):
        return tuple(map(float, que_str.split(ope)))

    def arithmetic_operations(query_string):
        if "+" in query_string:
            num1, num2 = split_operator(query_string, "+")
            return num1 + num2
        elif "-" in query_string:
            num1, num2 = split_operator(query_string, "-")
            return num1 - num2
        elif "*" in query_string:
            num1, num2 = split_operator(query_string, "*")
            return num1 * num2
        elif "//" in query_string:
            num1, num2 = split_operator(query_string, "//")
            if num2 == 0:
                return -1
            else:
                return num1 / num2

    print(arithmetic_operations("12 + 12"))
    print(arithmetic_operations("12 - 12"))
    print(arithmetic_operations("12 * 12"))
    print(arithmetic_operations("12 // 12"))
    print(arithmetic_operations("12 // 0"))


def perimeter_q2():
    def distance_btw_points(p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    def perimeter(lst):
        if len(lst) != 3:
            return "The given set of points does not form a triangle"
        peri = 0
        dists = []
        for i in range(2, -1, -1):
            dists += [distance_btw_points(lst[i], lst[i-1])]
        for i in range(2, -1, -1):
            if dists[i] + dists[i-1] <= dists[i-2]:
                return "The given sides are not of a triangle"
            else:
                peri += dists[i]
        return round(peri, 2)
    print(perimeter( [ [15, 7], [5, 22], [11, 1] ] ))
    print(perimeter( [ [0, 0], [0, 1], [1, 0] ] ) )
    print(perimeter( [ [-10, -10], [10, 10 ], [-10, 10] ] ) )


def tallest_skyscraper_q3():
    def tallest_skyscraper(matrix):
        transpose_matrix = list(zip(*matrix))
        sums = [sum(x) for x in transpose_matrix]
        return max(sums)

    print(tallest_skyscraper([
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [1, 1, 1, 1]
    ]))

    print(tallest_skyscraper([
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [1, 1, 1, 1]
    ]))

    print(tallest_skyscraper([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 1]
    ]))


def is_disarium_q5():
    def is_disarium(number):
        isd = False
        str_num = str(number)
        sm = 0
        for idx in range(len(str_num)):
            sm += int(str_num[idx])**(idx+1)
        if sm == number:
            isd = True
        return isd

    print(is_disarium(75))
    print(is_disarium(135))
    print(is_disarium(544))
    print(is_disarium(518))
    print(is_disarium(466))
    print(is_disarium(8))


def bonus_q4():
    def bonus(days):
        """
        0-32 ==> 0
        33 - 40 ==> 325
        41 - 48 ==> 550
        >48 ==> 600
        :param days:
        :return: days = 45 ==> 32*0 + 8*325 + 5*550
        """
        base_str = f"The bonus for {days} days is "
        ince = 0

        if days > 48:
            d = days - 48
            print(f"{d} * 600", end='+')
            ince += d * 600
            days -= d
        if 41 <= days <= 48:
            d = days - 40
            print(f"{d} * 550", end='+')
            ince += d * 550
            days -= d
        if 33 <= days <= 40:
            d = days - 32
            print(f"{d} * 325", end='+')
            ince += d * 325
            days -= d
        if 0 <= days <= 32:
            days -= 0
            print(f"{days} * 0", end='+')
            ince += days * 0
        if days < 0:
            print(f"{ince} = 0", end='+')
            ince = 0
        print()
        return base_str + f"{ince}"

    print(bonus(45))
    print(bonus(15))
    print(bonus(37))
    print(bonus(50))
    print(bonus(-50))


if __name__ == "__main__":
    arithmetic_operations_q1()
    perimeter_q2()
    tallest_skyscraper_q3()
    bonus_q4()
    is_disarium_q5()
