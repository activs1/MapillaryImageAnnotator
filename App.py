import tkinter as tk
from DataGenerator import DataGenerator
from Logger import Logger
from CsvWriter import CsvWriter
from PIL import Image, ImageTk


class App:

    def __init__(self):
        self.window = None
        self.generator = DataGenerator()
        self.logger = Logger()
        self.csv_writer = CsvWriter()
        self.index = self.logger.get_last() + 1

        self.image_size = (512, 512)
        self.image = None
        self.imageID = None
        self.image_on_canvas = None
        self.image_frame = None
        self.canvas = None
        self.confirm_button = None
        self.skip_button = None
        self.classes = ["highway", "city", "countryside"]
        self.choice_buttons_list = []
        self.image_name_label = None

        self.selected_class = ""

        self.create_window()
        self.create_checkboxes()
        self.createUI()
        self.run()


    def create_window(self):
        self.window = tk.Tk()
        self.window.state("zoomed")
        self.window.title("Annotator App")

    def run(self):
        self.window.mainloop()

    def create_checkboxes(self):
        for index, _class in enumerate(self.classes):
            self.choice_buttons_list.append(tk.Checkbutton(self.window, text=_class))
            if _class == 'highway':
                self.choice_buttons_list[index].configure(command=self.highway_selected)
            elif _class == 'city':
                self.choice_buttons_list[index].configure(command=self.city_selected)
            elif _class == 'countryside':
                self.choice_buttons_list[index].configure(command=self.countryside_selected)

    def createUI(self):
        self.image_frame = tk.Frame(self.window)
        self.canvas = tk.Canvas(self.image_frame, width=self.image_size[0], height=self.image_size[1],
                                background="black")
        self.canvas.pack(side=tk.LEFT)
        self.canvas.update()
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor='nw')
        self.image_frame.grid(column=0, row=2, rowspan=5, columnspan=5)

        self.image_name_label = tk.Label(self.window, text="fname")
        self.image_name_label.grid(column=0, row=1, columnspan=5)

        fname = self.generator[self.index]
        self.image = Image.open(fname)
        self.image = self.image.resize((self.image.width // 2, self.image.height // 2), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(self.image)
        self.canvas.itemconfigure(self.image_on_canvas, image=self.image)
        self.canvas.configure(width=self.image.width(), height=self.image.height())
        self.canvas.update()
        self.image_name_label.configure(text=fname)
        self.logger.log(fname, self.index)
        self.index += 1

        self.confirm_button = tk.Button(self.window, text="Confirm annotation", command=self.confirm_button_event)
        self.confirm_button.grid(column=5, row=0)

        self.skip_button = tk.Button(self.window, text="Skip image", command=self.skip_button_event)
        self.skip_button.grid(column=6, row=0)

        for index, checkbox in enumerate(self.choice_buttons_list):
            checkbox.grid(column=index, row=0)

    def highway_selected(self):
        self.selected_class = 'highway'
        for index, checkbox in enumerate(self.choice_buttons_list):
            if checkbox.cget('text') != 'highway':
                checkbox.deselect()

    def city_selected(self):
        self.selected_class = 'city'
        for index, checkbox in enumerate(self.choice_buttons_list):
            if checkbox.cget('text') != 'city':
                checkbox.deselect()

    def countryside_selected(self):
        self.selected_class = 'countryside'
        for index, checkbox in enumerate(self.choice_buttons_list):
            if checkbox.cget('text') != 'countryside':
                checkbox.deselect()

    def confirm_button_event(self):
        if self.selected_class != "":
            fname = self.generator[self.index]
            self.image = Image.open(fname)
            self.image = self.image.resize((self.image.width // 2, self.image.height // 2), Image.ANTIALIAS)
            self.image = ImageTk.PhotoImage(self.image)
            self.canvas.itemconfigure(self.image_on_canvas, image=self.image)
            self.canvas.configure(width=self.image.width(), height=self.image.height())
            self.canvas.update()
            self.image_name_label.configure(text=fname)
            self.logger.log(fname, self.index)
            for index, checkbox in enumerate(self.choice_buttons_list):
                checkbox.deselect()


            self.csv_writer.append_row(fname, self.selected_class)
            self.index += 1

    def skip_button_event(self):
        fname = self.generator[self.index]
        self.image = Image.open(fname)
        self.image = self.image.resize((self.image.width // 2, self.image.height // 2), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(self.image)
        self.canvas.itemconfigure(self.image_on_canvas, image=self.image)
        self.canvas.configure(width=self.image.width(), height=self.image.height())
        self.canvas.update()
        self.image_name_label.configure(text=fname)
        self.logger.log(fname, self.index, skip=True)
        self.index += 1