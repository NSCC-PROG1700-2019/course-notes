
def open_logfile():
    try:
        return open('log.txt', 'w')
    except PermissionError as p:
        print(f"Unable to log errors. {p}")

def close_logfile(fp):
    fp.close()

def write_logfile(fp, line):
    try:
        fp.write(line)
        fp.write('\n')
    except AttributeError as e:
        print(f"Could not write to log file. {e}")

def main():
    fp = open_logfile()
    try:
        user = input("Enter a number: ")
        print(f"You entered: {int(user)}")
    except ValueError as e:
        write_logfile(fp, str(e))
    else:
        close_logfile(fp)
    finally:
        print("finally called!")

if __name__ == '__main__':
    main()