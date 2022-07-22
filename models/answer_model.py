from database.conn_mysql import mysql_conn
from datetime import datetime


class Answer:
    def __init__(self, a_id, q_id, content, create_date):
        self.a_id = a_id
        self.q_id = q_id
        self.content = content
        self.create_date = create_date

    def __str__(self):
        return self.content

    @staticmethod
    def get_answer_list(q_id):
        db_cursor = mysql_conn().cursor()
        sql = "SELECT a_id, content, create_date FROM answer WHERE q_id IN(SELECT q_id FROM question WHERE q_id = %s)"
        db_cursor.execute(sql, q_id)
        answer_list = db_cursor.fetchall()

        if not answer_list:
            return None

        return answer_list

    @staticmethod
    def create(q_id, content):
        db_cursor = mysql_conn().cursor()
        sql = "INSERT INTO answer(q_id, content, create_date) VALUES(%s, %s, %s)"
        result = db_cursor.execute(sql, (q_id, content, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        mysql_conn().commit()
        return bool(result)

