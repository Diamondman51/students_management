import psycopg2



class Database:
    instance = None
    def __init__(self):
        self.create_tables()
        database = 'school'
        host = 'localhost'
        user = 'postgres'
        password = 'Zshavkatov61@'
        port = '5432'

        self.conn = psycopg2.connect(
            database=database,
            host=host,
            user=user,
            password=password,
            port=port
        )

        self.cursor = self.conn.cursor()

    # Create tables
    def create_tables(self):
        sql = """
        CREATE TABLE IF NOT EXISTS students(
            student_id varchar(15) Primary Key,
            names varchar(100),
            gender bool,
            class integer,
            birthday date,
            age integer,
            address varchar(200),
            phone_number varchar(15),
            email varchar(15)
        )"""
        self.cursor.execute(sql)
        self.conn.commit()

    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = cls()
        return cls.instance

    def student_add(self, student_id, names, gender, grade, birthday, age, address, phone, email):
        sql = """INSERT INTO students(student_id, names, gender,grade,birthday,age,address,phone,email)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        self.cursor.execute(sql, (student_id, names, gender, grade, birthday, age, address, phone, email))
        self.conn.commit()

    def student_delete(self, student_id):
        sql = """DELETE FROM students WHERE student_id=%s"""
        self.cursor.execute(sql, (student_id,))
        self.conn.commit()

    def student_update(self, name, student_id):
        sql = """UPDATE TABLE students SET name=%s WHERE student_id=%s"""
        self.cursor.execute(sql, (name, student_id))
        self.conn.commit()

    def student_read(self, grade: int):
        sql = """SELECT * FROM students"""
        self.cursor.execute(sql)
        return self.cursor.fetchall()

f = Database()
f.create_tables()