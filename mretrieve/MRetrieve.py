from mretrieve.mangadex import query as mangadex


def get_title(title, indexer=None):
    if indexer == "mangadex":
        return {
            'status': 'success',
            'message': 'Manga Title Retrieved',
            'data': mangadex.get_manga_info(title)
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
