# # # # # from robyn import Robyn

# # # # # app = Robyn(__file__)

# # # # # @app.get("/")
# # # # # async def h(request):
# # # # #     return "Hello, world!"

# # # # # @app.post("/")
# # # # # async def h(request):
# # # # #     return "Hello, world!"

# # # # # app.start(port=8080)


# # # # from robyn import Robyn, templating, Response
# # # # from jinja2 import Environment, FileSystemLoader

# # # # app = Robyn(__file__)

# # # # # Configure Jinja2 environment
# # # # env = Environment(loader=FileSystemLoader("."))

# # # # @app.get("/")
# # # # def index():
# # # #     template = env.get_template("index.html")
# # # #     html_content = template.render(title="Welcome", name="Robyn User")
# # # #     # return Response(html_content)
# # # #     return Response(
# # # #         status_code=200,
# # # #         headers={"Content-Type": "text/html"},
# # # #         description=html_content
# # # #     )


# # # # app.start(port=8000)

# # # # # d = [i for i in range(30, 40)]

# # # # # data = [d[i:i+4] for i in range(0, len(d), 4)]

# # # # # for row in data:
# # # # #     for i in row:
# # # # #         print(i, end=' ')
# # # # #     print()



# # # import datetime


# # # class Person:
# # #     def __init__(self, age: int, name: str):
# # #         self.__age = age
# # #         self.__name = name

# # #     @property
# # #     def name(self):



# # # Jurabek = Person(20, 'Jo\'rabek')

# # # print(Jurabek.name)

# # def send_docs(name: str, age: int):
# #     docs = {
# #         'Name': name,
# #         'age': age
# #     }

# #     return docs

# # class Univer:
# #     def __init__(self, name: str):
# #         self.__students_docs = []
# #         self.__name = name
    
# #     # @property
# #     # def students_docs(self):
# #     #     return self.__students_docs
    
# #     # @students_docs.deleter
# #     # def students_docs(self, value):
# #     #     print('Student udalen', value)

# #     # @property
# #     # def name(self):
# #     #     return self.__name

# #     # @name.deleter
# #     # def name(self):
# #     #     print('dfghjk')
    
# #     # @name.setter
# #     # def name(self, name):
# #     #     if name == '':
# #     #         return
# #     #     self.__name = name


# # #     def get_docs(self, docs: dict):
# # #         self.students_docs.append(docs)

# # # akbar = send_docs('Akbar', 20)
# # # aybek = send_docs('Aybek', 21)
# # # fatxullo = send_docs('Fatxullo', 19)


# # Garvard = Univer('Garvard')
# # Oxford = Univer('Oxford')

# # print(Garvard.__name)
# # Garvard.__name = ''
# # Garvard.__name = 'Oybek'
# # print(Garvard.__name)



# # # Garvard.get_docs(akbar)
# # # Garvard.get_docs(fatxullo)

# # # Oxford.get_docs(aybek)
# # # Oxford.get_docs(akbar)

# # # del Oxford.name
# # # print(Oxford.name)

# # # print('Before:')
# # # print('Garvard: ', Garvard.students_docs)
# # # print('Oxford: ', Oxford.students_docs)

# # # print()
# # # print('After:')

# # # Oxford.get_docs(fatxullo)

# # # del Oxford.students_docs[0]

# # # print('Garvard: ', Garvard.students_docs)
# # # print('Oxford: ', Oxford.students_docs)


# from PySide6.QtWidgets import (
#     QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
# )
# from PySide6.QtCore import QPropertyAnimation, QEasingCurve, Qt, QRect
# import sys


# class Sidebar(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setFixedWidth(0)
#         self.setStyleSheet("background-color: #2e3440;")

#         layout = QVBoxLayout(self)
#         layout.addWidget(QLabel("Menu Item 1", alignment=Qt.AlignCenter))
#         layout.addWidget(QLabel("Menu Item 2", alignment=Qt.AlignCenter))
#         layout.addWidget(QLabel("Menu Item 3", alignment=Qt.AlignCenter))


# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Animated Sidebar")
#         self.setGeometry(100, 100, 800, 500)

#         self.sidebar = Sidebar()

#         self.toggle_btn = QPushButton("Toggle Sidebar")
#         self.toggle_btn.clicked.connect(self.toggle_sidebar)

#         self.main_content = QLabel("Main Content Area", alignment=Qt.AlignCenter)
#         self.main_content.setStyleSheet("background-color: #eceff4; padding: 50px; color: black")

#         layout = QHBoxLayout(self)
#         layout.addWidget(self.sidebar)
#         main_layout = QVBoxLayout()
#         main_layout.addWidget(self.toggle_btn)
#         main_layout.addWidget(self.main_content)
#         layout.addLayout(main_layout)

#         self.animation = QPropertyAnimation(self.sidebar, b"minimumWidth")
#         self.animation.setDuration(300)
#         self.animation.setEasingCurve(QEasingCurve.InOutQuad)

#         self.sidebar_expanded = False

#     def toggle_sidebar(self):
#         if self.sidebar_expanded:
#             self.animation.setStartValue(150)
#             self.animation.setEndValue(50)
#         else:
#             self.animation.setStartValue(50)
#             self.animation.setEndValue(150)
#         self.sidebar_expanded = not self.sidebar_expanded
#         self.animation.start()


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())



import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout
from PySide6.QtCore import QPropertyAnimation, QRect, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sidebar with Bottom-to-Top Animation")
        self.setGeometry(100, 100, 800, 600)

        # Central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Toggle button
        self.toggle_button = QPushButton("Toggle Sidebar")
        self.toggle_button.clicked.connect(self.toggle_sidebar)
        layout.addWidget(self.toggle_button)
        layout.addStretch()

        # Sidebar widget
        self.sidebar = QWidget(self)
        self.sidebar.setStyleSheet("background-color: #2b2b2b; border: 1px solid #555;")
        self.sidebar_width = 200
        self.sidebar_height = 300

        # # Initial position: hidden below the window
        # self.sidebar_hidden_pos = QRect(0, self.height(), self.sidebar_width, self.sidebar_height)
        # self.sidebar_visible_pos = QRect(0, self.height() - self.sidebar_height, self.sidebar_width, self.sidebar_height)
        # self.sidebar.setGeometry(self.sidebar_hidden_pos)

        # Animation setup
        self.animation = QPropertyAnimation(self.sidebar, b"geometry")
        self.animation.setDuration(300)  # Animation duration in milliseconds
        self.is_sidebar_visible = False

    def toggle_sidebar(self):
        if self.is_sidebar_visible:
            # Hide: move sidebar down
            self.animation.setStartValue(self.sidebar_visible_pos)
            self.animation.setEndValue(self.sidebar_hidden_pos)
        else:
            # Show: move sidebar up
            self.animation.setStartValue(self.sidebar_hidden_pos)
            self.animation.setEndValue(self.sidebar_visible_pos)

        self.animation.start()
        self.is_sidebar_visible = not self.is_sidebar_visible

    def resizeEvent(self, event):
        # Update sidebar positions on window resize
        self.sidebar_hidden_pos = QRect(0, self.height(), self.sidebar_width, self.sidebar_height)
        self.sidebar_visible_pos = QRect(0, self.height() - self.sidebar_height, self.sidebar_width, self.sidebar_height)
        
        # Update sidebar geometry based on visibility
        if self.is_sidebar_visible:
            self.sidebar.setGeometry(self.sidebar_visible_pos)
        else:
            self.sidebar.setGeometry(self.sidebar_hidden_pos)
        super().resizeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())