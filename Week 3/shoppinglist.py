def display_menu():
    print('\n----- The Shopping List Program -----\n')
    print('list -- Display Shopping List')
    print('add  -- Add a new item to the list')
    print('del  -- Delete an item from the list')
    print('save -- Save the list')
    print('exit -- Exit from this program')

def display_items(shopping_list):
    print('\n----- Current Shopping List -----')
    for item in shopping_list:
        print(item)

def add_item(shopping_list):
    new_item = input('\nPlease enter an item to add to the list: ')

    if new_item:
        shopping_list.append(new_item)

def delete_item(shopping_list):
    remove_item = input('\Please enter the name of the item you wish to delete: ')

    #counter = shopping_list.count('remove_item')
    #if counter >0:
        #shopping_list.remove(remove_item)

    #if remove_item in shopping_list:
        #shopping_list.remove(remove_item)
    
    try:
        shopping_list.remove(remove_item)
    except ValueError:
        print(f'{remove_item} is not in the list.')
    else:
        print(f'{remove_item} has been removed from the list.')
    
def save_list(shopping_list):
    with open('c:\\file location info.txt', 'w') as output_list:
        for item in shopping_list:
            output_list.write(f'{item}\n')

def open_list():
    new_list = []
    try:
        with open('c:\\file location info.txt', 'w') as input_list:
            while True:
                item = input_list.readline().replace('\n', '')  #To avoid adding an additional blank line
                if not item:
                    break
                    
                new_list.append(item)
            
    except:
        print('Error: Failure in opening and reading from the file.')

    return new_list
        
def get_menu_request(shopping_list):
    while True: #To loop through menu options until user selects exit.
        display_menu()
        menu_option = input('Select an Option >> ').lower()

        if menu_option == 'list': display_items(shopping_list)
        if menu_option == 'add' : add_item(shopping_list)
        if menu_option == 'del' : delete_item(shopping_list)
        if menu_option == 'save': save_list(shopping_list)
        if menu_option == 'open' : shopping_list = open_list()
        if menu_option == 'exit' : break

        print(shopping_list)





if __name__ == '__main__':
    shopping_list = []
    get_menu_request(shopping_list)

    print('\nGoodbye!')