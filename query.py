from movies import Movies

class Menu:
    def __init__(self, moviesfile):
        self.movies = Movies(moviesfile)

    def display(self):
        print("Menu:")
        print("1. List all the movie names")
        print("q. Quit")

    def run(self):
        while True:
            self.display()
            option = input("Enter your choice: ")
            if option == 'q':
                print("Exiting program...")
                break
            elif option == '1':
                self.list_all_movie_names()
            else:
                print("Invalid option. Please try again.")

    def list_all_movie_names(self):
        print("All movie names:")
        for i, movie in enumerate(self.movies.get_all_movies(), 1):
            print(f"{i}. {movie['name']}")

if __name__ == "__main__":
    menu = Menu('./movies.txt')
    menu.run()