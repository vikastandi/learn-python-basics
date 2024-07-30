# Declare a function add_two_numbers. It takes two arguments and returns the sum of them.
def add_two_numbers(a, b):
    return a + b

# Write a function "are_of_circle" that takes a radius as an argument and returns the area of the circle.
def area_of_circle(radius):
    return 3.14 * radius ** 2

# Write a functin called "add_all_nums" which takes arbitrary number of arguments and returns the sum of all the arguments.
# Check if all the list items are numbers. If not, return "Invalid input".
def add_all_nums(*args):
    total = 0
    for num in args:
        if not isinstance(num, (int, float)):
            return "Invalid input"
        total += num
    return total

# write function "convert_celsius_to_fahrenheit" that takes a temperature in Celsius and returns it in Fahrenheit.
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Write a function called check-season that takes a month as an argument and returns the season of the month.
# Check if the month is valid or not. If not, return "Invalid input".
def check_season(month):
    if month in ["January", "February", "March"]:
        return "Winter"
    elif month in ["April", "May", "June"]:
        return "Spring"
    elif month in ["July", "August", "September"]:
        return "Summer"
    elif month in ["October", "November", "December"]:
        return "Autumn"
    else:
        return "Invalid input"
    
# Write a function called calculate_slope that takes two points as arguments and returns the slope of the line.
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

# Write a fnction "solve_quadratic_eqn" that takes three arguments a, b, c and returns the solutions of the quadratic equation.
def solve_quadratic_eqn(a, b, c):
    return (-b + (b ** 2 - 4 * a * c) ** 0.5) / 2 * a, (-b - (b ** 2 - 4 * a * c) ** 0.5) / 2 * a

# Declare a function named "print_list" that takes a list as an argument and prints all the items in the list.
def print_list(lst):
    for item in lst:
        print(item)

# Declare a function named "capitalize_list_items" that takes a list as an argument and returns a new list with all the items capitalized.
def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]

# Declare a function named "remove_item" that takes a list and an item as arguments and returns a new list with the item removed.
def remove_item(lst, item):
    return [i for i in lst if i != item]

# Declare a function name "even_and_odds". It takes a positive integer as parameter adn it counts number of even and odd numbers in the number.
def even_and_odds(num):
    even = 0
    odd = 0
    for i in range(0, num + 1):
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

# Declare a function named "factorial". It takes a positive integer as argument and returns the factorial of the number.
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
    
# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std_deviation.
def calculate_mean(lst):
    return sum(lst) / len(lst)

def calculate_median(lst):
    lst.sort()
    n = len(lst)
    if n % 2 == 0:
        return (lst[n // 2] + lst[n // 2 - 1]) / 2
    else:
        return lst[n // 2]
    
def calculate_mode(lst):
    return max(set(lst), key = lst.count)

def calculate_range(lst):
    return max(lst) - min(lst)

def calculate_variance(lst):
    mean = calculate_mean(lst)
    return sum([(x - mean) ** 2 for x in lst]) / len(lst)

def calculate_std_deviation(lst):
    return calculate_variance(lst) ** 0.5

# Write a function called "is_prime" that takes a number as an argument and returns True if the number is prime, False otherwise.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Write a function which check if all items are unique in the list.
def check_unique(lst):
    return len(lst) == len(set(lst))

# write a function which checks if all the items in the list are of the same data type.
def check_same_data_type(lst):
    return len(set(map(type, lst))) == 1

# write a function which check if provided variable is a valid python variable.
def is_valid_variable(variable):
    return variable.isidentifier()


if __name__ == "__main__":
    print(add_two_numbers(1, 2)) # 3
    print(even_and_odds(100)) # (51, 50)

