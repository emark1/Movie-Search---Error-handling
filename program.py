import requests
import requests.exceptions
import collections
import movieservice

def main():
    print_header()
    search_event_loop()


def print_header():
    print('-------------')
    print('MOVIE SEARCH')
    print('-------------')

def search_event_loop():
    search = 'ONCE_THROUGH_LOOP'

    while search != 'x':
        try:
            search = input("Search for a movie (enter X to exit): ")
            if search != 'x':
                results = movieservice.find_movies(search)
                print("Found {} results.".format(len(results)))
                for r in results:
                    print('{} -- {}'.format(r.year, r.title))
                print()
        except ValueError:
            print("Text is required for search.")
        except requests.exceptions.ConnectionError as cerror:
            print("Error your network is down: {}".format(cerror))
        

    print("Program ended.")



# movies = []
# for md in movies_list:
#     m = MovieResult(**md)
#     movies.append(m)
# for md in movies_list:
#     m = MovieResult(
#         imdb_code=md.get('imdb_code'),
#         title=md.get('title'),
#         duration=md.get('duration'),
#         director=md.get('director'),
#         year=md.get('year', 0.0),
#         rating=md.get('rating', 0.0),
#         imdb_score=md.get('imdb_score', 0.0),
#         keywords=md.get('keywords'),
#         genres=md.get('genres')
#     )
#     movies.append(m)


if __name__ == '__main__':
    main()