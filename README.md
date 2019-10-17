# imdb-crawler
imdb.com movies crawler in scrapy and python

Get Movies basic information from imdb.com


returned fields contains :
* url
* name
* image
* genre
* contentRating
* actor
* creator
* description
* datePublished
* keywords
* aggregateRating
* review
* trailer
* duration



## how to use:

```
git clone https://github.com/doroudi/imdb-crawler
```

install scrapy using 

```
pip install scrapy
```

or [install using Anaconda](https://anaconda.org/conda-forge/scrapy)


run spider

```
scrapy crawl topMovies -o output.json
```

