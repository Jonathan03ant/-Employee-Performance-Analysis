
from PerformanceMetrics import Performance_metrics
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import Qt

class UI(QMainWindow):
	def __init__(self):	#Function that runs when initialized
		super().__init__()

		#Set Title of Window
		self.setWindowTitle("Employee Assessment")
		
		#Set Window Size
		self.resize(800,600)

		#Add Label
		label= QLabel("Testing this out", self)
		label.setStyleSheet("font-size: 24px;")
		label.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.setCentralWidget(label)




app = QApplication(sys.argv)
window = UI()
window.show()
sys.exit(app.exec())