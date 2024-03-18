from movies import Movies

def display_menu():
    print("Menu:")
    print("q. Quit")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == 'q':
            print("Exiting program...")
            break
        else:
            print("Invalid option. Please try again.\n")


if __name__ == "__main__":
    main()

movies = Movies('./movies.txt')
