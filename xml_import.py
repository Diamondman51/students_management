import xml.etree.ElementTree as ET
from time import strptime, strftime

import psycopg2

tree = ET.parse('students.xml')

dataset = tree.getroot()

# for record in dataset:
#     print(record.tag, record[0].text)

data = [(record[0].text, record[1].text, record[2].text, record[3].text,
         record[4].text, record[5].text, strftime('%Y-%m-%d', strptime(record[6].text, '%m/%d/%Y')))
        for record in dataset]
# for i in data:
#     print(i)


def populate():
    database = 'school management'
    user = 'postgres'
    password = 'Zshavkatov61@'
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

    for i in data:
        # print(i)
        query = f'''insert into students_table (student_id, names, email, gender, phone_number, address, birthday)
        values {i}
        '''

        cursor.execute(query)
        conn.commit()
    print('Success')

populate()


# class Import