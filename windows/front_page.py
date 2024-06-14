import psycopg2
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QWidget, QMenu, QAbstractItemView, QTableWidgetItem, QFileDialog
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

from Buttons.Button_tools import Button_tools
from Buttons.Double_button_widgets import DoubleButtonWidgetStudents

from multiprocessing_for_loading.load_students_information_table import Students_information_Table
from ui_files.ui_index import Ui_Form
from windows.db_manager import Database
from windows.studentDialog import StudentDialog

import pandas as pd

from windows.xml_import import XML_import


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle('Sidebar menu')
        self.stackedWidget.setCurrentIndex(2)
        self.database = Database.get_instance()
        # set icon_only_widget hidden
        self.icon_only_widget.setHidden(True)

        # Hide dropdowns
        self.students_dropdown.setHidden(True)
        self.teachers_dropdown.setHidden(True)
        self.finance_dropdown.setHidden(True)
        # self.students_2.setChecked(True)
        # self.teachers_2.setChecked(True)
        # self.finance_2.setChecked(True)

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
        self.database.create_connection()

        # Create students table
        self.create_students_table()

        # Load students information to QTable with additional Thread
        # self.thread_load_students_info = Students_information_Table(self)
        # if not self.thread_load_students_info.isRunning():
        #     self.thread_load_students_info.start()

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

        # Excel export
        self.excelExport_btn.clicked.connect(self.export_to_excel_StudentsTable)

        # PDF export
        self.pdfExport_btn.clicked.connect(self.export_to_pdf_StudentsTable)

        # Import XML
        self.import_xml_btn.clicked.connect(self.import_xml_file)

        # Add button tools
        self.button_tools = Button_tools()

        self.add_to_layout()

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

    # CREATE STUDENTS TABLE
    def create_students_table(self):
        cursor = self.database.create_connection().cursor()

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

        cursor.execute(create_students_table_query)

        # Commit changes and close the connection
        self.database.conn.commit()
        self.database.conn.close()

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
        # if not self.thread_load_students_info.isRunning():
        #     self.thread_load_students_info.start()
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

        cursor = self.database.create_connection().cursor()

        query = f'''select * from students_table
        where
        ('{class_filter}' = 'SELECT CLASS' or class = '{class_filter}')
        and
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
        cursor = self.database.create_connection().cursor()
        sql_query = f"""select * from students_table
                    where lower(names) like lower('{search_query}%')"""
        cursor.execute(sql_query)
        result = cursor.fetchall()

        self.populate_the_filter(result)

    # Export to Excel
    def export_to_excel_StudentsTable(self):

        # Convert QTableWidget to pandas dataframe
        data = []

        self.headers = [self.studentInfo_table.horizontalHeaderItem(col).text() for col in range(self.studentInfo_table.columnCount())]

        for row in range(self.studentInfo_table.rowCount()):
            # Check if the item is not None before accessing its text
            row_data = [self.studentInfo_table.item(row, col).text() if self.studentInfo_table.item(row, col) is not None else '' for col in range(self.studentInfo_table.columnCount())]
            data.append(row_data)

        # Create a pandas Data Frame with the collected data and the headers
        df = pd.DataFrame(data, columns=self.headers)

        # Save the Data Frame to Excel file
        # Exclude the last column before exporting
        df_filtered = df.iloc[:, :-1]

        # Open QFileDialog to get the file path
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self, 'Save Excel File', '', 'Excel files (*.xlsx);;All Files (*)')

        if file_path:
            # Save the filtered Dataframe to Excel File at the choosen path
            df_filtered.to_excel(file_path, index=False)
            print(f'Table exported to {file_path}')
            print(data)


    # Export to PDF
    def export_to_pdf_StudentsTable(self):

        # Open QFileDialog to get the file path
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self, 'Save PDF file', '', 'PDF Files (*.pdf);;All Files (*)')
        if file_path:
            # Create a PDF Document
            pdf_document = SimpleDocTemplate(file_path, pagesize=letter)

            # Assuming n is the total number of columns in your QTable Widget
            n = self.studentInfo_table.columnCount()

            # Extract headers from the QTableWidget
            headers = [self.studentInfo_table.horizontalHeaderItem(col).text() for col in range(n - 1)]

            # Extract the data from the QTableWidget, excluding the last column
            data = [headers]

            for row in range(self.studentInfo_table.rowCount()):
                row_data = [self.studentInfo_table.item(row, col).text() if self.studentInfo_table.item(row, col) is not None else '' for col in range(n - 1)]
                data.append(row_data)

            # Create a PDF Table
            pdf_table = Table(data)

            # Apply the styles to the table
            style = TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 8),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ])

            pdf_table.setStyle(style)

            # Build the PDF Document
            pdf_document.build([pdf_table])

            print(f'Table exported to {file_path}')


    def populate_the_filter(self, data):
        # print(data)

        # Populate the filter with the filtered data
        for row_index, row_data in enumerate(data):
            self.studentInfo_table.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.studentInfo_table.setItem(row_index, col_index, item)

            # create a custom widget with two buttons lined up horizontally for the actions column
            double_button_widget = DoubleButtonWidgetStudents(row_index, row_data, self)

            # Set this custom widget with two buttons lined up horizontally for the actions column
            self.studentInfo_table.setCellWidget(row_index, 9, double_button_widget)
            self.studentInfo_table.setRowHeight(row_index, 50)

    def import_xml_file(self):
        data = XML_import(self)

    # Adding additional widget to for_btn_tools
    def add_to_layout(self):
        self.for_btn_tools.addWidget(self.button_tools)
