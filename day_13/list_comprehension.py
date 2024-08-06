def list_comprehension_operations():
    # Filter only negative and zero in the list using list comprehension
    # numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
    numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
    print([number for number in numbers if number > 0])

    # Flatten the list of lists to a one dimensional list using list comprehension
    # list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print([number for row in list_of_lists for number in row])

    # using list Comprehension to create a list of tuples
    input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print([(i, 1, i, i **2, i ** 3, i ** 4, i ** 5) for i in input_list])

    countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
    print([[country[0][0].upper(), country[0][0].upper()[:3], country[0][1].upper()] for country in countries])

    # dictionaries
    print([{'country': country[0][0].upper(), 'city': country[0][1].upper()} for country in countries])

    # Write a lamba function which can solve a slope or y-intercept of linear functions
    # f(x) = 2x + 1 and g(x) = x + 3
    f = lambda x: 2 * x + 1
    g = lambda x: x + 3
    print(f'f(0): {f(0)}')
    print(f'g(1): {g(1)}')

    # write a function to add two numbers and return result
    def add_two_numbers(a, b):
        return a + b
    

if __name__ == '__main__':
    list_comprehension_operations()