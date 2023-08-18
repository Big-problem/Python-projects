# Learn the json module
import sys
import clipboard
import json

FILE_PATH = 'clipboard.json'

def save_data(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4) # save the data inside the f

def load_data(file_path):
    try: # in case the file doesn't exist
        with open(file_path, 'r') as f:
            data = json.load(f) # read dict from f
            return data
    except:
        return {}

if __name__ == '__main__':
    if len(sys.argv) == 2:
        command = sys.argv[1]
        data = load_data(FILE_PATH)
        
        if command == 'save': # save the data into the clipboard
            key = input('Enter a key: ')

            # paste the data from the clipboard to the variable
            data[key] = clipboard.paste()
            save_data(FILE_PATH, data)
            print('Data saved!')
        elif command == 'load': # load data from the clipboard
            key = input('Enter a key: ')

            if key in data:
                clipboard.copy(data[key]) # copy data to the clipboard
                print('Data copied to clipboard!')
            else:
                print('Key does not exist.')
        elif command == 'delete': # load data from the clipboard
            key = input('Enter a key: ')

            if key in data:
                data.pop(key) # copy data to the clipboard
                save_data(FILE_PATH, data)
                print('Data deleted!')
            else:
                print('Key does not exist.')
        elif command == 'list': # show what's in the json file
            print(data)
        else:
            print('Unknown command')
    else:
        print('Please pass exactly one command')