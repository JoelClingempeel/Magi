from flask import Flask, render_template, url_for
import json
import sqlite3

app = Flask('__name__')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/spell')
def spell():
    conn = sqlite3.connect('data.db')
    spell = next(conn.execute("select * from foo;"))[1]
    conn.execute("update foo set spell = 0 where id = 1;")
    conn.commit()
    return json.dumps({'spell': spell})


if __name__ == '__main__':
    app.run(host="0.0.0.0")
