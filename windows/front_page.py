import psycopg2
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QWidget, QMenu, QAbstractItemView, QTableWidgetItem

from Buttons.Double_button_widgets import DoubleButtonWidgetStudents
from UI_files.ui_index import Ui_Form
from windows.db_manager import Database
from windows.studentDialog import StudentDialog


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle('Sidebar menu')
        # self.stackedWidget.setCurrentIndex(0)
        self.database = Database.get_instance()
        # set icon_only_widget hidden
        self.icon_only_widget.setHidden(True)

        # Hide dropdowns
        self.students_dropdown.setHidden(True)
        self.teachers_dropdown.setHidden(True)
        self.finance_dropdown.setHidden(True)
        self.students_2.setChecked(True)
        self.teachers_2.setChecked(True)
        self.finance_2.setChecked(True)

        # Connect buttons to switch to different pages
        self.dashboard_1.clicked.connect(self.switch_to_dashboard_page)
        self.dashboard_2.clicked.connect(self.switch_to_dashboard_page)

        self.institution_1.clicked.connect(self.switch_to_institution_page)
        self.institution_2.clicked.connect(self.switch_to_institution_page)

        self.student_info.clicked.connect(self.switch_to_student_info_page)
        self.student_pay.clicked.connect(self.switch_to_student_payment_page)

        self.student_transaction.clicked.connect(self.switch_to_student_transaction_page)
        self.teacher_info.clicked.connect(self.switch_to_teacher_information_page)

        self.teacher_salary.clicked.connect(self.switch_to_teacher_salaries_page)
        self.teacher_transaction.clicked.connect(self.switch_to_teacher_transactions_page)

        self.budgets.clicked.connect(self.switch_to_finance_budgets_page)
        self.expenses.clicked.connect(self.switch_to_finance_expenses_page)

        self.business_overview.clicked.connect(self.switch_to_finance_business_overview_page)
        self.settings_1.clicked.connect(self.switch_to_settings_page)
        self.settings_2.clicked.connect(self.switch_to_settings_page)

        # Connect buttons to respective context menus
        self.students_1.clicked.connect(self.students_context_menu)
        self.teachers_1.clicked.connect(self.teachers_context_menu)
        self.finance_1.clicked.connect(self.finances_context_menu)

        # connect to sqlite and create database if it does not exist
        self.create_connection()

        # Create students table
        self.create_students_table()

        # Load students information to QTable
        self.load_students_info()
        self.select_class.currentIndexChanged.connect(self.reloadStudentstable_data)
        self.select_gender.currentIndexChanged.connect(self.reloadStudentstable_data)
        self.search_student.textChanged.connect(self.search_Students)

        # Control column width
        self.studentInfo_table.setColumnWidth(0, 120)
        self.studentInfo_table.setColumnWidth(1, 80)
        self.studentInfo_table.setColumnWidth(2, 60)
        self.studentInfo_table.setColumnWidth(3, 70)
        self.studentInfo_table.setColumnWidth(4, 70)
        self.studentInfo_table.setColumnWidth(5, 50)
        self.studentInfo_table.setColumnWidth(6, 70)
        self.studentInfo_table.setColumnWidth(7, 80)
        self.studentInfo_table.setColumnWidth(8, 120)
        self.studentInfo_table.setColumnWidth(9, 150)


        # Open add student dialog
        self.addStudent_btn.clicked.connect(self.open_addStudent_dialog)

        # Initialize table settings
        # self.init_table_settings()

        # Load students
        # self.load_students()

        # search
        self.search_student.textEdited.connect(self.search)

    # Methods to switch to different pages

    def switch_to_dashboard_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_institution_page(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_student_info_page(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_student_payment_page(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_to_student_transaction_page(self):
        self.stackedWidget.setCurrentIndex(4)

    def switch_to_teacher_information_page(self):
        self.stackedWidget.setCurrentIndex(5)

    def switch_to_teacher_salaries_page(self):
        self.stackedWidget.setCurrentIndex(6)

    def switch_to_teacher_transactions_page(self):
        self.stackedWidget.setCurrentIndex(7)

    def switch_to_finance_budgets_page(self):
        self.stackedWidget.setCurrentIndex(8)

    def switch_to_finance_expenses_page(self):
        self.stackedWidget.setCurrentIndex(9)

    def switch_to_finance_business_overview_page(self):
        self.stackedWidget.setCurrentIndex(10)

    def switch_to_settings_page(self):
        self.stackedWidget.setCurrentIndex(11)

    def students_context_menu(self):
        self.show_custom_context_menu(self.students_1,
                                      ['Student Information', 'Student Payments', 'Student Transactions'])

    def teachers_context_menu(self):
        self.show_custom_context_menu(self.teachers_1,
                                      ['Teacher Information', 'Teacher Salaries', 'Teacher Transactions'])

    def finances_context_menu(self):
        self.show_custom_context_menu(self.finance_1,
                                      ['Budgets', 'Expenses', 'Business Overview'])

    def show_custom_context_menu(self, button, menu_items):

        menu = QMenu(self)

        menu.setStyleSheet('''
            QMenu {
            background-color: black;
            color: white;
            border-radius:5;
            }

            QMenu:selected {
            background-color:white;
            color:#12B298;
            border-radius:5;;
            }
            ''')

        # add actions to the menu
        for item_text in menu_items:
            action = QAction(item_text, self)
            action.triggered.connect(self.handle_menu_item_click)
            menu.addAction(action)

        # Show the menu
        menu.move(button.mapToGlobal(button.rect().topRight()))
        menu.exec()

    def handle_menu_item_click(self):
        text = self.sender().text()

        if text == 'Student Information':
            self.switch_to_student_info_page()
        if text == 'Student Payments':
            self.switch_to_student_payment_page()
        if text == 'Student Transactions':
            self.switch_to_student_transaction_page()
        if text == 'Teacher Information':
            self.switch_to_teacher_information_page()
        if text == 'Teacher Salaries':
            self.switch_to_teacher_salaries_page()
        if text == 'Teacher Transactions':
            self.switch_to_teacher_transactions_page()
        if text == 'Budgets':
            self.switch_to_finance_budgets_page()
        if text == 'Expenses':
            self.switch_to_finance_expenses_page()
        if text == 'Business Overview':
            self.switch_to_finance_business_overview_page()

    # database_creation
    def create_connection(self):
        # Establish connection
        database = 'school management'
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

        # Craete a cursor to execute PostgreSQL

        corsor = self.conn.cursor()

        # Create the database if it does not exist
        # corsor.execute(f'Create database IF NOT EXISTS {database}')
        #
        # self.conn = psycopg2.connect(
        #     database=database,
        #     host=host,
        #     user=user,
        #     password=password,
        #     port=port
        # )

        return self.conn

    # CREATE STUDENTS TABLE

    def create_students_table(self):
        cursor = self.create_connection().cursor()

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
                phone_number VARCHAR(15),
                email VARCHAR(15)
                )
            """

        cursor.execute(create_students_table_query)

        # Commit changes and close the connection
        self.conn.commit()
        self.conn.close()

    def init_table_settings(self):
        column_names = ["Name", "Id", "Gender", "Class", "birthday", "age", "address", "phone_number", "email"]

        self.studentInfo_table.setColumnCount(len(column_names))
        self.studentInfo_table.setColumnWidth(0, 200)
        self.studentInfo_table.setColumnWidth(1, 50)
        self.studentInfo_table.setColumnWidth(2, 50)
        self.studentInfo_table.setColumnWidth(3, 50)
        self.studentInfo_table.setColumnWidth(4, 100)
        self.studentInfo_table.setColumnWidth(5, 50)
        self.studentInfo_table.setColumnWidth(6, 100)
        self.studentInfo_table.setColumnWidth(7, 200)
        self.studentInfo_table.setColumnWidth(7, 100)
        self.studentInfo_table.setColumnWidth(7, 100)

        self.studentInfo_table.setHorizontalHeaderLabels(column_names)

        self.studentInfo_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

    def load_students(self):
        self.studentInfo_table.clearContents()
        self.studentInfo_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        # self.studentInfo_table.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)

        # self.init_table_settings()

        # read from db
        students = self.database.student_read(9)

        print(f"So'rov natijas: {len(students)} ta mijoz")
        if not students:
            return

        # qatorlar sonini kirit
        self.studentInfo_table.setRowCount(len(students))

        # ma'lumotlarni jadvalga kirit
        for row, student in enumerate(students):
            for column, item in enumerate(student):
                self.studentInfo_table.setItem(row, column, QTableWidgetItem(str(item)))

    # Open dialog when inserting new student
    def open_addStudent_dialog(self):

        # instantiate and show the dialog
        addStudent_dialog = StudentDialog()
        result = addStudent_dialog.exec()  # This will block untill the dialog is closed
        # self.load_students()

        if result == StudentDialog.Accepted:
            # If the dialog was accepted (User clicked add student button)
            self.reloadStudentstable_data()

    def reloadStudentstable_data(self):
        self.load_students_info()

    # Search
    def search(self, ):
        pass

    # Load students info to QTable
    def load_students_info(self):
        # clear existing data in the data
        self.studentInfo_table.setRowCount(0)

        # fetch data on the selected class and gender in the combo boxes
        selected_class = self.select_class.currentText()
        selected_gender = self.select_gender.currentText()
        data = self.get_data_from_table(selected_class, selected_gender)
        self.populate_the_filter(data)

    def get_data_from_table(self, class_filter, gender_filter):

        cursor = self.create_connection().cursor()

        query = f'''select * from students_table
        where
        ('{class_filter}' = 'SELECT CLASS' or class = '{class_filter}') and
        ('{gender_filter}' = 'SELECT GENDER' or gender = '{gender_filter}')'''

        cursor.execute(query)

        data = cursor.fetchall()

        return data

    # Search
    def search_Students(self):

        # Clear previous table results
        self.studentInfo_table.setRowCount(0)

        # Get the search query from the QlineEdit
        search_query = self.search_student.text()

        # Execute the SQL query
        cursor = self.create_connection().cursor()
        sql_query = f"""select * from students_table
                    where lower(names) like lower('{search_query}%')"""
        cursor.execute(sql_query)
        result = cursor.fetchall()

        self.populate_the_filter(result)

    def populate_the_filter(self, data):

        # Populate the filter with the filtered data
        for row_index, row_data in enumerate(data):
            self.studentInfo_table.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.studentInfo_table.setItem(row_index, col_index, item)

            # create a custom widget with two buttons lineed up horizontally for the actions column
            double_button_widget = DoubleButtonWidgetStudents(row_index, row_data)

            # Set this custom widget with two buttons lineed up horizontally for the actions column
            self.studentInfo_table.setCellWidget(row_index, 9, double_button_widget)
            self.studentInfo_table.setRowHeight(row_index, 50)

