import sys
import clipboard
import json

if len(sys.argv) == 2:
    command = sys.argv[1]
    
    if command == 'save':
        pass
    elif command == 'load':
        pass
    elif command == 'list':
        pass
    else:
        print('Unknown command')
else:
    print('Please pass exactly one command')


# paste the data from the clipboard to the data variable
clipboard.paste()
