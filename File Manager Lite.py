
# File Manager Lite v1.0.0
# Anish Reddy


# Imports

import os
import time

# Technical Functions

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def divider():
    print('----------------------------------------')

def error(return_screen):
    input('Something went wrong... Press enter to return to try again:')
    return_screen()

def go_back(return_screen, enter):
    if enter == 'y':
        input('Press enter to return to the menu:')
        return_screen()
    elif enter == 'n':
        return_screen()



# The Home Screen

def menu_screen():

    read_this_file = ''

    clear()
    print('File Manager Lite v1.0.0')
    print('By Anish Reddy')
    divider()
    print('n - create a new text file')
    print('s - load a text file from save')
    print('i - more info')
    print('e - exit the program')
    divider()

    activity = input('Choose the letter corresponding by the activity you would like to perform, then press enter: ')
    
    # New Text File
    if activity == 'n':
        
        new_file()
    
    # Load Text File from Save
    elif activity == 's':
        
        clear()
        choose_text_file()

    # Information
    elif activity == 'i':
        
        clear()
        print('Information')
        divider()
        print('Made by Anish Reddy')
        print('Is a python file that can create/edit/copy (.txt) files that are in the same directory as this python file')
        print('In case you are stuck in a loop, use "Ctrl+C" to force quit')
        divider()
        go_back(menu_screen, 'y')
    
    # Exit
    elif activity == 'e':
        
        divider()
        exit_y_n = input('Are you sure you want to exit? (y/n): ')

        if exit_y_n == 'y':
            exit('Goodbye')
        elif exit_y_n == 'n':
            menu_screen()
        else:
            error(menu_screen)
    
    # Input Error
    else:
        divider()
        error(menu_screen)




# Choosing a Text File in the same directory as the python file.

def choose_text_file():
    
    clear()
    print('List Text Files')
    divider()

    global read_this_file
    read_this_file = ''
    
    file_number = 0
    file_list = []
    file_number_list = []

    for file in os.listdir():
        
        if file.endswith(".txt"):

            file_number = file_number + 1

            print(str(file_number) + ' - ' + file)

            file_list.append(file)

            file_number_list.append(file_number-1)

    if file_number == 0:
        print('No possible text files found...')
        go_back(menu_screen, 'y')

    else:
        print('\ne - exit to the menu')
        divider()
        chosen_file_number_as_string = input('Enter the number of the file you want to choose: ')

        try:
            chosen_file_number = int(chosen_file_number_as_string)-1
            integer = 'true'
        except:
            integer = 'false'
        
        if integer == 'true':
            if chosen_file_number in file_number_list:
                chosen_file = file_list[chosen_file_number]
                file_edit_options(chosen_file)
            else:
                error(choose_text_file)
        
        elif integer == 'false':
            if chosen_file_number_as_string == 'e':
                go_back(menu_screen, 'n')
            else:
                error(choose_text_file)
        
        else:
            exit('Something went horrifically wrong')



# Do something with the file

def file_edit_options(chosen_file):
    
    clear()
    print('Chosen file: ' + chosen_file)
    divider()
    print('r - read file contents')
    print('w - overwrite the contents of this file')
    print('a - add to the contents of the file')
    print('c - make a copy of the file')
    print('b - go back to file picker')
    print('e - exit to the menu')
    divider()
    edit_action = input('What would you like to do with "' + chosen_file + '": ')

    if edit_action == 'r':
        read_file(chosen_file)
    
    elif edit_action == 'w':
        overwrite_files(chosen_file)
    
    elif edit_action == 'a':
        add_to_file(chosen_file)
    
    elif edit_action == 'c':
        make_file_copy(chosen_file)
    
    elif edit_action == 'b':
        go_back(choose_text_file, 'n')

    elif edit_action == 'e':
        go_back(menu_screen, 'n')
    
    else:
        input('Something went wrong... Press enter to return to try again:')
        file_edit_options(chosen_file)



# Read the file
def read_file(chosen_file):
    
    clear()
    print(chosen_file)
    divider()
    with open(chosen_file, 'r') as f:
        print(f.read())
    divider()
    input('Press enter to go back:')
    file_edit_options(chosen_file)



# Overwrite the contents of the file
def overwrite_files(chosen_file):

    new_contents = ''

    clear()
    print(chosen_file + ': Original Contents')
    divider()
    
    with open(chosen_file, 'r') as f:
        print(f.read())
    
    print('\n\nType the contents you would like to overwrite the original contents with (you cannot add multiple lines):')
    divider()
    new_contents = input()

    divider()
    yes_no = input('Are you sure you want to overwrite the contents? Type "yes" to confirm: ')
    
    if yes_no == 'yes':
        with open(chosen_file, 'w') as f:
            f.write(new_contents)
        read_file(chosen_file)
    
    else:
        file_edit_options(chosen_file)



# Append to the contents to file
def add_to_file(chosen_file):

    append_contents = ''

    clear()
    print(chosen_file + ': Add contents to the end of the file')
    divider()
    
    with open(chosen_file, 'r') as f:
        print(f.read())
    
    append_contents = input()
    divider()
    yes_no = input('Are you sure you want to add to the file? Type "yes" to confirm: ')
   
    if yes_no == 'yes':
        with open(chosen_file, 'a') as f:
            f.write('\n')
            f.write(append_contents)
        read_file(chosen_file)
    
    else:
        file_edit_options(chosen_file)



# Make a copy of the file
def make_file_copy(chosen_file):

    clear()
    print(chosen_file)
    divider()
   
    with open(chosen_file, 'r') as f:
        copied_contents = f.read()
        print(copied_contents)
        
    divider()
    copy_name = input('What would you like to name the copy (don\'t include .txt): ') + '.txt'
    
    try:
        with open(copy_name, 'x') as f:
            #with open(copy_name, 'w') as f:
            f.write(copied_contents)
        works = 'true'
    
    except:
        works = 'false'
    
    if works == 'true':
        read_file(copy_name)
    elif works == 'false':
        input('A problem has occured. Check to see if you have a text file with the same name already. Press enter to continue:')
        file_edit_options(chosen_file)
    else:
        exit('Something went very wrong...')



#Create a new file
def new_file():

    clear()
    new_file_name = input('What would you like to name the copy (don\'t include .txt): ') + '.txt'
    
    try:
        with open(new_file_name, 'x') as f:
            pass
        works = 'true'
    except:
        works = 'false'
    
    if works == 'true':
        clear()
        print(new_file_name + ': Type out the contents of the file')
        divider()
        new_file_contents = input()
        
        with open(new_file_name, 'w') as f:
            f.write(new_file_contents)
        read_file(new_file_name)

    elif works == 'false':
        input('A problem has occured. Check to see if you have a text file with the same name already. Press enter to continue:')
        menu_screen()

    else:
        exit('You broke this code')




try:
    menu_screen()
except:
    exit('you somehow broke this program')