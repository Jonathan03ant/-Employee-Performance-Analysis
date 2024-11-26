
from PerformanceMetrics import Performance_metrics
import sys
from PyQt6.QtWidgets import (
	QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, 
	QHBoxLayout, QLabel, QListWidget, QScrollArea, QSplitter,
	QListWidget
)
from PyQt6.QtCore import Qt

class UI(QMainWindow):
	# ===== MEMBER VARIABLES =====
	widget_array = []

	view_panel = None
	list_display = None
	splitter = None



	# ===== MEMBER FUNCITONS =====

	def __init__(self):	#Function that runs when initialized
		super().__init__()
		# INITALIZE MEMBER Qt VARIABLES
		self.view_panel = QWidget()
		self.list_display = QListWidget()
		self.splitter = QSplitter(Qt.Orientation.Horizontal, self)

		#Set Title of Window
		self.setWindowTitle("Employee Assessment Software")
		
		#Set Window Size
		self.resize(800,600)

		#Create Display Panel
		view_layout = QVBoxLayout()
		
		#Title For Viewing Panel
		view_label = QLabel("Employee Evaluation")
		view_label.setStyleSheet("font-size: 24px;")
		view_layout.addWidget(view_label)
		
		self.view_panel.setLayout(view_layout)

		# Scroll Panel And Content
		select_panel = QWidget()
		select_layout = QVBoxLayout()

		# Populate Scroll Panel And Employee Array
		for i in range(150):
			EmployeeID = f"{i:04}"
			self.list_display.addItem(f"ID: {EmployeeID}")
			self.create_display_widget(f"ID: {EmployeeID}")
			# print(f"Added Employee: {EmployeeID}")
		
		#Connect to list_display slot
		self.list_display.itemClicked.connect(self.on_item_clicked)

		# Add Scroll Area to Layout
		select_layout.addWidget(self.list_display)
		select_panel.setLayout(select_layout)

		# Add created panels to layout
		self.splitter.addWidget(self.view_panel)
		self.splitter.addWidget(select_panel)
		self.splitter.setSizes([2,1])

		self.setCentralWidget(self.splitter)

	def create_display_widget(self, info):
		widget = QWidget()
		widget_layout = QVBoxLayout()
		
		# Populate Widget
		label = QLabel(f"Display Info For Employee With {info}")
		label.setStyleSheet("font-size: 24px;")
		widget_layout.addWidget(label)
		widget.setLayout(widget_layout)

		# Add Widget to list
		self.widget_array.append(widget)

	
	#Slot to handle item clicks for list panel
	def on_item_clicked(self, item):
		index = self.list_display.row(item)
		#print(f"Selected Index: {index}, {item.text()}")
		self.update_display(index)

	# Update the displayed information on the display screen
	def update_display(self, index):
		#print(f"display update to show info for Employee with {item.text()}")
		if index<self.widget_array.__sizeof__():
			self.splitter.replaceWidget(0, self.widget_array[index])
		else:
			print("ERROR: Cannot Display Entree (Does Not Exist In widget_array)")


# Run Window (will be called from a different file eventually)
app = QApplication(sys.argv)
window = UI()
window.show()
sys.exit(app.exec())