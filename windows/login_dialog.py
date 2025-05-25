import psycopg2
from PySide6.QtWidgets import QDialog, QLineEdit

from ui_files.login_dialog_UI import Ui_Dialog


class Login(Ui_Dialog, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Login')
        self.password_line.setEchoMode(QLineEdit.Password)
        # self.password_line.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        # self.password_line.setEchoMode(QLineEdit.NoEcho)

        self.sign_in_btn.clicked.connect(self.sign_in)

    def create_connection(self):
        database = 'school management'
        name = 'users'
        host = 'localhost'
        user = 'postgres'
        password = 'Zshavkatov61'
        port = '5432'

        conn = psycopg2.connect(
            user=user,
            database=database,
            host=host,
            password=password,
            port=port
        )

        cursor = conn.cursor()

        query = f'''create table if not exists {name}(
        email varchar(60),
        password varchar(30)
        )'''
        cursor.execute(query)
        conn.commit()
        return conn

    def sign_in(self):
        email = self.email_Line.text()
        password = self.password_line.text()
        print(f'{email}, {password}')
        conn = self.create_connection()
        cursor = conn.cursor()

        query = f'''select * from users where (email=%s and password=%s)'''

        cursor.execute(query, (email, password))
        # conn.commit()
        if cursor.fetchone():
            cursor.close()
            conn.close()
            self.accept()
        else:
            q = "select * from users where email='admin' and password='admin'"
            cursor.execute(q)
            conn.commit()
            res = cursor.fetchone()
            if not res:
                insert_admin = f'''insert into users values ('admin', 'admin')'''
                cursor.execute(insert_admin)
                conn.commit()
                cursor.close()
                conn.close()