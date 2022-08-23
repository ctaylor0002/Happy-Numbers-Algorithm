
# Split the number as a string then convert to integers
def split_num(number):
    return(list(number))

# Test if an inputted value is an integer rather than a random string
def test_num(number):
    try:
        int(number)
        number_split = split_num(number)
        return number_split
    except ValueError:
        return False

def determine_happy_number(converted_number):
    end_value = 0
    for number in converted_number:
        end_value +=int(number)**2

    print(end_value)