import csv

from PySide6.QtWidgets import QFileDialog

from windows.db_manager import Database


class CSV_import:
    def __init__(self):
        self.parse_the_file()

    def parse_the_file(self):
        file_path, _ = QFileDialog.getOpenFileName(None, "Select File", "", "CSV Files (*.csv);;All Files (*)")

        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file, delimiter=',')
            reader = list(reader)
            self.populate(reader)
            # for r in reader:
            #     print(','.join(r))
    def populate(self, csv_data):

        database = Database.get_instance()
        conn = database.create_connection()

        cursor = conn.cursor()

        for data in csv_data[1:]:
            # print(i)
            query = f'''insert into students_table (student_id, names, gender, class, birthday, address, phone_number, email)
            values (%s, %s, %s, %s, %s, %s, %s, %s)
            '''

            cursor.execute(query, data)
            conn.commit()
        print('Success')
        conn.close()


# file = CSV_import()
# file.parse_the_file()