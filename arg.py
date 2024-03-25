import sys

def arg_start(total_args, min_args):
    if len(sys.argv) < min_args + 1:
        print(f"Usage: {sys.argv[0]} <arguments>")
        print(f"At least {min_args} arguments required.")
        sys.exit(1)
    if len(sys.argv) > total_args + 1:
        print(f"Usage: {sys.argv[0]} <arguments>")
        print(f"Too many arguments. Expected {total_args} arguments.")
        sys.exit(1)

def arg(*args):
    for arg in args:
        if arg in sys.argv:
            return True
    return False