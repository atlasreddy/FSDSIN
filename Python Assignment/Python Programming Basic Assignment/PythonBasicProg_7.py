from functools import reduce


def sum_array_q1():
    def sum_array(numbers):
        # sum(numbers)
        # Returns the sum of all the elements using `reduce`
        return reduce((lambda a, b: a + b), numbers)
    print(sum_array((1,2,3,4,56,-5,10,-56)))


def largest_ele_q2():
    def largest_ele(numbers):
        # max(numbers)
        return reduce((lambda a,b: a if a>b else b), numbers)
    print(largest_ele((1,2,3,45,78,23,4)))


def rotate_array_q3():
    def rotate_array(arr, d):
        return arr[d:len(arr)] + arr[0:d]
    print(rotate_array([1,2,3,4,5], 2))


def split_add_array_q4():
    def split_add_array(arr, pos):
        return arr[pos:] + arr[:pos]
    print(split_add_array([1,2,3,4,5,6], 3))

def monotonic_array_check_q5():
    def monotonic_array_check(arr):
        return (
            all(
                arr[i] <= arr[i+1] for i in range(len(arr)-1)
            ) or all(
            arr[i] >= arr[i+1] for i in range(len(arr)-1)
        )
        )
    print(monotonic_array_check((1,2,3,5,6)))
    print(monotonic_array_check((1,2,3,5,6,12,8)))
    print(monotonic_array_check((6,5,4,3,2,1)))


if __name__ == '__main__':
    sum_array_q1()
    largest_ele_q2()
    rotate_array_q3()
    split_add_array_q4()
    monotonic_array_check_q5()
