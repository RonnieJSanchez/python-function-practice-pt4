# Write a Python function called max_num()to find the Max of three numbers.
def max_num(x, y, z):
    return max([x, y, z])


print(max_num(7, 9, 10))
print(max_num(26, 67, 18))
print(max_num(1000, 987, 2343))

# Write a Python function called mult_list()  to multiply all the numbers in a list.


def mult_list(lst):
    # if empty list, return 0
    if len(lst) == 0:
        return 0
    # product starts with first element of list
    prod = lst[0]

    # go through list elements and multiply them together
    if len(lst) > 1:
        for i in lst[1:]:
            prod = prod * i

    return prod


print(mult_list([1, 2, 3]))
print(mult_list([]))
print(mult_list([15]))

# Write a Python function called rev_string() to reverse a string.


def rev_string(back_str):
    return back_str[::-1]


print(rev_string(""))
print(rev_string("beach"))
print(rev_string("california"))

# Write a Python function called num_within() to check whether a number falls in a given range


def num_within(x, y, z):
    return x in range(y, z+1)


print(num_within(3, 5, 6))
print(num_within(12, 5, 67))
print(num_within(2, 3, 8))

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
triangle = [[1], [1, 1]]


def pascal(n):
    # base case
    if n < 1:
        print("invalid number")
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2
        # fill up correct number of rows in triangle
        while len(triangle) < n:
            row = []
            row_prev = triangle[row_number - 1]
            # create correct row, then add to triangle (this row will be 1 longer than row before it)
            length = len(row_prev)+1
            for i in range(length):
                # first number is 1
                if i == 0:
                    row.append(1)
                # intermediate numbers get added from previous row
                elif i > 0 and i < length-1:
                    row.append(triangle[row_number-1]
                               [i-1]+triangle[row_number-1][i])
                    # last number is 1
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1

            # print triangle
            for row in triangle:
                print(row)


pascal(2)
pascal(5)
