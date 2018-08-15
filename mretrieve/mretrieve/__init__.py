from mretrieve.mangadex import query as mangadex
from mretrieve.indexer import Indexer


class MRetrieve:
    def __init__(self, idxr=None):
        if idxr is not None:
            self.indexer = idxr
        elif idxr == Indexer.NONE:
            self.indexer = Indexer.MANGADEX
        else:
            self.indexer = Indexer.MANGADEX
        return

    def gettitle(self, title):
        if self.indexer == Indexer.MANGADEX:
            return {
                'status': 'success',
                'message': 'Manga Title Retrieved',
                'data': mangadex.get_manga_info(title)
            }
        elif self.indexer == Indexer.NONE:
            return {
                'status': 'error',
                'message': 'No Indexer Specified',
                'data': None
            }
        else:
            return {
                'status': 'error',
                'message': 'No Such Indexer',
                'data': None
            }

    def get_chapters(title, indexer=None):
        if indexer == "mangadex":
            chapters = mangadex_query.get_chapters(title)
            if chapters is not None:
                return {
                    'status': 'success',
                    'message': 'Manga Chapters Retrieved',
                    'data': chapters
                }
            return {
                'status': 'error',
                'message': 'Error Retrieving Chapters',
                'data': None
            }
        elif indexer is None:
            return {
                'status': 'error',
                'message': 'No Indexer Specified',
                'data': None
            }
        else:
            return {
                'status': 'error',
                'message': 'No Such Indexer',
                'data': None
            }

    def get_pages(title, chapter, indexer=None):
        if indexer == "mangadex":
            pages = mangadex_query.get_pages(title, chapter)
            if pages is not None:
                return {
                    'status': 'success',
                    'message': 'Chapter Pages Retrieved',
                    'data': pages
                }
            return {
                'status': 'error',
                'message': 'Error Retrieving Pages',
                'data': None
            }
        elif indexer is None:
            return {
                'status': 'error',
                'message': 'No Indexer Specified',
                'data': None
            }
        else:
            return {
                'status': 'error',
                'message': 'No Such Indexer',
                'data': None
            }

    def get_hot(indexer=None):
        if indexer == "mangadex":
            hot = mangadex_search.get_hot()
            if hot is not None:
                return {
                    'status': 'success',
                    'message': 'Hot Manga Retrieved',
                    'data': hot
                }
            return {
                'status': 'error',
                'message': 'Error Retrieving Hot Manga',
                'data': None
            }
        elif indexer is None:
            return {
                'status': 'error',
                'message': 'No Indexer Specified',
                'data': None
            }
        else:
            return {
                'status': 'error',
                'message': 'No Such Indexer',
                'data': None
            }

    def get_genres(genres, indexer=None):
        if indexer == "mangadex":
            genre_titles = mangadex_search.get_genres(genres)
            if genre_titles is not None:
                return {
                    'status': 'success',
                    'message': 'Genre Titles Retrieved',
                    'data': genre_titles
                }
            return {
                'status': 'error',
                'message': 'Error Retrieving Genre Titles',
                'data': None
            }
        elif indexer is None:
            return {
                'status': 'error',
                'message': 'No Indexer Specified',
                'data': None
            }
        else:
            return {
                'status': 'error',
                'message': 'No Such Indexer',
                'data': None
            }

    def get_search(args, indexer=None):
        if indexer == "mangadex":
            search = mangadex_search.get_search(
                {
                    'query': args['query'] if 'query' in args else None,
                    'genres': args['genres'] if 'genres' in args else None,
                    'author': args['author'] if 'author' in args else None,
                    'artist': args['artist'] if 'artist' in args else None
                })
            if search is not None:
                return {
                    'status': 'success',
                    'message': 'Search Retrieved',
                    'data': search
                }
            return {
                'status': 'error',
                'message': 'Error Retrieving Hot Manga',
                'data': None
            }
        elif indexer is None:
            return {
                'status': 'error',
                'message': 'No Indexer Specified',
                'data': None
            }
        else:
            return {
                'status': 'error',
                'message': 'No Such Indexer',
                'data': None
            }

    def new_chapters(id_, chapters, indexer=None):
        if indexer == "mangadex":
            new, chapters_ = mangadex_update.new_chapters(id_, chapters)
            if chapters_ is not None:
                return {
                    'status': ('new_chapters' if new else 'no_new_chapters'),
                    'message': 'New Chapters Retrieved',
                    'data': chapters_
                }
            return {
                'status': 'error',
                'message': 'Error Retrieving New Chapters',
                'data': None
            }
        elif indexer is None:
            return {
                'status': 'error',
                'message': 'No Indexer Specified',
                'data': None
            }
        else:
            return {
                'status': 'error',
                'message': 'No Such Indexer',
                'data': None
            }

    def new_pages(id_, chapter, pages, indexer=None):
        if indexer == "mangadex":
            new, chapters_ = mangadex_update.new_pages(id_, chapter, pages)
            if chapters_ is not None:
                return {
                    'status': ('new_pages' if new else 'no_new_pages'),
                    'message': 'New Pages Retrieved',
                    'data': chapters_
                }
            return {
                'status': 'error',
                'message': 'Error Retrieving New Pages',
                'data': None
            }
        elif indexer is None:
            return {
                'status': 'error',
                'message': 'No Indexer Specified',
                'data': None
            }
        else:
            return {
                'status': 'error',
                'message': 'No Such Indexer',
                'data': None
            }

