from PySide6.QtCore import QThread


class Students_information_Table(QThread):
    def __init__(self, side_bar):
        super().__init__()
        self.side_bar = side_bar

    def run(self):
        self.load_students_info()

    def load_students_info(self):
        # clear existing data in the data
        self.side_bar.studentInfo_table.setRowCount(0)

        # fetch data on the selected class and gender in the combo boxes
        selected_class = self.side_bar.select_class.currentText()
        selected_gender = self.side_bar.select_gender.currentText()
        data = self.get_data_from_table(selected_class, selected_gender)
        self.side_bar.populate_the_filter(data)

    def get_data_from_table(self, class_filter, gender_filter):

        cursor = self.side_bar.database.create_connection().cursor()

        query = f'''select * from students_table
        where
        ('{class_filter}' = 'SELECT CLASS' or class = '{class_filter}') 
        and
        ('{gender_filter}' = 'SELECT GENDER' or gender = '{gender_filter}')'''
        cursor.execute(query)

        data = cursor.fetchall()

        return data
