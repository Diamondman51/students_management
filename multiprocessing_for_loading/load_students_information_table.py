from time import sleep

from PySide6.QtWidgets import QTableWidgetItem, QPushButton
from PySide6.QtCore import QThread

from Buttons.Double_button_widgets import DoubleButtonWidgetStudents


class Students_information_Table(QThread):
    def __init__(self, side_bar):
        super().__init__()
        self.side_bar = side_bar

    def run(self):
        self.load_students_info()

    def load_students_info(self):
        pass
        # clear existing data in the data
        self.side_bar.studentInfo_table.setRowCount(0)

        # fetch data on the selected class and gender in the combo boxes
        selected_class = self.side_bar.select_class.currentText()
        selected_gender = self.side_bar.select_gender.currentText()
        data = self.get_data_from_table(selected_class, selected_gender)
        self.side_bar.populate_the_filter(data)


        # Populate the filter with the filtered data
        # for row_index, row_data in enumerate(data):
        #     self.side_bar.studentInfo_table.insertRow(row_index)
        #     for col_index, cell_data in enumerate(row_data):
        #         item = QTableWidgetItem(str(cell_data))
        #         self.side_bar.studentInfo_table.setItem(row_index, col_index, item)
        #
        #
        #     # create a custom widget with two buttons lined up horizontally for the actions column
        #     double_button_widget = DoubleButtonWidgetStudents(row_index, row_data, self)
        #     #
        #     # # Set this custom widget with two buttons lined up horizontally for the actions column
        #
        #     self.side_bar.studentInfo_table.setCellWidget(row_index, col_index+1, QPushButton(" + "))
        #     self.side_bar.studentInfo_table.setRowHeight(row_index, 50)
        #     sleep(1)


    def get_data_from_table(self, class_filter, gender_filter):

        cursor = self.side_bar.create_connection().cursor()

        query = f'''select * from students_table
        where
        ('{class_filter}' = 'SELECT CLASS' or class = '{class_filter}')
        and
        ('{gender_filter}' = 'SELECT GENDER' or gender = '{gender_filter}')'''
        print(query)
        cursor.execute(query)

        data = cursor.fetchall()

        return data
