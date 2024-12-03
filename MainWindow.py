
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
		view_layout.addWidget(view_label, alignment=Qt.AlignmentFlag.AlignTop)
		
		# Add outline to view panel
		self.add_widget_outline(self.view_panel)
		
		self.view_panel.setLayout(view_layout)

		# Scroll Panel And Content
		select_panel = QWidget()
		self.add_widget_outline(select_panel)
		select_layout = QVBoxLayout()
		
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
	
	#Slot to handle item clicks for list panel
	def on_item_clicked(self, item):
		index = self.list_display.row(item)
		#print(f"Selected Index: {index}, {item.text()}")
		self.set_display_entry(index)

	# Update the displayed information on the display screen
	def set_display_entry(self, index):
		#print(f"display update to show info for Employee with {item.text()}")
		if index<self.widget_array.__sizeof__():
			self.splitter.replaceWidget(0, self.widget_array[index])
		else:
			print("ERROR: Cannot Display Entree (Does Not Exist In widget_array)")

	def add_entry(self, emp):
		# Initialize Widget and Layout
		widget = QWidget()
		self.add_widget_outline(widget)
		widget_layout = QVBoxLayout()
		widget_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
		
		# Add Important Labels
		self.add_label(widget_layout, 24, f"{emp.name}")					#Employee Name
		self.add_label(widget_layout, 18, f"Department: {emp.department}")	#Department
		self.add_label(widget_layout, 13, f"ID: {emp.employee_id}")			#Employee ID
		self.add_label(widget_layout, 13, f"Contact: {emp.email}\n")		#Email
		
		self.add_label(widget_layout, 16, f"Role: {emp.role}")				#Role
		self.add_label(widget_layout, 16, f"Salary: ${emp.salary}\n")		#Salary
		
		self.add_label(widget_layout, 18, f"Performance Score: {emp.nps}")	#Performance Score
		self.add_label(widget_layout, 18, f"Performance Summary:\n{emp.performance_summary}")

		# Add entry to list of widgets
		self.list_display.addItem(f"ID: {emp.employee_id}")

		# Add Widget to list
		widget.setLayout(widget_layout)
		self.widget_array.append(widget)

	def add_label(self, layout, font_size, text):
		lbl = QLabel(f"{text}")
		lbl.setStyleSheet(f"font-size: {font_size}px;")
		layout.addWidget(lbl)

	def add_widget_outline(self, widget):
		widget.setObjectName("OutlinedWidget")
		widget.setStyleSheet("""
    	QWidget#OutlinedWidget {
        	border: 4px solid black;
       		border-radius: 4px;
        	background-color: #f0f0f0;
    	}""")

'''
# Run Window (will be called from a different file eventually)
app = QApplication(sys.argv)
window = UI()
window.show()
sys.exit(app.exec())
'''