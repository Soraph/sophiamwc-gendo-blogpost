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
        title = request.form['title']
        content = request.form['content']

        sql_insert = '''
            INSERT INTO posts(title, content)
            VALUES(?, ?)
        '''
        try:
            c.execute(sql_insert, [title, content])
        except sqlite3.Error:
            db.rollback()
            raise
        else:
            db.commit()

        return '', 201
    else:
        sql_all_posts = '''
            SELECT
                id, title, content, date
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
