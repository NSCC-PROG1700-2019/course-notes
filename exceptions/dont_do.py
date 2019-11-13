
def main():
    try:
        user = input("Enter a number: ")
        print(f"You entered: {int(user)}")
    #except:
    except Exception as e:
        print("You have an error! {e}")


if __name__ == '__main__':
    main()