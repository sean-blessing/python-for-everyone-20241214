print('Welcome to the Wizard Inventory App\n')
items = ['wooden staff', 'wizard hat', 'cloth shoes']

def print_menu():
    print('COMMAND MENU')
    print('show - Show all items')
    print('grab - Grab an item')
    print('edit - Edit an item')
    print('drop - Drop an item')
    print('exit - Exit program\n')

def show_items():
    print("--- Show Items ---")
    for i, item in enumerate(items):
        print(f'{i+1}. {item}')
    print()

def grab_item():
    print("--- Grab (Add) Item ---")
    if len(items) < 4:        
        item = input('Item Name: ')
        items.append(item)
        print(f'{item} was added')
    else:
        print("You can't carry any more items. Drop something first")
    print()

def edit_item():
    print("--- Edit Item ---")
    item_nbr = int(input('Item Number: '))
    if item_nbr >= 1 and item_nbr <= len(items):
        new_name = input('Updated name: ')
        items[item_nbr-1] = new_name
        print(f'Item [{item_nbr}] was updated.')
    else:
        print('Invalid item #.')
    print()

def drop_item():
    print("--- Drop Item ---")
    item_nbr = int(input('Item Number: '))
    if item_nbr >= 1 and item_nbr <= len(items):
        drop_item = items.pop(item_nbr - 1)
        print(f'{drop_item} was dropped.')
    else:
        print('Invalid item #.')
    print()

def main():
    command = ""
    while(command != 'exit'):
        print_menu()
        command = input('Command: ')
        match command:
            case 'show':
                show_items()
            case 'grab':
                grab_item()
            case 'edit':
                edit_item()
            case 'drop':
                drop_item()
            case 'exit':
                pass
            case _:
                print('Invalid Command. Try Again.')
    print('Bye')

if __name__ == "__main__":
    main()