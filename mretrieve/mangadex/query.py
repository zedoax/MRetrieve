from mretrieve import Parser, Retriever
from mretrieve.mangadex import MANGADEX_URI, Log


def get_manga_info(title):
    try:
        result = Retriever.get(MANGADEX_URI + "/manga/" + title)
        result = Parser.fromstring(result.content)
        title = result.xpath('//h3[@class="panel-title"]/text()')[0]
        image = result.xpath('//img[@title="Manga image"]/@src')[0]
        author = result.xpath('//a[@title="Other manga by this author"]/text()')[0]

        return {
            'title': title,
            'image': image
        }
    except Retriever.HTTPError as e:
        Log.error(e.strerror)
    Log.error("Unknown Error Occurred")
