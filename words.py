#!/usr/bin/env python3

'''Retrivate and print words from a URL.

Usage:
    python3 words.ph <URL>
'''
import sys
from urllib.request import urlopen

def fetch_words(url):
    '''Fetch a list of  words from URL.

    Args:
        url: The URL of UTF-8 text documnet.

    Returns:
        A list of strings containing the words from the document
    '''
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_item(items):
    '''Prints items one per line.

    Args:
        items: An iterable series of printable items.
    '''
    for item in items:
        print(item)


def main(url):
    '''Prints each word  from a text documnet from a URL

    Args:
        url: The URL of UTF-8 text documnet.
    '''
    words = fetch_words(url)
    print_item(words)


if __name__ == '__main__':
    main(sys.argv[1]) # For example you can use this 'http://sixty-north.com/c/t.txt' url
