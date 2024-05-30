import tkinter as tk
from tkinter import messagebox

class MathVisualApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Edukasi Matematika")
        
        self.canvas = tk.Canvas(root, width=400, height=300, bg='white')
        self.canvas.pack()

        self.control_frame = tk.Frame(root)
        self.control_frame.pack()

        self.shape_var = tk.StringVar(value="line")

        self.create_shape_selector()
        self.create_color_selector()
        self.create_input_fields()
        self.create_draw_button()
        
    def create_shape_selector(self):
        tk.Label(self.control_frame, text="Pilih Objek:").grid(row=0, column=0, sticky="w")

        shapes = [("Garis", "line"), ("Lingkaran", "circle"), ("Persegi Panjang", "rectangle")]
        for text, value in shapes:
            tk.Radiobutton(self.control_frame, text=text, variable=self.shape_var, value=value).grid(row=0, column=shapes.index((text, value))+1, sticky="w")

    def create_color_selector(self):
        self.color_var = tk.StringVar(value="black")
        self.fill_color_var = tk.StringVar(value="")

        tk.Label(self.control_frame, text="Warna Garis:").grid(row=1, column=0, sticky="w")
        self.create_color_menu(self.color_var, 1, 1)

        tk.Label(self.control_frame, text="Warna Isi:").grid(row=1, column=2, sticky="w")
        self.create_color_menu(self.fill_color_var, 1, 3)

    def create_color_menu(self, variable, row, column):
        colors = ["red", "green", "blue", "yellow", "magenta", "white"]
        color_menu = tk.OptionMenu(self.control_frame, variable, *colors)
        color_menu.grid(row=row, column=column, sticky="w")

    def create_input_fields(self):
        self.inputs_frame = tk.Frame(self.control_frame)
        self.inputs_frame.grid(row=2, column=0, columnspan=4, sticky="w")

        self.inputs = {}

        self.add_input_field("Titik Awal X:", "start_x", 0, 0)
        self.add_input_field("Titik Awal Y:", "start_y", 0, 1)
        self.add_input_field("Titik Akhir X:", "end_x", 1, 0)
        self.add_input_field("Titik Akhir Y:", "end_y", 1, 1)
        self.add_input_field("Tebal Garis:", "width", 2, 0, default_value="1")

        self.update_input_fields()

        self.shape_var.trace("w", lambda *args: self.update_input_fields())

    def add_input_field(self, label, key, row, column, default_value=""):
        tk.Label(self.inputs_frame, text=label).grid(row=row, column=column * 2, sticky="w")
        self.inputs[key] = tk.Entry(self.inputs_frame)
        self.inputs[key].grid(row=row, column=column * 2 + 1, sticky="w")
        self.inputs[key].insert(0, default_value)

    def update_input_fields(self):
        shape = self.shape_var.get()
        
        for key in self.inputs:
            self.inputs[key].grid_remove()

        if shape == "line":
            self.show_line_inputs()
        elif shape == "rectangle":
            self.show_rectangle_inputs()
        elif shape == "circle":
            self.show_circle_inputs()

    def show_line_inputs(self):
        self.inputs["start_x"].grid()
        self.inputs["start_y"].grid()
        self.inputs["end_x"].grid()
        self.inputs["end_y"].grid()
        self.inputs["width"].grid()

    def show_rectangle_inputs(self):
        self.inputs["start_x"].grid()
        self.inputs["start_y"].grid()
        self.inputs["end_x"].grid()
        self.inputs["end_y"].grid()
        self.inputs["width"].grid()

    def show_circle_inputs(self):
        self.inputs["start_x"].grid()
        self.inputs["start_y"].grid()
        self.add_input_field("Jari-Jari:", "radius", 2, 0)
        self.inputs["radius"].grid()
        self.inputs["width"].grid()

    def create_draw_button(self):
        draw_button = tk.Button(self.control_frame, text="Gambar", command=self.draw_shape)
        draw_button.grid(row=3, column=0, columnspan=4)

    def draw_shape(self):
        shape = self.shape_var.get()
        color = self.color_var.get()
        fill_color = self.fill_color_var.get()
        
        try:
            if shape == "line":
                start_x = int(self.inputs["start_x"].get())
                start_y = int(self.inputs["start_y"].get())
                end_x = int(self.inputs["end_x"].get())
                end_y = int(self.inputs["end_y"].get())
                width = int(self.inputs["width"].get())
                self.canvas.create_line(start_x, start_y, end_x, end_y, fill=color, width=width)
            elif shape == "rectangle":
                start_x = int(self.inputs["start_x"].get())
                start_y = int(self.inputs["start_y"].get())
                end_x = int(self.inputs["end_x"].get())
                end_y = int(self.inputs["end_y"].get())
                width = int(self.inputs["width"].get())
                self.canvas.create_rectangle(start_x, start_y, end_x, end_y, outline=color, width=width, fill=fill_color)
            elif shape == "circle":
                center_x = int(self.inputs["start_x"].get())
                center_y = int(self.inputs["start_y"].get())
                radius = int(self.inputs["radius"].get())
                width = int(self.inputs["width"].get())
                self.canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, outline=color, width=width, fill=fill_color)
        except ValueError:
            messagebox.showerror("Error", "Mohon masukkan nilai yang valid")

if __name__ == "__main__":
    root = tk.Tk()
    app = MathVisualApp(root)
    root.mainloop()
