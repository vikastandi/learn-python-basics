import random
import string

# Write a function which generates a six digit/character random user id.
# The function should return a string of length 6. for e.g. '1ee33d'
def random_user_id():
    digits_chars = string.digits + string.ascii_lowercase
    user_id = ''
    digits_chars_len = len(digits_chars)
    for i in range(0,6):
        user_id += digits_chars[random.randint(0,digits_chars_len - 1)]
    return user_id

def user_id_gen_by_user():
    number_of_chars = int(input("Enter the number of characters for the user id: "))
    number_of_ids = int(input("Enter the number of user ids: "))
    digits_chars = string.digits + string.ascii_lowercase
    user_ids = []
    digits_chars_len = len(digits_chars)

    for i in range(0, number_of_ids):
        user_id = ''
        for j in range(0, number_of_chars):
            user_id += digits_chars[random.randint(0,digits_chars_len - 1)]
        user_ids.append(user_id)
    return user_ids

# write a function named "rgb_color_gen" which will generate rgb colors (3 values ranging from 0 to 255)
def rgb_color_gen():
    rgb = []
    for i in range(0,3):
        rgb.append(random.randint(0,255))
    return rgb

# Write a function named "list_of_hexa_colors" which will generate a list of hexa colors (6 characters) prefixed with '#'
def list_of_hexa_colors():
    hexa_colors = []
    for i in range(0,10):
        hexa_color = '#'
        for j in range(0,6):
            hexa_color += string.hexdigits[random.randint(0,15)]
        hexa_colors.append(hexa_color)
    return hexa_colors

# Write a function named "shuffle_list" which takes a list as an argument and returns a list with shuffled elements.
# write the algorithm from scratch and don't use any inbuilt functions.
def shuffle_list(input_list):
    shuffled_list = []
    input_list_len = len(input_list)
    for i in range(0, input_list_len):
        current_len = len(input_list)
        random_index = random.randint(0, current_len - 1)
        shuffled_list.append(input_list[random_index])
        input_list.pop(random_index)
    return shuffled_list

# Write a function which return an array of seven random numbers in a range of 0 to 9. All the numbers must be unique.
def seven_random_numbers():
    input_numbers = [0,1,2,3,4,5,6,7,8,9]
    random_numbers = []
    for i in range(0,7):
        random_index = random.randint(0, len(input_numbers) - 1)
        random_numbers.append(input_numbers[random_index])
        input_numbers.pop(random_index)
    return random_numbers

if __name__ == "__main__":
    #print(random_user_id())
    #print(user_id_gen_by_user())
    #print(list_of_hexa_colors())
    #print(shuffle_list([1,2,3,4,5,6,7,8,9,10]))
    print(seven_random_numbers())