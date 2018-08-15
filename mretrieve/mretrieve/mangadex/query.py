from MRetrieve import Retriever
from MRetrieve.mangadex import MANGADEX_URI, Log
from datetime import datetime
from bs4 import BeautifulSoup
import re


def get_manga_info(title):
    try:
        result = Retriever.get(MANGADEX_URI + "/manga/" + title)
        parse = BeautifulSoup(result.content, "lxml")

        title = parse.find('h3', class_='panel-title').text
        image = MANGADEX_URI + parse.find('img', title='Manga image')['src']
        author = parse.find('a', title='Other manga by this author').text
        artist = parse.find('a', title='Other manga by this artist').text
        genres = get_genres_from_tree(parse.find_all('a', class_='genre'))
        rating = float(''.join(char for char in parse.find('th', text='Rating:').parent.text.
                               split(" ")[1] if char.isdigit() or char == '.'))
        status = parse.find('th', text='Pub. status:').next_sibling.next_sibling.text
        description = parse.find('th', text='Description:').next_sibling.next_sibling.text

        return {
            'title': title,
            'image': image,
            'author': author,
            'artist': artist,
            'genres': genres,
            'rating': rating,
            'status': status,
            'description': description
        }
    except Retriever.HTTPError as e:
        Log.error(e.strerror)
    except:
        Log.error("Unknown Error Occurred")
    return None


def get_genres_from_tree(tree):
    genres = []
    for g in tree:
        genres.append(g.text)
    return genres


def get_chapters(title):
    try:
        result = Retriever.get(MANGADEX_URI + "/manga/" + str(title))
        parse = BeautifulSoup(result.content, "lxml")

        chapters = []
        for chapter in parse.find_all('a', attrs={'data-chapter-num': True}):
            language = chapter.parent.parent.find('img', attrs={'src': re.compile('flags')})['title']
            date = chapter.parent.parent.find('time')['datetime']
            date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S UTC")
            chapters.append({
                'chapter': chapter['data-chapter-num'],
                'title': chapter['data-chapter-name'],
                'id': chapter['data-chapter-id'],
                'language': language,
                'date': date
            })
        return chapters
    except:
        Log.error("Unknown Error Occurred")
    return None


def get_pages(title_id, page):
    try:
        result = Retriever.get(MANGADEX_URI + "/chapter/" + title_id + "/" + page)
        parse = BeautifulSoup(result.content, "lxml")

        pages = parse.find_all('option', text=re.compile("Page "), attrs={'value': True})
        pagenums = []
        for page in pages:
            pagenums.append(int(page['value']))

        pageurls = []
        for i in pagenums:
            result = Retriever.get(MANGADEX_URI + "/chapter/" + title_id + "/" + str(i))
            parse = BeautifulSoup(result.content, "lxml")
            pageurls.append(parse.find('img', attrs={'id': 'current_page'})['src'])

        pages = []
        for i, p in zip(pagenums, pageurls):
            pages.append({
                'number': i,
                'url': p
            })

        return pages
    except:
        Log.error("Unknown Error Occurred")
    return None
