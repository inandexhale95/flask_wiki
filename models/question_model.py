import pymysql.cursors
from database.conn_mysql import mysql_conn


class Question:
    def __init__(self, q_id, u_id, subject, content, create_date):
        self.q_id = q_id
        self.u_id = u_id
        self.subject = subject
        self.content = content
        self.create_date = create_date

    def __str__(self):
        return self.subject

    @staticmethod
    def get_question_count():
        db_cursor = mysql_conn().cursor()
        sql = "SELECT COUNT(*) FROM question"
        db_cursor.execute(sql)
        result = db_cursor.fetchone()
        return result[0]

    @staticmethod
    def get_question_list(per_page, page):
        # OFFSET이 0부터 시작돼 -1을 해줌
        page -= 1
        db_cursor = mysql_conn().cursor(pymysql.cursors.DictCursor)
        sql = "SELECT * FROM question ORDER BY create_date DESC LIMIT %s OFFSET %s" % (per_page, page*per_page)
        db_cursor.execute(sql)
        question_list = db_cursor.fetchall()

        if not question_list:
            return None

        return question_list

    @staticmethod
    def get_question(q_id):
        db_cursor = mysql_conn().cursor(pymysql.cursors.DictCursor)
        sql = "SELECT * FROM question WHERE q_id = %d" % q_id
        db_cursor.execute(sql)
        question = db_cursor.fetchone()

        if not question:
            return None
        return question

    @staticmethod
    def insert(subject, content, u_id) -> bool:
        db_cursor = mysql_conn().cursor()
        sql = "INSERT INTO question(subject, content, u_id) VALUES('%s', '%s', '%s')" % (subject, content, u_id)
        result: int = db_cursor.execute(sql)
        mysql_conn().commit()
        return bool(result)
