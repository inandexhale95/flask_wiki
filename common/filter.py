import pymysql.cursors
from database.conn_mysql import mysql_conn
from datetime import datetime
from models import question_model


def format_datetime(value: datetime, fmt="%Y년 %m월 %d일 %p %I:%M"):
    return value.strftime(fmt)


def answer_count(q_id):
    db_cursor = mysql_conn().cursor()
    sql = "SELECT COUNT(*) FROM answer WHERE q_id = (SELECT q_id FROM question WHERE q_id = %s)" % q_id
    db_cursor.execute(sql)
    result = db_cursor.fetchone()
    return result[0]


def get_question_writer(u_id):
    db_cursor = mysql_conn().cursor(pymysql.cursors.DictCursor)
    sql = "SELECT username FROM user WHERE u_id = (SELECT DISTINCT u_id FROM question WHERE u_id = %s)" % u_id
    db_cursor.execute(sql)
    result = db_cursor.fetchone()
    print(result)
    return result['username']
