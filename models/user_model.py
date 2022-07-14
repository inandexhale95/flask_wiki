from database.conn_mysql import mysql_conn
from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, u_id, username, password, email, create_date):
        self.u_id = u_id
        self.username = username
        self.password = password
        self.email = email
        self.create_date = create_date

    def __str__(self):
        return self.username

    def get_id(self):
        return self.u_id

    @staticmethod
    def create_user(username, password, email):
        db_cursor = mysql_conn().cursor()
        sql = "INSERT INTO user(username, password, email) VALUES('%s', '%s', '%s')" % (username, password, email)
        db_cursor.execute(sql)
        mysql_conn().commit()

    @staticmethod
    def duplicate_user_check(username):
        db_cursor = mysql_conn().cursor()
        sql = "SELECT EXISTS(SELECT username FROM user WHERE username = %s)"
        db_cursor.execute(sql, username)
        id_check = db_cursor.fetchone()[0]
        return id_check

    @staticmethod
    def duplicate_email_check(email):
        db_cursor = mysql_conn().cursor()
        # 이메일을 넣을 때는 작은 따옴표를 사용해야한다.
        sql = "SELECT EXISTS(SELECT email FROM user WHERE email = '%s')" % email
        db_cursor.execute(sql)
        email_check = db_cursor.fetchone()[0]
        return email_check

    @staticmethod
    def get_user(username):
        db_cursor = mysql_conn().cursor()
        sql = "SELECT * from user WHERE username = %s"
        db_cursor.execute(sql, username)
        user = db_cursor.fetchone()
        return user

    @staticmethod
    def get_user_for_id(u_id):
        db_cursor = mysql_conn().cursor()
        sql = "SELECT * from user WHERE u_id = %s"
        db_cursor.execute(sql, u_id)
        user = db_cursor.fetchone()
        return user
