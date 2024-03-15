# This script defines a PyQt5-based GUI application for user login.
# It includes a LoginWindow class that prompts users to input their mobile number and password,
# and upon submission, it verifies the credentials against a Firebase Firestore database.
# If the credentials are valid, it displays the user profile form from the 'home' module.

#Importing necessary libraries
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QApplication, QGraphicsDropShadowEffect, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPixmap
from home.c2w_home import C2W_UserProfileForm #  Import User Profile Form home module
from google.cloud  import firestore
import json

from dbConfig import db

#LoginWindow class Defination
class LoginWindow(QWidget):
    def  __init__(self):
        super().__init__()   #Call parent constructor
        self.layout = QVBoxLayout()
        
        #Creating outer widget for login  window frame
        self.outerWidgetLogin= QWidget
        self.outerWidgetLogin.setStyleSheet("background:#f9f9fc; max-height:600px; max-width:400px; border-radius:15px; margin-left:160px")
        
        #Loading logo image
        pixmap = QPixmap("./assets/image.png")
        
        # Displaying logo image
        self.image_label = QLabel(self)
        self.image_label.setPixmap(pixmap)
        self.image_label.setGeometry(0,0,10,10)
        self.image_label.setAlignment(Qt.AlignHCenter)
        self.image_label.setStyleSheet("margin-bottom:20px; margin-top:10px")
        
        # Adding Shadow effect to the login interface
        shadow = QGraphicsDropShadowEffect(self.outerWidgetLogin)
        shadow.setColor(QColor(63,63,63,180)) # Set shadow coloe and opatcity
        shadow.setBlurRadius(20)              # Set blurr radius of the shadow
        shadow.setXOffset(5)                  # Set horizontal offset of the shadow
        shadow.setXOffset(5)                  # Set  vertical offset of the shadow
        self.outerWidgetLogin.setGraphicsEffect(shadow)
        
        #Layout for outer widget
        outer_layout = QVBoxLayout(self.outerWidgetLogin)
        
        #Creating UI elemets
        self.heading = QLabel("Core2web")
        self.heading.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.heading.setStyleSheet()
        self.heading.setStyleSheet("font-size:25px; font-weight:500; margin-top:20px; height:60px; font-family:Poppins")
        self.pageHeading=QLabel("Login")
        self.pageHeading.setAlignment(Qt.AlignCenter)
        self.pageHeading.setStyleSheet("width:350px; font-size:30px; color:qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #013565, stop:1 #057be7);")
        
        self.userEmailLabel = QLineEdit()
        self.userEmailLabel.setPlaceholderText("Enter Mobile No")
        self.userEmailLabel.setStyleSheet("border:1px solid #918a8ae8; max-width:300px; padding-left:20px; font-size:15px; margin-top:40px")
        
        self.userPassLabel = QLineEdit()
        self.userPassLabel.setPlaceholderText("Enter Password")
        self.userPassLabel.setEchoMode(QLineEdit.Password)
        self.userPassLabel.setStyleSheet("border:1px solid #918a8ae8; max-width:300px; padding-left:20px; font-size:15px; margin-top:40px")
        
        self.submitBtn=QPushButton("Submit")
        self.submitBtn.clicked.connect(self.submit)
        self.submitBtn.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #013565, stop:1 #057be7);width:350px; font-size:20px; color:#ffffff; margin-top:50px")
        self.submitBtn.enterEvent = self.on_enter_btn
        self.submitBtn.leaveEvent = self.on_leave_btn
        
        # Adding UI elements to outer layout
        outer_layout.addWidget(self.image_label)
        outer_layout.addWidget(self.pageHeading)
        outer_layout.addLayout(self.inputFeildHolder)
        self.formLayout = QVBoxLayout()
        outer_layout.addLayout(self.formLayout)
        outer_layout.setAlignment(Qt.AlignHCenter)
        outer_layout.addStretch(1)
        
        # Setting main Layout
        self.layout.addWidget(self.outerWidgetLogin)
        self.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #013565, stop:1 #057be7); min-height:40px;")
        self.setLayout(self.layout)
        
    # Event handlers for UI elements
    def on_enter(self, event):
        self.userForgot.setStyleSheet("color: blue; margin-bottom:20px")
        
    def on_leave(self,event):
        self.userForgot.setStyleSheet("color: black; margin-bottom:20px")
        
    def on_enter_btn(self,event):
        self.submitBtn.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #013565, stop:1 #1ae7c3);width:350px; font-size:20px; color:#ffffff; margin-top:50px")
        
    def on_leave_btn(self,event):
        self.submitBtn.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #013565, stop:1 #057be7);width:350px; font-size:20px; color:#ffffff; margin-top:50px")
        
    #Method to handle login submission
    def submit(self):
        mobileNo =  self.userEmailLabel.text()
        password = self.userPassLabel.text()
        
        # Validating mobile  number format
        if not mobileNo.isdigit() or len(mobileNo) !=10 :
            QMessageBox.critical(self,"Error","Please enter a valid 10-digit Mobile Number.")
            return
        
        #Retrieving user profiles form Firestore
        user_profiles_ref = db.collection('c2w_admin')
        user_profiles = user_profiles_ref.stream()
        
        # Authenticating user
        for user_profiles in user_profiles:
            user_data = user_profiles.to_dict()
            if(user_data['mobileNo'] == mobileNo and user_data[ 'password']==password):
                self.setStyleSheet("background:white")
                self.layout.removeWidget(self.outerWidgetLogin)
                self.home = C2W_UserProfileForm(self.layout, LoginWindow)
                # Display user profile form
                break
        else:
             QMessageBox.critical(self,"Error","Invalid  Username/Password")