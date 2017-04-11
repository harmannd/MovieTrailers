import fresh_tomatoes
import media


# Creates a series of movie entries
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://www.impawards.com/1995/posters/toy_story_ver1.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://www.movieposter.com/posters/archive/main/98/MPW-49246",  # NOQA
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
hobbit = media.Movie("The Hobbit: An Unexpected Journey",
                     "A small man get robbed.",
                     "http://www.comicbookbrain.com/_imagery/2013-12-19/hobbit-unexpected-journey-ring-poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=SDnYMbYB-nU")
school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "http://img.moviepostershop.com/the-school-of-rock-movie-poster-2003-1020191888.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")
ratatouille = media.Movie("Ratatouille",
                          "A rat is a chef is Paris",
                          "http://www.pixartalk.com/wp-content/uploads/2009/06/ratus1.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")
midnight_in_paris = media.Movie("Midnight in Paris",
                                "No longer daytime in Paris",
                                "https://images-na.ssl-images-amazon.com/images/I/61uuYEUFw4L._SY450_.jpg",  # NOQA
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")
hunger_games = media.Movie("Hunger Games",
                           "Children forced to kill each other for our"
                           " amusement",
                           "https://images-na.ssl-images-amazon.com/images/I/51OGv-AnD6L.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=mfmrPu43DF8")

# Send the movies to be displayed 
movies = [toy_story, avatar, hobbit, school_of_rock, ratatouille,
          midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)

