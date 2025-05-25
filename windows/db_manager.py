import psycopg2




# f.create_tables()

class Database:
    instance = None
    def __init__(self):
        database = 'school management'
        host = 'localhost'
        user = 'postgres'
        password = 'Zshavkatov61'
        port = '5432'
        # print(123)

        self.conn = psycopg2.connect(
            database=database,
            host=host,
            user=user,
            password=password,
            port=port
        )

        self.cursor = self.conn.cursor()
        self.create_students_table()

    # Create tables
    def create_students_table(self):

        # The query

        create_students_table_query = f"""
                 create table if not exists students_table(
                 names TEXT,
                 student_id VARCHAR(15) PRIMARY KEY,
                 gender TEXT,
                 class TEXT,
                 birthday TEXT,
                 age INT,
                 address TEXT,
                 phone_number VARCHAR(20),
                 email VARCHAR(50)
                 )
             """

        self.cursor.execute(create_students_table_query)

        # Commit changes and close the connection
        self.conn.commit()
        self.conn.close()

    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = cls()
        return cls.instance

    def student_add(self, student_id, names, gender, grade, birthday, age, address, phone, email):
        sql = """INSERT INTO students_table(student_id, names, gender,grade,birthday,age,address,phone,email)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        self.cursor.execute(sql, (student_id, names, gender, grade, birthday, age, address, phone, email))
        self.conn.commit()

    def student_delete(self, student_id):
        sql = """DELETE FROM students_table WHERE student_id=%s"""
        self.cursor.execute(sql, (student_id,))
        self.conn.commit()

    def student_update(self, name, student_id):
        sql = """UPDATE TABLE students_table SET name=%s WHERE student_id=%s"""
        self.cursor.execute(sql, (name, student_id))
        self.conn.commit()

    def student_read(self, grade: int):
        sql = """SELECT * FROM public.students_table 
        where class=%s"""
        self.cursor.execute(sql, (f'Grade {grade}',))
        return self.cursor.fetchall()

    def student_by_grade(self, grade: int):
        sql = """SELECT * FROM students_table WHERE grade = %s"""
        self.cursor.execute(sql, (grade,))
        return self.cursor.fetchall()

    def student_by(self, grade: int, gender: int):
        sql = """SELECT * FROM students_table WHERE grade = %sa and gender=%s"""
        self.cursor.execute(sql, (grade,))
        return self.cursor.fetchall()

    @staticmethod
    def format_args(parameters: dict):
        sql = " AND ".join(
            [f"{param} = %s" for param in parameters]
        )
        return sql, tuple(parameters.values())

    def student_filter(self, **kwargs):
        sql, parameters = self.format_args(kwargs)
        sql = f"""SELECT * FROM students_table""" + f'WHERE {sql}' if parameters else ''
        self.cursor.execute(sql, parameters)
        return self.cursor.fetchall()

    def create_connection(self):
        # Establish connection
        database = 'school management'
        host = 'localhost'
        user = 'postgres'
        password = 'Zshavkatov61'
        port = '5432'

        self.conn = psycopg2.connect(
            database=database,
            host=host,
            user=user,
            password=password,
            port=port
        )

        return self.conn
