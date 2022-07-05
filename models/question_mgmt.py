from services.mysql import conn_mysql


class Question:
    def __init__(self, q_id, subject, content, create_date):
        self.q_id = q_id,
        self.subject = subject,
        self.content = content,
        self.create_date = create_date

    def __str__(self):
        return self.subject

    @staticmethod
    def get_question_list():
        db_cursor = conn_mysql().cursor()
        sql = "SELECT * FROM question"
        db_cursor.execute(sql)
        question_list = db_cursor.fetchall()

        if not question_list:
            return None

        return question_list

    @staticmethod
    def get_question(q_id):
        db_cursor = conn_mysql().cursor()
        sql = "SELECT * FROM question WHERE q_id = %d" % q_id
        db_cursor.execute(sql)
        question = db_cursor.fetchone()

        if not question:
            return None

        return question
