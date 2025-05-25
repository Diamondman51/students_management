# from PySide6.QtCore import Qt, QAbstractListModel, QModelIndex

# class MyModel(QAbstractListModel):
#     def __init__(self, data):
#         super().__init__()
#         self._data = data

#     def data(self, index, role):
#         if role == Qt.DisplayRole:
#             return self._data[index.row()]
#         return None

#     def rowCount(self, index):
#         return len(self._data)



# from PySide6.QtWidgets import QStyledItemDelegate, QApplication, QMessageBox
# from PySide6.QtCore import QRect, QSize

# class ButtonDelegate(QStyledItemDelegate):
#     def paint(self, painter, option, index):
#         super().paint(painter, option, index)
#         text = index.data()
#         painter.drawText(option.rect, Qt.AlignLeft, text)
#         button_rect = QRect(option.rect.right() - 80, option.rect.top() + 5, 70, option.rect.height() - 10)
#         painter.drawRect(button_rect)
#         painter.drawText(button_rect, Qt.AlignCenter, "Click")

#     def editorEvent(self, event, model, option, index):
#         button_rect = QRect(option.rect.right() - 80, option.rect.top() + 5, 70, option.rect.height() - 10)
#         if button_rect.contains(event.pos()):
#             QMessageBox.information(None, "Button Clicked", f"You clicked row {index.row()}")
#             return True
#         return False

#     def sizeHint(self, option, index):
#         return QSize(100, 40)



# from PySide6.QtWidgets import QApplication, QListView, QVBoxLayout, QWidget, QPushButton
# import sys

# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setMinimumWidth(500)
#         self.setMinimumHeight(500)
#         self.setWindowTitle("Fast QListView with Buttons")
#         layout = QVBoxLayout(self)
#         btn = QPushButton('Add')
#         layout

#         self.listview = QListView()
#         self.model = MyModel([f"Item {i}" for i in range(100000)])  # thousands of items
#         self.delegate = ButtonDelegate()

#         self.listview.setModel(self.model)
#         self.listview.setItemDelegate(self.delegate)
#         layout.addWidget(self.listview)


# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# sys.exit(app.exec())




from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QTableWidgetItem,
    QPushButton, QVBoxLayout, QWidget
)
from PySide6.QtCore import QThread, Signal, Slot, Qt
import sys
import time


# Background worker thread
class DataLoaderThread(QThread):
    row_data_ready = Signal(int, str)  # (row_index, row_value)

    def run(self):
        for i in range(10000):  # Simulate thousands of rows
            time.sleep(0.01)  # Simulate slight delay
            self.row_data_ready.emit(i, f"Item {i}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Async QTableWidget")
        self.resize(800, 600)

        self.table = QTableWidget(0, 2)
        self.table.setHorizontalHeaderLabels(["Data", "Action"])

        layout = QVBoxLayout()
        layout.addWidget(self.table)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.loader_thread = DataLoaderThread()
        self.loader_thread.row_data_ready.connect(self.add_row)
        self.loader_thread.start()

    # @Slot(int, str)
    def add_row(self, row: int, value: str):
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(value))

        button = QPushButton("Click")
        button.clicked.connect(lambda _, r=row: print(f"Button in row {r} clicked"))
        self.table.setCellWidget(row, 1, button)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
