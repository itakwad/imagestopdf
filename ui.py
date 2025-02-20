import customtkinter as ctk
from tkinter import filedialog, Label
from converter import convert_images_to_pdf

class ImageToPDFApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("تحويل الصور إلى PDF")
        self.geometry("750x520")
        self.resizable(False, False)  # منع تغيير حجم النافذة
        
        # أيقونة الزر بعلامة +
        self.btn_select = ctk.CTkButton(self, text="+", font=("Arial", 35, "bold"), width=40, height=40, command=self.select_images)
        self.btn_select.place(relx=0.9, rely=0.1, anchor='ne')
        
        # إضافة Tooltip
        self.tooltip = Label(self, text="اختيار الصور", bg="#333", fg="white", padx=5, pady=2)
        self.tooltip.place_forget()

        self.btn_select.bind("<Enter>", self.show_tooltip)
        self.btn_select.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        self.tooltip.place(relx=0.85, rely=0.1, anchor='ne')

    def hide_tooltip(self, event):
        self.tooltip.place_forget()

    def select_images(self):
        files = filedialog.askopenfilenames(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if files:
            output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF File", "*.pdf")])
            if output_path:
                convert_images_to_pdf(files, output_path)

# دالة لتشغيل الواجهة من main.py
def run_ui():
    app = ImageToPDFApp()
    app.mainloop()