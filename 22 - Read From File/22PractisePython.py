"""Given a .txt file that has a list of a bunch of names,
count how many of each name there are in the file, 
and print out the results to the screen. I have a .txt file for you, 
if you want to use it!

Extra:

Instead of using the .txt file from above (or instead of, if 
you want the challenge), take this .txt file, and count how many 
of each “category” of each image there are. This text file is actually a 
list of files corresponding to the SUN database scene recognition database, 
and lists the file directory hierarchy for the images. Once you take a look 
at the first line or two of the file, it will be clear which part represents 
the scene category. To do this, you’re going to have to remember a bit about 
string parsing in Python 3. I talked a little bit about it in this post."""


def read_from_file(file_name:str) ->dict:
    """Function reads file, removes \n. If entry with the 'key'
    key exists, entry is updated, otherwise new entry is created and
     default value of 1 is added to that entry. FUnction returns dictionary"""
    names_dict = {}
    with open(file_name,'r') as file:
        for line in file:
            line = line.strip()
            if line in names_dict:
                names_dict[line] +=1
            else:
                names_dict[line] = 1
    return names_dict



def print_dict(adict:dict) ->None:
    """function prints dictionary pairs."""
    for key, value in adict.items():
        print(key,":",value)

if __name__=='__main__':
    print_dict(read_from_file("nameslist.txt"))