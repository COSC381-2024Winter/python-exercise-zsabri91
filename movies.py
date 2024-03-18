class Movies:
    def __init__(self, movies_file):
        self._movies = []

        with open(movies_file, encoding="utf-8") as file:
            row_idx = 0
            for line in file:
                if row_idx % 3 == 0:
                    movie_name = line.rstrip()
                if row_idx % 3 == 1:
                    movie_cast = line.rstrip().split(',')
                if row_idx % 3 == 2:
                    self._movies.append(
                        {
                            'name': movie_name,
                            'cast': movie_cast
                        }
                    )
                    movie_name = None
                    movie_cast = None
                row_idx += 1

        if movie_name and movie_cast:
            # Add the last movie to the list
            self._movies.append(
                {
                    'name': movie_name,
                    'cast': movie_cast
                }
            )

    def get_all_movies(self):
        return self._movies

    def search_movies_by_name(self, keyword):
        keyword = keyword.lower()
        found_movies = []
        for movie in self._movies:
            if keyword in movie['name'].lower():
                found_movies.append(movie)
        return found_movies

    def search_movies_by_cast(self, keyword):
        keyword = keyword.lower()
        found_movies = []
        for movie in self._movies:
            for actor in movie['cast']:
                if keyword in actor.lower():
                    found_movies.append(movie)
                    break  # Break the loop after finding the first match in the cast
        return found_movies


if __name__ == "__main__":
    movies = Movies('./movies.txt')
