# -*- coding: 1251 -*-
# from getpass import getpass
from mysql.connector import connect, Error
# import mysql
import mysql.connector
import html
from flask import Flask, render_template, request
from DB_try import UseDatabase, ConnectionError, CredentialsError, SQLError


app = Flask(__name__)

app.config['db_config'] = {'host': '127.0.0.1',
                           'port': '3306',
                           'user': 'Jukki',
                           'password': 'carib637',
                           'database': 'forever_glasses'}


# def create_connection(user_host, user_port, user_name, passwd, db_name):
#     cursor = connection.cursor()
#     connection = create_connection(
#         "127.0.0.1", "3306", "Jukki", "carib637", "forever_glasses")
#     try:
#         cursor.execute()
#         connection = mysql.connector.connect(host=user_host,
#                                              port=user_port,
#                                              user=user_name,
#                                              password=passwd,
#                                              database=db_name,
#                                              )
#         print("Сongratulations_connection_'forever_glasses'")

#     except Error as e:
#         print(f"The error '{e}' occurred")


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


@app.route('/viewlog', methods=['GET', 'POST'])
def view_log() -> 'html':
    """Display the contents of the log file as a HTML table."""
    try:
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """select id, ip, datetime, browser_string from log"""
            cursor.execute(_SQL)
            contents = cursor.fetchall()
        titles = ('id', 'ip', 'datetime', 'browser_string')
        return render_template('viewlog.html',
                               the_title='View Log',
                               the_row_titles=titles,
                               the_data=contents,
                               )

    except ConnectionError as err:
        print('Is your database switched on? Error:', str(err))
    except CredentialsError as err:
        print('User-id/Password issues. Error:', str(err))
    except SQLError as err:
        print('Is your query correct? Error:', str(err))
    except Exception as err:
        print('Something went wrong:', str(err))
    return 'Error'


app.secret_key = "&jRdu%/dPPP#cLA#**bW%tt"

if __name__ == '__main__':
    app.run(debug=True)
