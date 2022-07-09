from database.conn_mysql import mysql_conn


class Question:
    def __init__(self, q_id, subject, content, create_date):
        self.q_id = q_id,
        self.subject = subject,
        self.content = content,
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
        # 질문 게시글 총 갯수
        total_question = Question.get_question_count()
        # (질문 갯수 / 페이지 출력 갯수)
        total_page = round(total_question / per_page)
        db_cursor = mysql_conn().cursor()
        sql = "SELECT * FROM question ORDER BY q_id LIMIT %s OFFSET %s" % (per_page, page*per_page)
        db_cursor.execute(sql)
        question_list = db_cursor.fetchall()

        if not question_list:
            return None

        return question_list

    @staticmethod
    def get_question(q_id):
        db_cursor = mysql_conn().cursor()
        sql = "SELECT * FROM question WHERE q_id = %d" % q_id
        db_cursor.execute(sql)
        question = db_cursor.fetchone()

        if not question:
            return None

        return question

    @staticmethod
    def insert(subject, content) -> bool:
        db_cursor = mysql_conn().cursor()
        sql = "INSERT INTO question(subject, content) VALUES('%s', '%s')" % (subject, content)
        result: int = db_cursor.execute(sql)
        mysql_conn().commit()
        return bool(result)
