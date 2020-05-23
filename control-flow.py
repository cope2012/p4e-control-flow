GROCERY_LIST = [
    'bread',
    'bananas',
    'apples',
    'cheese',
    'milk'
]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def print_grocery_list():
    print('--- Begin of the list ---')
    for grocery in GROCERY_LIST:
        print(grocery)
    else:
        print('--- End of the list ---')


def sum_numbers(num):
    result = 0

    for tmp in range(num):
        result += tmp

    return result


def even_numbers(numbers_list):
    result_list = []

    for num in numbers_list:
        if num % 2 == 0:
            result_list.append(num)

    return result_list


def no_f_words(word_list):
    filtered_list = []
    for word in word_list:
        if word[0] == 'f':
            continue

        filtered_list.append(word)

    return filtered_list


def find_the_number(num_to_find):
    found = False

    while not found:
        if numbers.pop() == num_to_find:
            found = True

    print(found)


if __name__ == '__main__':
    print_grocery_list()
    # print(sum_numbers(3))
    # print(even_numbers([0, 1, 2, 3, 4, 5, 6, 7, 8]))
    # print(no_f_words(['I', 'fucking', 'love', 'python']))
    # find_the_number(50)
