from functools import reduce
from countries import countries
from countries_data import countries_data

def higher_order_functions_examples():
    countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
    names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Use for loop to print each country in the countries list
    for country in countries:
        print(country)

    # use map to create a new list by changing each country to uppercase
    countries_upper = list(map(lambda country: country.upper(), countries))
    print(countries_upper)

    # Use map to create a new list by changing each number to its square
    numbers_squared = list(map(lambda number: number ** 2, numbers))
    print(numbers_squared)

    # Use filter to filter out countries containing 'land'
    countries_with_land = list(filter(lambda country: 'land' in country, countries))
    print(countries_with_land)

    # Use filter to filter out countries having exactly six characters
    countries_with_six_characters = list(filter(lambda country: len(country) == 6, countries))
    print(countries_with_six_characters)

    # Use filter to filter out countries starting with 'E'
    countries_starting_with_e = list(filter(lambda country: country.startswith('E'), countries))
    print(countries_starting_with_e)

    # Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
    sum_of_numbers = reduce(lambda even_square1, even_square2: even_square1 + even_square2,
                            list(
                                filter(lambda square: square % 2 == 0,
                                       list(
                                           map(lambda number: number**2, numbers)))))
    print(sum_of_numbers)

    # Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
    countries_sentence = reduce(lambda country1, country2: f'{country1}, {country2}', countries[:-1])
    print(f'{countries_sentence} and {countries[-1]} are north European countries')

# Declare a function called get_string_lists which takes a list as a parameter and returns a list containing only string items
def get_string_lists(items):
    return list(filter(lambda item: type(item) == str, items))

# Declare a function called categorize_countries that reutrns a list of countries with pattern 'land', 'ia', 'island', 'stan' in their names
def categorize_countries():
    return list(filter(lambda country: 'land' in country or 'ia' in country or 'island' in country or 'stan' in country, countries))

# Declare a get_first_ten_countries function that returns the first ten countries in the countries list
def get_first_ten_countries():
    return countries[:10]

def countries_data_operations():
    # use the countries_data and perform following operations
    


if __name__ == '__main__':
    higher_order_functions_examples()
    print(get_string_lists([1, 2, 3, 'Asabeneh', 'Python', 'Finland'])) # ['Asabeneh', 'Python', 'Finland']
    #print(categorize_countries()) # ['Finland', 'Iceland', 'Ireland', 'Pakistan', 'Thailand', 'Uganda', 'United Kingdom', 'United States']