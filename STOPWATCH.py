import sys
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QMainWindow)
from PyQt5.QtCore import QTimer, Qt
class stopwatch(QMainWindow):
    def __init__(self):
        super().__init__()
        self.elapsed_ms = 0
        self.timer_obj = QTimer()
        self.timer_obj.timeout.connect(self.update_label)
        self.timer = QLabel("00:00:00")
        self.central_widget = QWidget()
        self.layout = QVBoxLayout()
        self.seclayout = QHBoxLayout()
        self.initUI()
    def initUI(self):
        self.start = QPushButton("START")
        self.stop = QPushButton("STOP")
        self.restart = QPushButton("RESTART")
        self.seclayout.addWidget(self.start)
        self.seclayout.addWidget(self.stop)
        self.seclayout.addWidget(self.restart)
        self.setWindowTitle("STOP WATCH")
        self.layout.addWidget(self.timer)
        self.layout.addLayout(self.seclayout)
        self.setCentralWidget(self.central_widget)
        self.setGeometry(650, 400, 700, 200)
        self.timer.setStyleSheet("font-size: 100px;"
                                 "color: green;"
                                 "background-color: black"
                                 )
        self.central_widget.setLayout(self.layout)
        self.timer.setAlignment(Qt.AlignHCenter)
        self.start.clicked.connect(self.starter)
        self.stop.clicked.connect(self.stoper)
        self.restart.clicked.connect(self.restarter)

    def starter(self):
        self.timer_obj.start(10)

    def stoper(self):
        self.timer_obj.stop()



    def restarter(self):
        (self.restarterr())

    def restarterr(self):
        self.elapsed_ms = 0
        self.timer_obj.stop()
        self.rendering()



    def update_label(self):
        self.elapsed_ms += 10
        self.rendering()

    def rendering(self):
        self.minutes = (self.elapsed_ms // 1000) // 60
        self.seconds = (self.elapsed_ms // 1000) % 60
        self.milliseconds = self.elapsed_ms % 1000
        self.timer.setText(f"{self.minutes:02d}:{self.seconds:02d}:{self.milliseconds:03d}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    WATCH = stopwatch()
    WATCH.show()
    sys.exit(app.exec_())

