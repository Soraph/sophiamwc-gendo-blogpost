#!/usr/bin/env python
import requests


def main():
    r = requests.post('http://127.0.0.1:5000/', {
            'title': 'Post from client',
            'content': 'Lorem ipsum'
        })


if __name__ == '__main__':
    main()
