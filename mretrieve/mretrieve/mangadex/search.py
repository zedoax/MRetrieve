from bs4 import BeautifulSoup
from MRetrieve import Retriever
from mretrieve.mangadex import Log, MANGADEX_URI
from mretrieve.mangadex.objects.genre import Genre

MANGADEX_SEARCH_URI = "/?page=search"
MANGADEX_AUTHOR_URI = "&author="
MANGADEX_ARTIST_URI = "&artist="
MANGADEX_GENRES_URI = "&genres="
MANGADEX_TITLE_URI = "&title="


def get_hot():
    try:
        result = Retriever.get(MANGADEX_URI + "/featured")
        parse = BeautifulSoup(result.content, "lxml")

        titles_ = parse.find_all('a', class_='manga_title')
        titles = []
        for title in titles_:
            title_id = ''.join(c for c in title['href'] if c.isdigit())
            title_id = title_id[:5]
            titles.append({
                'title': title['title'],
                'id': title_id
            })
        return titles
    except:
        Log.error("Unknown Error Occurred")
    return None


def get_genres(genres):
    return get_search({
        'genres': genres
    })


def get_search(args=None):
    try:
        # Build Search URI
        url = MANGADEX_URI + MANGADEX_SEARCH_URI
        if args['query']:
            url += MANGADEX_TITLE_URI + args['query']
        if args['genres']:
            url += MANGADEX_GENRES_URI + build_genre_list(args['genres'])
        if args['author']:
            url += MANGADEX_AUTHOR_URI + args['author']
        if args['artist']:
            url += MANGADEX_ARTIST_URI + args['artist']

        # Retrieve and parse search
        result = Retriever.get(url)
        parse = BeautifulSoup(result.content, 'lxml')
        titles = []
        for title in parse.find_all('a', class_='manga_title'):
            title_id = ''.join(c for c in title['href'] if c.isdigit())
            title_id = title_id[:5]
            titles.append({
                'title': title.text,
                'id': title_id
            })
        return titles
    except:
        Log.error("Unknown Error Occurred")
    return None


def build_genre_list(genres):
    # Create a list of genres that mangadex can interpret
    genres_ = []
    for genre in genres:
        genres_.append(Genre[str(genre).upper()].value)

    # Create the search url
    lst = ''
    for genre in genres_:
        lst += str(genre) + ','
    lst = lst[:len(lst) - 1]
    return lst
