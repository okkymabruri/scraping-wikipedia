#!/usr/bin/env python
# coding: utf-8

import codecs
import html
import pickle
import re

import bs4
import requests
from nltk import sent_tokenize

def get_article(link):
    # link = webbrowser
    article_text = requests.get(str(link), "utf8")
    if article_text is not None:
        html = bs4.BeautifulSoup(
            article_text.text,
            "lxml",
        )
        title = html.select("#firstHeading")[0].text
        paragraphs = html.select("p")
        for para in paragraphs:
            article = '\n'.join([para.text for para in paragraphs])
            # removing the footnote
            article = (re.sub('\[\d+\]', '', article.strip()))
        return article

article = get_article("https://en.wikipedia.org/wiki/Indonesia")

f = open("article.txt", "a")
f.write(article)
f.close()

