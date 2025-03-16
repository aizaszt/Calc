import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("calc.ui", self)  # Загрузка UI-файла

        # Подключаем кнопки к методам
        self.zero0.clicked.connect(lambda: self.add_digit("0"))
        self.one.clicked.connect(lambda: self.add_digit("1"))
        self.two.clicked.connect(lambda: self.add_digit("2"))
        self.three.clicked.connect(lambda: self.add_digit("3"))
        self.four.clicked.connect(lambda: self.add_digit("4"))
        self.five.clicked.connect(lambda: self.add_digit("5"))
        self.six.clicked.connect(lambda: self.add_digit("6"))
        self.seven.clicked.connect(lambda: self.add_digit("7"))
        self.eight.clicked.connect(lambda: self.add_digit("8"))
        self.nine.clicked.connect(lambda: self.add_digit("9"))

        self.add.clicked.connect(lambda: self.add_operator("+"))
        self.multuplication.clicked.connect(lambda: self.add_operator("*"))
        self.subt.clicked.connect(lambda: self.add_operator("-"))
        self.division.clicked.connect(lambda: self.add_operator("/"))
        self.dot.clicked.connect(lambda: self.add_dot("."))

        self.delete_2.clicked.connect(self.clear_display)
        self.equal.clicked.connect(self.calculate_result)

    def add_digit(self, digit):
        current_text = self.label.text()
        if current_text == "0":
            self.label.setText(digit)
        else:
            self.label.setText(current_text + digit)

    def add_operator(self, operator):
        current_text = self.label.text()
        if current_text and current_text[-1] not in "+-/*.":
            self.label.setText(current_text + operator)

    def add_dot(self):
        current_text = self.label.text()
        tokens= current_text.replace('+', " ").replace("-", " ").replace("*", " ").replace('/', " ").split()
        if tokens and "." not in tokens[-1]:
            self.label.setText(current_text+".")
        elif not tokens:
            self.label.setText("0.")
    def clear_display(self):

        self.label.setText("0")

    def calculate_result(self):

        try:
            result = eval(self.label.text())  # Не использовать eval в реальных проектах!
            self.label.setText(str(result))
        except:
            self.label.setText("Ошибка")


