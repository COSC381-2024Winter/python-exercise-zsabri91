from movies import Movies

class Menu:
    def __init__(self, moviesfile):
        self.movies = Movies(moviesfile)

    def display(self):
        print("Menu:")
        print("1. List all the movie names")
        print("2. Search movies by names")
        print("3. Search movies by cast")
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
            elif option == '2':
                self.search_movies_by_names()
            elif option == '3':
                self.search_movies_by_cast()
            else:
                print("Invalid option. Please try again.")

    def list_all_movie_names(self):
        print("All movie names:")
        for i, movie in enumerate(self.movies.get_all_movies(), 1):
            print(f"{i}. {movie['name']}")

    def search_movies_by_names(self):
        keyword = input("Enter a keyword to search for movies: ")
        results = self.movies.search_movies_by_name(keyword)

        if results:
            print("Movies found:")
            for movie in results:
                print(movie['name'])
        else:
            print("No movies found with that keyword.")

    def search_movies_by_cast(self):
        keyword = input("Enter a keyword to search for cast members: ")
        results = self.movies.search_movies_by_cast(keyword)

        if results:
            print("Movies found:")
            for result in results:
                movie_name = result['name']
                cast_list = result['cast']
                print(f"{movie_name}\n[{', '.join([actor for actor in cast_list if keyword.lower() in actor.lower()])}]")
        else:
            print("No movies found with that cast member.")

if __name__ == "__main__":
    menu = Menu('./movies.txt')
    menu.run()
