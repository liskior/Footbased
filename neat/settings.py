from PyQt5.QtCore import pyqtSlot
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel, QComboBox,
    QHBoxLayout, QVBoxLayout, QGridLayout, QApplication)



class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Demo Footbased'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        save_button = QPushButton('Save')
        save_button.setToolTip('Save changes')
        save_button.clicked.connect(self.on_click)

        movements = ['Forward slide', 'Backward slide', 'Toe raise', 'Heel raise',
                        'Pronation', 'Suspination', 'Outward sweep']

        actions = ["Empty", "Zoom", "Swipe left", "Swipe right"]

        grid = QGridLayout()
        grid.setSpacing(10)

        for index, movement in enumerate(movements):

            dropdown = QComboBox(self)
            for action in actions:
                dropdown.addItem(action)
            grid.addWidget(dropdown, index, 0)
            label = QLabel(movement)
            grid.addWidget(label, index, 1)


        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(save_button)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        grid.addLayout(vbox, len(movements), 1)

        self.setLayout(grid)

        self.show()

        self.setFixedSize(self.size())

    @pyqtSlot()
    def on_click(self):
        print('Implement save changes')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())