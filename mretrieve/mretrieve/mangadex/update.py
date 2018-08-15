from MRetrieve import MRetrieve


def new_chapters(id_, chapters):
    chapters_ = MRetrieve.get_chapters(id_, 'mangadex')['data']
    for chapter in chapters:
        if chapter in chapters_:
            chapters_.remove(chapter)
    return len(chapters_) > 0, chapters_


def new_pages(id_, chapter, pages):
    pages_ = MRetrieve.get_pages(id_, chapter)['data']
    for page in pages:
        if page in pages_:
            pages_.remove(page)
    return len(pages_) > 0, pages_
