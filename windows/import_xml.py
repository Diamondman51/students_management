import xml.etree.ElementTree as ET
from time import strptime, strftime

import psycopg2
from PySide6.QtWidgets import QFileDialog


class XML_import:
    def __init__(self):
        self.parse_the_file()

    def parse_the_file(self):
        file_path, _ = QFileDialog.getOpenFileName(None, "Select File", "", "XML File (*.xml);;All Files (*)")

        if file_path:

            tree = ET.parse(file_path)

            dataset = tree.getroot()

            # for record in dataset:
            #     print(record.tag, record[0].text)

            data = [( record[1].text, record[2].text, record[3].text,
                     record[4].text, record[5].text, strftime('%Y-%m-%d', strptime(record[6].text, '%m/%d/%Y')))
                    for record in dataset]

            self.populate(data)

    def populate(self, xml_data):
        database = 'school management'
        user = 'postgres'
        password = 'Zshavkatov61'
        host = 'localhost'
        port = '5432'

        conn = psycopg2.connect(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port
        )

        cursor = conn.cursor()

        for data in xml_data:
            # print(data)
            query = f'''insert into students_table (names, email, gender, phone_number, address, birthday)
            values {data}
            '''

            cursor.execute(query)
            conn.commit()
        print('Success')
        conn.close()
