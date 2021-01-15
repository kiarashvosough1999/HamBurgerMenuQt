from PyQt5.QtCore import Qt, QSize, QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QFrame, QMainWindow, QPushButton, QSizePolicy


class HamBurgerMenu(QMainWindow):

    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.centralwidget = QWidget()
        self.centralwidget.setMinimumSize(400, 300)

        size = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.splitter = QVBoxLayout(self.centralwidget)  # hold top bar frame and showable window
        self.splitter.setContentsMargins(0, 0, 0, 0)
        self.splitter.setSpacing(0)

        self.top_bar_frame = QFrame(
            self.centralwidget)  # act as adapter between back layer layout and new HBoxLayout on top bar
        self.top_bar_frame.setSizePolicy(size)
        self.top_bar_frame.setMaximumHeight(70)
        self.top_bar_frame.setFrameShape(QFrame.NoFrame)
        self.top_bar_frame.setFrameShadow(QFrame.Raised)

        self.top_bar_horizontalLayout = QHBoxLayout(self.top_bar_frame)  # hold widgets in top bar
        self.top_bar_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_bar_horizontalLayout.setSpacing(0)

        # x = QPushButton( "f", self.top_bar_frame)
        # x.setMaximumWidth(40)
        # x.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        # x.setSizePolicy(size)

        top_toggle_button_frame = QFrame(self.top_bar_frame)
        top_toggle_button_frame.setSizePolicy(size)
        # top_toggle_button_frame.setMaximumWidth(70)
        # top_toggle_button_frame.setMaximumHeight(70)
        # top_toggle_button_frame.setFrameShape(QFrame.StyledPanel)
        # top_toggle_button_frame.setFrameShadow(QFrame.Raised)
        top_toggle_button_frame.setStyleSheet(u"background-color: white;")

        top_bar_customizable_frame = QFrame(self.top_bar_frame)
        top_bar_customizable_frame.setSizePolicy(size)
        top_bar_customizable_frame.setFrameShape(QFrame.StyledPanel)
        top_bar_customizable_frame.setFrameShadow(QFrame.Raised)
        top_bar_customizable_frame.setStyleSheet(u"background-color: rgb(200, 100, 135);")

        top_bar_toggle_button_vertical_holder_layout = QVBoxLayout(top_toggle_button_frame)
        top_bar_toggle_button_vertical_holder_layout.setContentsMargins(0, 0, 0, 0)
        top_bar_toggle_button_vertical_holder_layout.setSpacing(0)

        q = QPushButton(" Menu", top_toggle_button_frame)
        q.clicked.connect(self.animate1)
        # q.isFlat = True
        q.setStyleSheet("QPushButton {\
        border: 0;\
        margin: 5px;\
        padding: 5px;}")

        p = QPixmap("hamburger-menu-10-782968.png")
        q.setIcon(QIcon(p))
        q.setSizePolicy(size)
        top_bar_toggle_button_vertical_holder_layout.addWidget(q)

        top_toggle_button_frame.setLayout(top_bar_toggle_button_vertical_holder_layout)

        self.top_bar_horizontalLayout.addWidget(top_toggle_button_frame, 0, Qt.AlignLeft)
        self.top_bar_horizontalLayout.addWidget(top_bar_customizable_frame)

        self.top_bar_frame.setLayout(self.top_bar_horizontalLayout)

        self.mainPage_frame = QFrame(self.centralwidget)
        # self.mainPage_frame.setStyleSheet(u"background-color: rgb(100, 201, 35);")
        self.mainPage_horizontalLayout = QHBoxLayout(self.mainPage_frame)
        self.mainPage_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainPage_horizontalLayout.setSpacing(0)

        self.navigation_drawer_frame = QFrame(self.mainPage_frame)
        # self.navigation_drawer_frame.setSizePolicy(size)
        self.navigation_drawer_frame.setMinimumWidth(77)
        # self.navigation_drawer_frame.setMaximumWidth(77)
        self.navigation_drawer_frame.setStyleSheet(u"background-color: rgb(100, 201, 35);")

        self.navigation_drawer_vertical_layout = QVBoxLayout(self.navigation_drawer_frame)
        self.navigation_drawer_vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.navigation_drawer_vertical_layout.setSpacing(0)

        bt1 = QPushButton("hhhhh", self.navigation_drawer_frame)
        bt1.setSizePolicy(size)
        # bt1.setMaximumHeight(20)

        self.navigation_drawer_vertical_layout.addWidget(bt1, 0, Qt.AlignTop)

        self.navigation_drawer_frame.setLayout(self.navigation_drawer_vertical_layout)

        self.mainPage_horizontalLayout.addWidget(self.navigation_drawer_frame, 0, Qt.AlignLeading)

        self.mainPage_frame.setLayout(self.mainPage_horizontalLayout)
        self.splitter.addWidget(self.top_bar_frame)
        self.splitter.addWidget(self.mainPage_frame)

        self.centralwidget.setLayout(self.splitter)
        self.setCentralWidget(self.centralwidget)

        self.show()

    def animate1(self):
        print("jjjj")
        animation = QPropertyAnimation(self.navigation_drawer_frame, b"minimumWidth")
        animation.setDuration(400)
        animation.setStartValue(self.navigation_drawer_frame.width())
        animation.setEndValue(100)
        animation.setEasingCurve(QEasingCurve.InOutQuart)
        animation.start()
