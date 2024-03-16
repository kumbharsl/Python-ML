# This script defines a PyQt5-based GUI application for displaying user information records.
# It includes a C2W_Info class that fetches records from a Firestore database  and displays them.
# Users can navigate back to the previous screen.

# Importing necessary libraries
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget, QScrollArea, QSplitter
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from dbConfig import db

# C2W_Info class definition
class C2W_Info(QWidget):
    def __init__(self, main_widget, back_widget):
        super().__init__()
        
        self.c2w_init_ui(main_widget, back_widget)
        self.back_widget = back_widget
        self.main_widget = main_widget
        
    # Method to initialize the UI elements
    def c2w_init_ui(self, main_widget, back_widget):
        # Header label
        header_label = QLabel('User Info Form')
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setStyleSheet('background-color: #003A6B; color: white; padding: 10px; font-size: 22px; max-height:40px')
        
        # Widget to hold the records layout
        self.records_widget = QWidget()
        # QVBoxLayout for the records
        self.records_layout = QVBoxLayout(self.records_widget)
        # Align records to the top
        self.records_layout.setAlignment(Qt.AlignTop)
        
        # Scroll area for records
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.records_widget)
        
        # Splitter to divide the window into two halves
        self.splitter = QSplitter(Qt.Horizontal)
        self.splitter.addWidget(QWidget())
        self.splitter.setSizes([self.width() // 2, self.width() // 2])
        self.splitter.setStyleSheet("QSplitter::handle {background: lightgray;}")
        
        # Header label for records
        header_label_records = QLabel('All Users')
        header_label_records.setAlignment(Qt.AlignCenter)
        header_label_records.setStyleSheet('background-color: #003A6B; color: white; padding: 10px; font-size: 22px; max-height:40px')
        
        # Back button
        self.backbtn = QPushButton("back")
        self.backbtn.clicked.connect(lambda : self.c2w_back())
        self.backbtn.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #013565, stop:1 #057be7);max-width:100px; font-size:20px; color:#ffffff; margin-top:10px")
        
        # Setting layout for the left section
        self.splitter.widget(0).setLayout(QVBoxLayout())
        self.splitter.widget(0).layout().addWidget(header_label_records)
        self.splitter.widget(0).layout().addWidget(self.backbtn)
        self.splitter.widget(0).layout().addWidget(scroll_area)
        
        # Add splitter to the main layout
        main_widget.addWidget(self.splitter)
        
        # Fetch records from Firestore
        user_profiles_ref = db.collection('user_profiles')
        user_profiles = user_profiles_ref.stream()
        self.record_label = QLabel("self")
        
        # Display records in the right section
        count = 1
        for user_profile in user_profiles:
            user_data = user_profile.to_dict()
            record_label = QLabel()
            record_label.setFont(QFont('Arial',12))
            records_text = f"Record : {count}\n" \
                        f"Name: {user_data['first_name']} {user_data['last_name']}\n" \
                        f"Mobile No: {user_data['mobile_no']}\n" \
                        f"College Name: {user_data['college_name']}\n" \
                        f"Date Of Birth: {user_data['dob']}\n" \
                        f"Age: {user_data['age']}\n" \
                        f"Gender: {user_data['gender']}\n" \
                        f"Height: {user_data['height']} cm\n" \
                        f"Firestore User ID: {user_profile.id}\n\n"

            record_label.setText(records_text)
            record_label.setStyleSheet("background-color: rgba(255, 132, 2, 0.15); border: 1px solid black; padding: 5px; border-radius:10px")
            self.records_layout.addWidget(record_label)
            if count % 2 == 0:
                record_label.setStyleSheet("background-color: rgba(0, 102, 197, 0.15); border: 1px solid black;padding: 5px; border-radius:10px")
            count += 1
            
        # If no records found, display appropriate message
        if not count > 1:
            self.records_layout.addWidget(QLabel("No records found"))
    
    # Method to navigate back to the previous screen
    def c2w_back(self):
        self.main_widget.removeWidget(self.splitter)
        self.back_widget(self.main_widget,self.splitter)
        