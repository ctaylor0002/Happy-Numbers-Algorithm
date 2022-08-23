
# Split the number as a string then convert to integers
def split_num(number):
    return(list(number))

def test_num(number):
    try:
        int(number)
        number_split = split_num(number)
        return number_split
    except ValueError:
        return False