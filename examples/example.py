import sys, os
import asyncio
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data import data
from tests.base import async_test

sem = asyncio.Semaphore(5)

class StallMan(data.Item):

    urgent_items = data.TextField(repeated=True, selector=".column1 li")

    class Meta:
        base_url= "https://stallman.org/"

@async_test
async def hello():
    results = await StallMan.all("/")
    print(results[0].urgent_items)

hello()


class MovieDetails(data.Item):

    movie_name = data.TextField(selector=".hidden-xs h1")
    movie_year = data.TextField(selector=".hidden-xs h2")

class YifyMovie(data.Item):
    details = data.SubPageFields(MovieDetails, link_selector=".browse-movie-wrap a.browse-movie-link")
    pixel = data.TextField(selector=".browse-movie-tags a")

    class Meta:
        base_url = "https://yts.ag/"

@async_test
async def mymovie():
    results = await YifyMovie.one("/")
    print(results.pixel)
    details = await results.details
    for detail in details:
        print(detail.movie_name, detail.movie_year)

mymovie()