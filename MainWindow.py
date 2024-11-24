
from PerformanceMetrics import Performance_metrics
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QListWidget, QScrollArea, QSplitter
from PyQt6.QtCore import Qt

class UI(QMainWindow):
	def __init__(self):	#Function that runs when initialized
		super().__init__()

		#Set Title of Window
		self.setWindowTitle("Employee Assessment Software")
		
		#Set Window Size
		self.resize(800,600)

		#divide window
		splitter = QSplitter(Qt.Orientation.Horizontal, self)

		#Create Display Panel
		view_panel = QWidget()
		view_layout = QVBoxLayout()
		
		#Title For Viewing Panel
		view_label = QLabel("Employee Evaluation")
		view_label.setStyleSheet("font-size: 24px;")
		view_layout.addWidget(view_label)
		
		view_panel.setLayout(view_layout)

		# Scroll Panel And Content
		select_panel = QWidget()
		select_layout = QVBoxLayout()

		scroll_area = QScrollArea()
		scroll_area.setWidgetResizable(True)

		scroll_content = QWidget()
		scroll_content_layout = QVBoxLayout()

		# Populate Scroll Panel
		for i in range(150):
			EmployeeID = f"{i:04}"
			label = QLabel(f"Employee ID: {EmployeeID}")
			scroll_content_layout.addWidget(label)
			# print(f"Added Employee: {EmployeeID}")
		scroll_content.setLayout(scroll_content_layout)
		scroll_area.setWidget(scroll_content)

		# Add Scroll Area to Layout
		select_layout.addWidget(scroll_area)
		select_panel.setLayout(select_layout)


		# Add created panels to layout
		splitter.addWidget(view_panel)
		splitter.addWidget(select_panel)
		splitter.setSizes([2,1])

		self.setCentralWidget(splitter)




# Run Window (will be called from a different file eventually)
app = QApplication(sys.argv)
window = UI()
window.show()
sys.exit(app.exec())