import sys
from movies.commands import movlst, movdt, movsrch, movadd, movfv, movcat

def main():
    command = sys.argv[1]
    args = sys.argv[2:]

    if command == 'movlst':
        movlst()
    elif command == 'movdt':
        movdt(*args)
    elif command == 'movsrch':
        movsrch(*args)
    elif command == 'movadd':
        movadd(*args)
    elif command == 'movfv':
        movfv(*args)
    elif command == 'movcat':
        movcat(*args)
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
