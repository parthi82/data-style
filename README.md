## Data-Style

[![Build Status](https://travis-ci.org/sourcepirate/data-style.svg?branch=master)](https://travis-ci.org/sourcepirate/data-style)

a structured scrapper writen on top of beautifulsoup and asyncio. Also provides javascript support(optional) through
phantomjs and selenium.

Phantomjs dependency can be left optional if you don't need javascript support.

## installation

[installing phantomjs](http://phantomjs.org)


## Usage

```python

import asyncio
from data import data

class MovieDetails(data.Item):

    movie_name = data.TextField(selector=".hidden-xs h1")
    movie_year = data.TextField(selector=".hidden-xs h2")

class YifyMovie(data.Item):
    details = data.SubPageFields(MovieDetails, link_selector=".browse-movie-wrap a.browse-movie-link")
    pixel = data.TextField(selector=".browse-movie-tags a")

    class Meta:
        base_url = "https://yts.ag/"

async def mymovie():
    results = await YifyMovie.one("/")
    print(results.pixel)
    details = await results.details
    for detail in details:
        print(detail.movie_name, detail.movie_year)

loop = asyncio.get_event_loop()
loop.run_until_complete(mymovie())


```

## Develop

```
  python setup.py develop
  python setup.py test
```

## License
MIT
