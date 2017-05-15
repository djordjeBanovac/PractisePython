"""Given two .txt files that have lists of numbers in them, 
find the numbers that are overlapping. One .txt file has a 
list of all prime numbers under 1000, and the other .txt 
file has a list of happy numbers up to 1000.

(If you forgot, prime numbers are numbers that can’t be 
divided by any other number. And yes, happy numbers are a 
real thing in mathematics - you can look it up on Wikipedia. 
The explanation is easier with an example, which I will describe below.)"""


def list_from_file(file_name: str) ->list:
    """Opens a file and returns a list"""
    try:
        with open(file_name, 'r') as file:
            return file.readlines()
    except IOError as err:
        print("Error opening file: "+str(err))
        return None


def overlaping_nums(alist: list, blist: list) ->list:
    """returns a list of overlapping items in both lists"""
    return [item.strip() for item in alist if item in blist]


# def overlaping_nums_sets(alist: list, blist: list) ->set:
#     """Version with sets. uses intersection. Needs sanitizing"""
#     return set(alist).intersection(set(blist))

if __name__ == '__main__':
    print("list version:\n", sorted(overlaping_nums(list_from_file("primenumbers.txt"),
                                             list_from_file("happynumbers.txt"))))
   # print("set version:\n", sorted(overlaping_nums_sets(list_from_file("primenumbers.txt"),
    #                                             list_from_file("happynumbers.txt"))))