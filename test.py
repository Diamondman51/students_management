# # # # from random import randint
# # # #
# # # #
# # # # def generate_randomNumber():
# # # #     number = randint(1, 1000)
# # # #     random_number = f'{number:04d}'
# # # #     return random_number
# # # #
# # # # print(generate_randomNumber())
# # #
# # # tpl = ('one', 'two', 'three')
# # # tpl = ', '.join(tpl)
# # # # print(tpl)
# # #
# # #
# # # def pt(*args):
# # #     print(f"Hush kelibsiz, {', '.join(args[:-1])}", args[-1], sep=' va ')
# # #
# # #
# # # # pt('Anvar', 'Bekzod')
# # # # pt('Anvar', 'Bekzod', 'Otabek')
# # # # pt('Anvar', 'Anvar','Anvar','Anvar','Anvar','Anvar','Anvar','Anvar','Anvar','Anvar','Anvar','Anvar','Anvar','Anvar')
# # #
# # # # def info(**kwargs):
# # # #     print(', '.join([f"{key} {value}" for key, value in kwargs.items()]))
# # # #
# # # # info(ismi="Otabek", familiyasi="Nuriddinov", yoshi=2)
# # # # info(familiyasi="Nuriddinov", yoshi=20)
# # # # info(ismi="Otabek", yashash_joyi='Toshkent')
# # #
# # # def deco(f):
# # #     def ichki(a, b):
# # #         return
from g4f.client import Client

# # from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout
# # from PySide6.QtCore import QPropertyAnimation, QRect, QEasingCurve, Qt

# # class AnimatedStackedWidget(QStackedWidget):
# #     def __init__(self, *args, **kwargs):
# #         super().__init__(*args, **kwargs)
# #         self.current_index = 0

# #     def setCurrentIndex(self, index):
# #         old_widget = self.widget(self.current_index)
# #         new_widget = self.widget(index)
# #         direction = 1 if index > self.current_index else -1
# #         width = self.width()

# #         # Animate the old widget out
# #         old_animation = QPropertyAnimation(old_widget, b"geometry")
# #         old_animation.setDuration(400)
# #         old_animation.setStartValue(QRect(0, 0, width, self.height()))
# #         old_animation.setEndValue(QRect(-width * direction, 0, width, self.height()))
# #         old_animation.setEasingCurve(QEasingCurve.OutCubic)

# #         # Animate the new widget in
# #         new_widget.setGeometry(width * direction, 0, width, self.height())  # Prepare off-screen
# #         new_animation = QPropertyAnimation(new_widget, b"geometry")
# #         new_animation.setDuration(400)
# #         new_animation.setStartValue(QRect(width * direction, 0, width, self.height()))
# #         new_animation.setEndValue(QRect(0, 0, width, self.height()))
# #         new_animation.setEasingCurve(QEasingCurve.OutCubic)

# #         # Start animations
# #         old_animation.start()
# #         new_animation.start()

# #         super().setCurrentIndex(index)
# #         self.current_index = index

# # class MainWindow(QMainWindow):
# #     def __init__(self):
# #         super().__init__()
# #         self.setWindowTitle("Swipe Animation with Easing Example")
# #         self.resize(400, 300)

# #         central_widget = QWidget()
# #         self.setCentralWidget(central_widget)

# #         # Create AnimatedStackedWidget
# #         self.stacked_widget = AnimatedStackedWidget()

# #         # Add pages
# #         self.add_page("Page 1")
# #         self.add_page("Page 2")
# #         self.add_page("Page 3")

# #         # Buttons to change pages
# #         prev_button = QPushButton("Previous")
# #         prev_button.clicked.connect(self.prev_page)
# #         next_button = QPushButton("Next")
# #         next_button.clicked.connect(self.next_page)

# #         # Layout for navigation buttons
# #         nav_layout = QHBoxLayout()
# #         nav_layout.addWidget(prev_button)
# #         nav_layout.addWidget(next_button)

# #         # Main layout
# #         layout = QVBoxLayout(central_widget)
# #         layout.addWidget(self.stacked_widget)
# #         layout.addLayout(nav_layout)

# #     def add_page(self, text):
# #         if text == 'Page 1':

# #             page = QLabel(text)
# #             page.setStyleSheet('background-color: yellow')
# #             page.setAlignment(Qt.AlignCenter)
# #             self.stacked_widget.addWidget(page)
# #         if text == 'Page 2':
# #             page = QLabel(text)
# #             page.setStyleSheet('background-color: black')
# #             page.setAlignment(Qt.AlignCenter)
# #             self.stacked_widget.addWidget(page)
# #         if text == 'Page 3':
# #             page = QLabel(text)
# #             page.setStyleSheet('background-color: green')
# #             page.setAlignment(Qt.AlignCenter)
# #             self.stacked_widget.addWidget(page)



# #     def next_page(self):
# #         current_index = self.stacked_widget.currentIndex()
# #         next_index = (current_index + 1) % self.stacked_widget.count()
# #         self.stacked_widget.setCurrentIndex(next_index)

# #     def prev_page(self):
# #         current_index = self.stacked_widget.currentIndex()
# #         prev_index = (current_index - 1 + self.stacked_widget.count()) % self.stacked_widget.count()
# #         self.stacked_widget.setCurrentIndex(prev_index)

# # if __name__ == "__main__":
# #     app = QApplication([])

# #     window = MainWindow()
# #     window.show()

# #     app.exec()


# # data = [('Sarvinoz', '24/U/F0802', 'Female', 'Grade 5', '2008-02-05', 16, 'Ffdfsd', '998971030315265', 'fseefsefs@gmail.com'), ('SUha', '24/U/M0988', 'Male', 'Grade 1', '2000-01-01', 24, '', '', ''), ('Jovoh', '24/U/M0602', 'Male', 'Grade 9', '2008-02-05', 16, 'Axmad Yugnakiy, 52 uy, 31 xonadon', '98 352 72 11', 'ahmedshavkatov7@gmail.com'), ('Javohir', '24/U/M0690', 'Male', 'Grade 1', '2000-01-01', 24, "Bo'z 1, 27, 31", '894131213', 'dadawdsefgrdsgdrgdrgd')]
# #
# # for row, dat in enumerate(data):
# #     print(row, dat)


# # main.py
# import sys

# from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QVBoxLayout, QWidget, QTableWidgetItem


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Header Stylesheet Example")
#         self.setGeometry(100, 100, 600, 400)

#         self.table = QTableWidget(4, 4, self)

#         # Example data
#         for i in range(4):
#             for j in range(4):
#                 self.table.setItem(i, j, QTableWidgetItem(f"Item {i},{j}"))

#         layout = QVBoxLayout()
#         layout.addWidget(self.table)
#         container = QWidget()
#         container.setLayout(layout)
#         self.setCentralWidget(container)

#         self.default_style = """
#         QHeaderView::section {
#             background-color: red;
#             padding: 4px;
#             border: 1px solid gray;
#         }
#         QHeaderView::section:pressed {
#             background-color: green;
#             padding: 4px;
#             border: 1px solid blue;
#         }

#         """

#         self.table.horizontalHeader().setStyleSheet(self.default_style)
#         self.table.verticalHeader().setStyleSheet(self.default_style)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())


# seta = (0, 1, 'g', 2, 3, 4, 5, 6)
# for el in seta:
#     print(seta[el], el)
#     # if seta[el] % 3 == 0:
#     #     print(el, end=" ")


# не работает
# client = Client()
#
# response = client.chat.completions.create(
#     model='gpt-3.5-turbo',
#     messages=[{
#         'role':'user',
#         'content':'What is div on HTML'
#     }],
# )
#
# print(response.choices[0].message.content)