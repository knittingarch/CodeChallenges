# Write a function get_products_of_all_ints_except_at_index() that takes a list
# of integers and returns a list of the products.
# Solution by Sarah Dawson (without hints)

import operator

test = [1, 7, 3, 4]
final_products = []

for index, number in enumerate(test):
    print "Original list: ", test
    test2 = list(test)
    print "Index: ", index
    print "Number: ", number
    print "Starting state of the list: ", test2
    test2.remove(number)
    print "Curret state of the list: ", test2
    prod = reduce(operator.mul, test2, 1)
    print "Product of remaining numbers: ", prod
    final_products.append(prod)
    print "Calculated products: ", final_products
    print "State of list after this round of reduces: ", test2


# As a cleaner, finalized function

import operator

def find_product_of_other_numbers(numbers):
    final_products = []
    for number in numbers:
        new_numbers = list(numbers)
        new_numbers.remove(number)
        prod = reduce(operator.mul, new_numbers, 1)
        final_products.append(prod)
    return final_products