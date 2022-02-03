#-------------------------- READING FILES
# readline, for line in file, read, readlines approaches

def readline_file():
    ''' readline approach -> when you want to process only part of a file
    '''

    flanders_file = open('w6_read_file_In_Flanders_Fields.txt', 'r')
    flanders_poem = ''

    line = flanders_file.readline()
    while line != "":
        flanders_poem = flanders_poem + line
        line = flanders_file.readline()

    print(flanders_poem)
    flanders_file.close()
    
def forlinein_file():
    ''' for line in file approach -> when you want to process every line
    in the file one at a line.
    '''
    flanders_file = open('w6_read_file_In_Flanders_Fields.txt', 'r')
    flanders_poem = ''

    for line in flanders_file:
        flanders_poem = flanders_poem + line
    
    print(flanders_poem)
    flanders_file.close()
    
def read_file():
    ''' read approach -> when you want to read the whole file at once and
    use it as a single string.
    '''
    flanders_file = open('w6_read_file_In_Flanders_Fields.txt', 'r')
    flanders_poem = flanders_file.read()

    print(flanders_poem)
    flanders_file.close()

def readlines_file():
    ''' readlines approach -> when you want to examine each line of a
    file by index.
    '''
    flanders_file = open('w6_read_file_In_Flanders_Fields.txt', 'r')
    flanders_poem = ''
    
    flanders_list = flanders_file.readlines()
    for line in flanders_list:
        flanders_poem = flanders_poem + line

    print(flanders_poem)
    flanders_file.close()


#-------------------------- WRITING FILES

def write_files():
    import tkinter.filedialog

    #call function open to open that file
    from_filename = tkinter.filedialog.askopenfilename()
    from_file = open(from_filename, 'r')
    contents = from_file.read()
    from_file.close()

    #call function to select a file to save to
    to_filename = tkinter.filedialog.asksaveasfilename()
    to_file = open(to_filename, 'w')
    to_file.write('Copy\n') # add the newline
    to_file.write(contents) # write the contents of the file
    to_file.close()

