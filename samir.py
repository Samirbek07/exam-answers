# task 1
the_list = [1, 2, 3, 4, 6, 7, 8, 9, 10]


def missing(nums):

    anumbers = set(range(1, 11))


    missingnumber = (anumbers - set(nums)).pop()

    return missingnumber

missingnumber = missing(the_list)

print(f"The missing number is: {missingnumber}")



# task 2

# people = int(input("people: "))
#
# def find(num):
#     conc = num // 5
#     do = conc
#     if num % 5 > 1:
#         do += 1
#     return do
# print(find(people))


# task 3

percentage = float(input("Enter the percentage: "))
list = [10, 23, 7, 100, 20, 50, 24]

def finder(percent, numberl):
    result = []
    for x in numberl:
        result.append(percent / 100 * x)
    return result

print(f"{percentage}% of {list} is: {finder(percentage, list)}")




