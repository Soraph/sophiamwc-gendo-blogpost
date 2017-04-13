#!/usr/bin/env python
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)
db = sqlite3.connect('blog.db', check_same_thread=False)
db.row_factory = sqlite3.Row
c = db.cursor()


@app.route('/', endpoint='homepage', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        pass
    else:
        sql_all_posts = '''
            SELECT
                id, title, content
            FROM
                posts
            ORDER BY
                id DESC
        '''
        c.execute(sql_all_posts)

        page_data = {
                'page_title': 'Homepage',
                'posts': c.fetchall()
        }

        return render_template('base--homepage.html', **page_data)


if __name__ == '__main__':
    app.run(debug=True)
