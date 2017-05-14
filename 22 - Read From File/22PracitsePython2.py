"""Extra:

Instead of using the .txt file from above (or instead of, if 
you want the challenge), take this .txt file, and count how many 
of each “category” of each image there are. This text file is actually a 
list of files corresponding to the SUN database scene recognition database, 
and lists the file directory hierarchy for the images. Once you take a look 
at the first line or two of the file, it will be clear which part represents 
the scene category. To do this, you’re going to have to remember a bit about 
string parsing in Python 3. I talked a little bit about it in this post."""


def list_from_file(file_name:str) ->list:
    """Creates list from file with file.readlines(). In every element of the 
     list first two letters are removed. Actual image name starts after 
    the last '/' and in some cases there is a subcategory. Because of 
     that, every element of the list is being split from right. 
     Function returns list of lists."""
    try:
        with open(file_name,'r') as file:
            return [item[3:].rsplit('/',1) for item in file.readlines()]
    except IOError as err:
        print("error reading file: "+str(err))
        return (None)

def create_dict(alist:list) ->dict:
    """Function creates dictionary from list. it takes first element 
    of the sublist as key and on every occurrence of first element of the
    sublist value is increased."""
    category ={}
    for item in alist:
        if item[0] in category:
            category[item[0]] += 1
        else:
            category[item[0]] = 1
    return category

if __name__ == '__main__':
    for key,value in create_dict(list_from_file("Training_01.txt")).items():
        print(key,":",value)
