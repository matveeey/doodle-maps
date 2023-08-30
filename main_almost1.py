import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QListWidget, QPushButton, QLabel
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon

class MapApp(QMainWindow):
    add_point_signal = pyqtSignal(float, float)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Route Map App")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon("icon.png"))

        layout = QVBoxLayout()

        self.web_view = QWebEngineView()
        self.web_view.setHtml(open("map.html").read())
        layout.addWidget(self.web_view)

        self.add_point_button = QPushButton("Add Point")
        layout.addWidget(self.add_point_button)

        self.point_label = QLabel()
        layout.addWidget(self.point_label)

        self.point_list = QListWidget()
        layout.addWidget(self.point_list)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.add_point_button.clicked.connect(self.emit_add_point_signal)
        self.points = []

        self.add_point_signal.connect(self.add_point)
        self.update_point_list()

    def update_point_list(self):
        self.point_list.clear()
        for idx, point in enumerate(self.points):
            self.point_list.addItem(f"Point {point[2]}: {point[0]}, {point[1]}")

    def add_point(self, lat, lng):
        marker_id = len(self.points)
        self.points.append((lat, lng, marker_id))
        self.update_point_list()

        self.web_view.page().runJavaScript(f"addPoint({lat}, {lng}, {marker_id});")

    def move_point(self, marker_id, lat, lng):
        for idx, point in enumerate(self.points):
            if point[2] == marker_id:
                self.points[idx] = (lat, lng, marker_id)
                break
        self.update_point_list()

    def set_point_label(self, lat, lng):
        self.point_label.setText(f"Clicked Coordinates: Lat {lat}, Lng {lng}")

    def emit_add_point_signal(self):
        self.web_view.page().runJavaScript("getClickedCoords();")

    def receive_point_from_js(self, lat, lng):
        self.add_point_signal.emit(lat, lng)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MapApp()
    window.show()
    sys.exit(app.exec_())
