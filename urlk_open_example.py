#!/usr/bin/env python3

import sys

from urllib.request import urlopen


def save_file(value):
    try:
        f = open("url_data.txt", "a")
        f.write(value )
        f.close()
    except Exception:
        print("Could not save file")

def fetch_words(url):
    with urlopen(url) as story:
     story_words=[]
     for line in story:
        lines=line.decode('utf-8')
        save_file(lines)
        line_words=line.decode('utf-8').split()
        for words in line_words:
            story_words.append(words)
     return story_words

def print_words(story_words):
    for word in story_words:
        print(word)


def main(url):
    words=fetch_words(url)
    print_words(words)

if __name__=='__main__':
   main(sys.argv[1])

#print(story_words)

        #content=line.read()
        #print(content)
        #print(line)
        #save_file(line)




