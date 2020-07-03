# Sinhala-Lyrics-Search-Engine
This repository contains the Sinhala song lyrics corpus, the web crawler and the search engine built using ElasticSearch. 

## Getting Started:
To start the search engine, run an elasticsearch instance on port 9200.

## Directory Structure
- lyrics crawler: source code for the data scraper
- original data: original data files in unicode format
- processed data: data translated to Sinhala
- queries: ElasticSearch queries

## Structure of the data
The corpus was scraped from https://sinhalasongbook.com/. It contains 1094 unique Sinhala songs. Each song has 8 matadata fields as follows.

1. title - Sinhala
2. artist - Sinhala
3. lyricist - Sinhala
4. musicComposer - Sinhala
5. genre  - Sinhala
6. views - Number
7. shares - Number
8. lyrics  - Sinhala

Metadata fields in English were translated to Sinhala using [mtranslate](https://github.com/mouuff/mtranslate) python library.

## Main functions of the system
- Search a song by any field
- Faceted search
- Range queries
- Support for synonyms
