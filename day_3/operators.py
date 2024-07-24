
def operators_examples():
    # declare my age as integer variable
    age = 250

    # declare height as float variable
    height = 250.5

    # declare a variable "complex_number" and assign a value of complex number
    complex_number = 3 + 5j

    # prompt user to enter base and hright of the triangle and calculate the area of the triangle
    base = float(input('Enter the base of the triangle: '))
    height = float(input('Enter the height of the triangle: '))
    area_of_triangle = 0.5 * base * height
    print(area_of_triangle)

    # prompt user to enter side a, side b and side c of the triangle and calculate the perimeter of the triangle
    side_a = float(input('Enter the side a of the triangle: '))
    side_b = float(input('Enter the side b of the triangle: '))
    side_c = float(input('Enter the side c of the triangle: '))
    perimeter_of_triangle = side_a + side_b + side_c
    print(perimeter_of_triangle)

    # prompt the user to enter length and width of a rectangle and calculate the area of the rectangle
    length = float(input('Enter the length of the rectangle: '))
    width = float(input('Enter the width of the rectangle: '))
    area_of_rectangle = length * width
    print(area_of_rectangle)

    # prompt the user to enter the radius of a circle and calculate the area of the circle
    radius = float(input('Enter the radius of the circle: '))
    area_of_circle = 3.14 * radius ** 2
    print(area_of_circle)

    # Find the slope and euclidean distance between two points (2, 2) and (6, 10)
    x1, y1 = 2, 2
    x2, y2 = 6, 10
    slope = (y2 - y1) / (x2 - x1)
    euclidean_distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    print(slope, euclidean_distance)

    # calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out the corresponding y values.
    x = 2
    y = x**2 + 6 * x + 9
    print(y)
    
    # Find the length of 'python' and 'jargon' and make a falsy comparison statement.
    print(len('python') == len('jargon'))

    # use and operator to check if 'on' is found in both 'python' and 'jargon'
    print('on' in 'python' and 'on' in 'jargon')

    # I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
    print('jargon' in 'I hope this course is not full of jargon')

    # Find the length of the text python and convert the value to float and convert it to string
    print(str(float(len('python'))))

    # Even numbers are divisilble by 2 and the remainder is zero. How do you check if a number is even or not using python?
    number = 10
    print(number % 2 == 0)

    # check if the floor division of 7 by 3 is equal to the int converted value of 2.7
    print(7 // 3 == int(2.7))

    # Check if type of '10' is equal to 10
    print(type('10') == 10)

    # Check if int('9.8') is equal to 10
    print(int(float('9.8')) == 10)

    # Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
    hours = float(input('Enter hours: '))
    rate_per_hour = float(input('Enter rate per hour: '))
    pay = hours * rate_per_hour
    print(pay)

    # Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
    years = int(input('Enter number of years you have lived: '))
    seconds_lived = years * 365 * 24 * 60 * 60
    print(seconds_lived)

    # Write a python script that displays the following table
    # 1 1 1 1 1
    # 2 1 2 4 8
    # 3 1 3 9 27
    # 4 1 4 16 64
    # 5 1 5 25 125
    print('1 1 1 1 1')
    print('2 1 2 4 8')
    print('3 1 3 9 27')
    print('4 1 4 16 64')
    print('5 1 5 25 125')

if __name__ == "__main__":
    operators_examples()

