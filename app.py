#! /usr/bin/env python3

from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QByteArray


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 1100, 1100)

        self.widgetSvg = QSvgWidget(parent=self)
        self.widgetSvg.setGeometry(10, 10, 1080, 1080)

#         svg = """
# <svg version="1.1" width="300" height="300" xmlns="http://www.w3.org/2000/svg">
#     <rect width="100%" height="100%" fill="red" />
#     <circle cx="150" cy="100" r="80" fill="green" />
#     <text x="150" y="125" font-size="60" text-anchor="middle" fill="white">SVG</text>
# </svg>
#         """.encode("UTF-8")
#         svg = """<svg xmlns="http://www.w3.org/2000/svg">
# <circle r="50"/>
# </svg>""".encode("UTF-8")
        svg = """<svg xmlns="http://www.w3.org/2000/svg">
<rect x="62" y="25" height="110" width="16"
fill="rgb(100%,50%,50%)" stroke="black"
stroke-width="2"/>

<rect x="35" y="35" height="30" width="50"
fill="red" stroke="black" stroke-width="2"/>

<rect x="5" y="60" height="30" width="50"
fill="#f88" stroke="black" stroke-width="2"/>

<rect x="25" y="70" height="30" width="50"
fill="#ff8888" stroke="black" stroke-width="2"/>

<rect x="65" y="60" height="30" width="50"
fill="#eac" stroke="black" stroke-width="2"/>

<rect x="85" y="70" height="30" width="50"
fill="#eeaacc" stroke="black"
stroke-width="2"/>

<rect x="60" y="95" height="30" width="50"
fill="rgb(255,0,0)" stroke="black"
stroke-width="2"/>
</svg>""".encode("UTF-8")
        self.widgetSvg.load(svg)

        return


if __name__ == "__main__":

    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
