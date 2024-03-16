import tkinter as tk
from tkinter import ttk
from tkinter import font

class FontListApp(tk.Frame):
    def __init__(self, parent, main_frame, userData):
        super().__init__(parent)
        self.parent = parent
        self.main_frame = main_frame
        self.configure(bg="#BCD2E8")
        self.userData = userData
        
        # Get the list of available fonts
        available_fonts = font.families()
        
        #Creat the main background frame
        self.c2w_background_frame = tk.Frame(self, bg="#BCD2E8", width=800, height=600)
        self.c2w_background_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create a text widget to display the font list
        font_list_text = tk.Text(self.c2w_background_frame, wrap=tk.WORD, height=20, width=40, bg="white", fg="black", font=("Helvetica", 12))
        font_list_text.pack(padx=50, pady=20, fill=tk.BOTH, expand=True)
        
        # Insert the font list into the text widget
        # Insert each font name into the text widget with index
        for i, font_family in enumerate(available_fonts):
            bg_color = "#FFFFFF" if i % 2 == 0 else "#EFEFEF"
            font_list_text.insert(tk.END, f"{i + 1}. {font_family}\n",bg_color)
        
        # Style the text widget
        font_list_text.config(state=tk.DISABLED) # Disable editing
        font_list_text.config(cursor="arrow") # Change cursor to arrow

        # Create a button to switch back to the home label
        switch_button = ttk.Button(self, text="Back", command=self.switch_to_class1, style="Rounded.TButton")
        switch_button.pack(pady=20)
    
    def switch_to_class1(self):
        from Home.C2w_home import homeLabel
        # Destroy the current frame
        self.destroy()
        
        # Create and display the new frame from Class1
        class1_instance = homeLabel(self.parent, self.main_frame, self.userData)
        class1_instance.pack(fill=tk.BOTH, expand=True)

    def apply_styles():
        # Create a custom style for rounded buttons
        style = ttk.Style()
        style.configure("Rounded.TButton",
                        foreground="white",
                        background="#3047ff",

                        font=("Helvetica", 12),
                        relief=tk.FLAT)
        style.map("Rounded.TButton",

        foreground=[("active", "white"), ("pressed", "white")],
        background=[("active", "#3047ff"), ("pressed", "#3047ff")])