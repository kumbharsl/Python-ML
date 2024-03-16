import tkinter as tk
from tkinter import ttk
from tkinter import ttk, messagebox
import os
from PIL import Image, ImageTk
class homeLabel(tk.Frame):
    def __init__(self, parent, main_frame, userData):
        
        super().__init__(parent)
        self.parent = parent
        self.main_frame = main_frame
        self.configure(bg="lightblue")
        self.userData = userData
        
        # Add widgets to the new frame
        self.c2w_background_frame = tk.Frame(self, width=1000, height=1000)
        self.c2w_background_frame.pack(anchor=tk.CENTER, expand=True)
        
        # Create the left frame for navigation and buttons
        self.c2w_left_frame = tk.Frame(self.c2w_background_frame, bg="#00072D", width=300, height=1000)
        self.c2w_left_frame.pack(side=tk.LEFT, expand=True)
        
        # Set up button styling
        style = ttk.Style()
        style.configure("Rounded.TButton", borderwidth=0, relief="flat", background="#BCD2E8", padding=10, font=("Poppins", 12))
        style.map("Rounded.TButton", foreground=[('pressed', 'black'),('active', 'white')])
        
        # Create the Font Library button
        self.c2w_button_label = ttk.Button(self.c2w_left_frame, text="Font Library", style="Rounded.TButton", command=self.c2w_show_font_tab)
        self.c2w_button_label.pack()
        self.c2w_button_label.place(x=60, y=350, anchor='nw')
        
        # Create the Font Library button
        self.c2w_button_label = ttk.Button(self.c2w_left_frame, text="Font List", style="Rounded.TButton", command=self.switch_to_class2)
        self.c2w_button_label.pack()
        self.c2w_button_label.place(x=60, y=450, anchor='nw')

        # Load and display an image
        script_directory = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(script_directory,"../../assets/images/c2w.png")
        img = ImageTk.PhotoImage(Image.open(img_path))
        self.c2w_label = tk.Label(self.c2w_left_frame, image=img, background="#00072D")
        self.c2w_label.image = img
        self.c2w_label.pack()
        self.c2w_label.place(x=40, y=20, anchor='nw')
        
        # Set up the right frame for dynamic content
        rgba_color = (222, 55, 48, 255)
        tk_color = "#{:02x}{:02x}{:02x}".format(*rgba_color[:3])
        self.c2w_right_frame = tk.Frame(self.c2w_background_frame, bg="#BCD2E8", width=1200, height=1000)
        self.c2w_right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Set up a label with welcome text
        self.c2w_original_label_text = "Welcome To Core2web"
        self.c2w_right_label = tk.Label(self.c2w_right_frame, text=self.c2w_original_label_text, background="#BCD2E8", font=("Poppins", 50, "bold"), fg=tk_color)
        self.c2w_right_label.pack()
        self.c2w_right_label.place(x=200, y=300, anchor='nw')
        self.font_library_opened = False
        self.additional_widgets = []
    
    def c2w_show_font_tab(self):
        # Show Font Library tab
        if self.font_library_opened:
            messagebox.showinfo("Already Opened", "Font Library is already opened!")
        else:
            # Destroy existing widgets
            for widget in self.additional_widgets:
                widget.destroy()
            self.additional_widgets = []
            
            # Set up Font Library tab
            rgba_color = (222, 55, 48, 255)
            tk_color = "#{:02x}{:02x}{:02x}".format(*rgba_color[:3])
            
            # Create and pack widgets for Font Library
            self.c2w_heading_label = tk.Label(self.c2w_right_frame, text="Font Library", background="#BCD2E8", font=("Poppins", 20, "bold"), fg=tk_color)
            self.c2w_heading_label.pack()
            self.c2w_heading_label.place(x=60*2, y=150, anchor='nw')
            self.input_label = ttk.Entry(self.c2w_right_frame, width=60, font=("Poppins", 12))
            self.input_label.insert(0, "")
            self.input_label.pack()
            self.input_label.place(x=60*2, y=200, anchor='nw')
            self.c2w_right_label.config(text="")
            self.font_library_opened = True
            
            # Create buttons for different fonts
            self.c2w_button_label1 = ttk.Button(self.c2w_right_frame, text="Poppins", style="Rounded.TButton", command=self.c2w_poppinClicked)
            self.c2w_button_label1.pack()
            self.c2w_button_label1.place(x=60*2, y=350, anchor='nw')
        
            self.c2w_button_label2 = ttk.Button(self.c2w_right_frame, text="Modern", style="Rounded.TButton", command=self.c2w_modernClicked)
            self.c2w_button_label2.pack()
            self.c2w_button_label2.place(x=60*5, y=350, anchor='nw')
            
            self.c2w_button_label3 = ttk.Button(self.c2w_right_frame, text="Courier", style="Rounded.TButton", command=self.c2w_courierClicked)
            self.c2w_button_label3.pack()
            self.c2w_button_label3.place(x=60*8, y=350, anchor='nw')
            
            self.c2w_button_label4 = ttk.Button(self.c2w_right_frame, text="MS Sans Serif", style="Rounded.TButton", command=self.c2w_sanserifClicked)
            self.c2w_button_label4.pack()
            self.c2w_button_label4.place(x=60*11, y=350, anchor='nw')
            
            self.c2w_button_label5 = ttk.Button(self.c2w_right_frame, text="Calibri", style="Rounded.TButton", command=self.c2w_calibriClicked)
            self.c2w_button_label5.pack()
            self.c2w_button_label5.place(x=60*14, y=350, anchor='nw')

            self.c2w_show_label = tk.Label(self.c2w_right_frame, text="Hello from Core2web", background="#BCD2E9", font=("Poppins", 50, "bold"),fg=tk_color)
            self.c2w_show_label.pack()
            self.c2w_show_label.place(x=60*2, y=500, anchor='nw')

    def c2w_poppinClicked(self):
        # Change the font and display entered text
        self.c2w_show_label.config(text=self.input_label.get(), font=("Poppins", 30, "bold"))
    
    def c2w_modernClicked(self):
        # Change the font and display entered text
        self.c2w_show_label.config(text=self.input_label.get(), font=("Modern", 30, "bold"))
        
    def c2w_courierClicked(self):
        # Change the font and display entered text
        self.c2w_show_label.config(text=self.input_label.get(), font=("Courier", 30, "bold"))
        
    def c2w_sanserifClicked(self):
        # Change the font and display entered text
        self.c2w_show_label.config(text=self.input_label.get(), font=("MS Sans Serif", 30, "bold"))
    
    def c2w_calibriClicked(self):
        # Change the font and display entered text
        self.c2w_show_label.config(text=self.input_label.get(), font=("Calibri", 30, "bold"))
    
    def switch_to_class2(self):
        from FontList.C2w_fontList import FontListApp
        # Destroy the current frame
        self.destroy()
        
        # Create and display the new frame from Class2
        class2_instance = FontListApp(self.parent, self.main_frame, self.userData)
        class2_instance.pack(fill=tk.BOTH, expand=True)

    def c2w_reset_ui(self):
        # Reset UI when going back
        self.font_library_opened = False
        
        for widget in self.additional_widgets:
            widget.destroy()
        self.additional_widgets = []
        self.c2w_heading_label.destroy()
        self.input_label.destroy()
        self.c2w_button_label1.destroy()
        self.c2w_button_label2.destroy()
        self.c2w_button_label3.destroy()
        self.c2w_button_label4.destroy()
        self.c2w_button_label5.destroy()
        self.c2w_show_label.destroy()
        self.c2w_right_label.config(text=self.c2w_original_label_text)
        