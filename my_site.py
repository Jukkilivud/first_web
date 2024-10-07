# -*- coding: 1251 -*-
from psycopg2 import connect, Error
import psycopg2
import html
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/viewlog', methods=['GET', 'POST'])
def view_log() -> 'html':
    """Display the contents of the log file as a HTML table."""
    return render_template('viewlog.html')


try:
    connection = psycopg2.connect(host='127.0.0.1',
                                  port='5432',
                                  user='Jukki',
                                  password='carib637',
                                  database='forever_glasses',
                                  )

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM view_users")
    # cursor.execute(
    #     "INSERT INTO view_users(id, browser, name, date_visit) VALUES(%s, %s, %s, %s)"
    # )
    rows = cursor.fetchall()
    print('\n', "Connection database 'forever_glasses' successfully ('Успешное подключение!'):", '\n')
    for row in rows:
        print(row, '\n')

except (Exception, Error) as error:
    print("Error server PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("Connection PostgreSQL closed.")


@app.route('/')
@app.route('/entry', methods=['GET', 'POST'])
def entry_page() -> 'html':
    return render_template('entry.html')


@app.route('/gallery', methods=['GET', 'POST'])
def work_gallery() -> 'html':
    return render_template('gallery.html')


@app.route('/gallery#2', methods=['GET', 'POST'])
def work_gallery_2() -> 'html':
    return render_template('gallery_2.html')


@app.route('/gallery#3', methods=['GET', 'POST'])
def work_gallery_3() -> 'html':
    return render_template('gallery_3.html')


@app.route('/gallery#4', methods=['GET', 'POST'])
def work_gallery_4() -> 'html':
    return render_template('gallery_4.html')


@app.route('/gallery#5', methods=['GET', 'POST'])
def work_gallery_5() -> 'html':
    return render_template('gallery_5.html')


app.secret_key = "&jRdu%/dPPP#cLA#**bW%tt"

if __name__ == '__main__':
    app.run(debug=True)
