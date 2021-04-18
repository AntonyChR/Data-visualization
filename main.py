# Python 3.8.5
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
from tkinter.colorchooser import askcolor as sc
from subprocess import run
import pandas as pd

from Modules.Graphics import graph as gr
import Modules.Features as ft

class main():
    def __init__(self):
        # var
        self.path_file     = None
        self.title_columns = ["there is no data"]
        self.line_styles   = list(ft.line_style.keys())
        self.marker_style  = list(ft.marker_style.keys())

        #Window container
        self.root          = Tk()
        self.root.title("XD")

        #Options var
        self.bar_menu = Menu(self.root)
        self.root.config(menu = self.bar_menu)
        self.root.resizable(False,False)

        #File
        self.file_menu = Menu(self.bar_menu, tearoff = 0)
        #Menu options
        self.file_menu.add_command(label = "New", command=self.new_window)
        self.file_menu.add_command(label = "Save")
        self.file_menu.add_command(label = "Quit")

        #edit
        self.edit_menu = Menu(self.bar_menu, tearoff = 0)
        
        self.edit_menu.add_command(label = "Clear")

       
        self.graph_prop_menu = Menu(self.bar_menu, tearoff = 0)
        self.graph_prop_menu.add_command(label = "Font")
        self.graph_prop_menu.add_command(label = "Font size")

        self.bar_menu.add_cascade(label ="File", menu = self.file_menu)
        self.bar_menu.add_cascade(label ="Edit" , menu = self.edit_menu)
        self.bar_menu.add_cascade(label ="Plot" , menu = self.graph_prop_menu)

        #path label
        self.data_boxes_labels = Frame(self.root)
        self.data_boxes_labels.grid(row = 0, column =0)

        self.path_label = Label(self.data_boxes_labels, text="File data: ")
        self.path_label.grid(row=0, column=0, padx=5)
        self.path = StringVar()
        self.path_box = Entry(self.data_boxes_labels, textvariable=self.path, width=35)
        self.path_box.config(justify=CENTER)
        self.path_box.grid(row=0, column=1,columnspan=2)
        # Selecti file button
        self.search_file_Btn = Button(
            self.data_boxes_labels, text=". . .", command=self.search_file)
        self.search_file_Btn.grid(row=0, column=3, padx=5, pady=5)

        # title
        self.title_label = Label(self.data_boxes_labels, text="Title: ")
        self.title_label.grid(row=1, column=0, padx=5)

        # title boxe
        self.title = StringVar()
        self.title.set("")
        self.title_box = Entry(self.data_boxes_labels, textvariable=self.title, width=35)
        self.title_box.config(justify=CENTER)
        self.title_box.grid(row=1, column=1,columnspan=2)

        self.x_label = Label(self.data_boxes_labels, text="X-axis title:")
        self.x_label.grid(row=2, column=0, pady=5, padx=5)

        self.x_name = StringVar()
        self.x_name.set("name (units)")
        self.x_name_box = Entry(self.data_boxes_labels, textvariable=self.x_name, width=35)
        self.x_name_box.config(justify=CENTER)
        self.x_name_box.grid(row=2, column=1, pady=5, columnspan=2)

        self.y_label = Label(self.data_boxes_labels, text="Y-axis title:")
        self.y_label.grid(row = 3, column = 0, padx = 5)

        self.y_name = StringVar()
        self.y_name.set("name (units)")
        self.y_name_box = Entry(self.data_boxes_labels, textvariable=self.y_name, width = 35)
        self.y_name_box.config(justify = CENTER)
        self.y_name_box.grid(row = 3, column = 1, pady = 5, columnspan = 2)


        self.x_name_variable_label = Label(self.data_boxes_labels, text = "X: ")
        self.x_name_variable_label.grid(row = 4, column = 0)

        self.x_data = ttk.Combobox(self.data_boxes_labels, width = 32)
        self.x_data.grid(row = 4, column = 1)
        self.x_data['values'] = self.title_columns

        self.y_name_variable_label = Label(self.data_boxes_labels, text = "Y: ")
        self.y_name_variable_label.grid(row = 5, column = 0)

        self.y_data = ttk.Combobox(self.data_boxes_labels, width = 32)
        self.y_data.grid(row = 5, column = 1, pady = 5)
        self.y_data['values'] = self.title_columns

        ttk.Separator(self.root, orient = VERTICAL).grid(row = 0, column = 1, sticky = 'ns')

        self.frame_ecuation = Frame(self.root)
        self.frame_ecuation.grid(row = 0, column = 2)

        self.ecuation_label = Label(self.frame_ecuation, text = "Equation")
        self.ecuation_label.grid(row = 4, column = 0)

        self.ecuation = StringVar()
        self.ecuation.set("")
        self.ecuation_box = Entry(self.frame_ecuation, textvariable = self.ecuation, width = 35)
        self.ecuation_box.config(justify = CENTER)
        self.ecuation_box.grid(row = 4, column = 1)

        self.domain_label = Label(self.frame_ecuation, text = "Domain a:b")
        self.domain_label.grid(row = 5, column = 0, pady = 5, padx =5 ) 

        self.domain = StringVar()
        self.domain.set("")
        self.domain_box = Entry(self.frame_ecuation, textvariable = self.domain, width = 35)
        self.domain_box.config(justify = CENTER)
        self.domain_box.grid(row = 5, column = 1, pady = 5)

        self.legend_label = Label(self.frame_ecuation, text = "Legend")
        self.legend_label.grid(row = 6, column = 0)

        self.legend_ecuation = StringVar()
        self.legend_ecuation.set("")
        self.legend_ecuation_box = Entry(self.frame_ecuation, textvariable = self.legend_ecuation, width = 35)
        self.legend_ecuation_box.config(justify = CENTER)
        self.legend_ecuation_box.grid(row = 6, column = 1)

        self.color_curve_label = Label(self.frame_ecuation, text = "Color de curva: ")
        self.color_curve_label.grid(row = 7, column = 0)

        self.color_curve = "#1F77B4"
        self.color_ecuation_buttom = Button(self.frame_ecuation, bg = self.color_curve, width = 1, command = self.select_colour_ecuation)
        self.color_ecuation_buttom.grid(row = 7, column = 1,pady = 5, sticky = "w")


        ttk.Separator(self.root, orient = HORIZONTAL).grid(row = 1, column = 1,columnspan = 2, sticky = 'ew')


        self.configuration_graph_data = Frame(self.root)
        self.configuration_graph_data.grid(row = 2, column = 0, columnspan = 4)


        self.grid_value = BooleanVar()
        self.grid = Checkbutton(self.configuration_graph_data,
								text     = "Grid",
								variable = self.grid_value,
								onvalue  = True,
								offvalue = False,
								height   = 2,
								width    = 10)
        self.grid.grid(row=0, column=0, padx=5)

        
        self.color_label = Label(self.configuration_graph_data,text ="Color Points:")
        self.color_label.grid(row = 0, column = 1)
        self.color_points="#FF0000"
        self.color_buttom = Button(self.configuration_graph_data, bg = self.color_points, width = 1, command = self.select_colour_points)
        self.color_buttom.grid(row = 0, column = 2)

        self.marker_label = Label(self.configuration_graph_data, text = "Marker: ")
        self.marker_label.grid(row = 0, column = 3)

        self.marker_list = ttk.Combobox(self.configuration_graph_data, width = 15)
        self.marker_list.grid(row = 0, column = 4, pady = 5)
        self.marker_list['values'] = self.marker_style


        # Lyne styles
        self.line_style_label = Label(self.configuration_graph_data, text = "Line Style: ")
        self.line_style_label.grid(row = 1, column = 0)

        self.line_style = ttk.Combobox(self.configuration_graph_data, width = 15)
        self.line_style.grid(row = 1, column = 1, pady = 5)
        self.line_style['values'] = self.line_styles

        # Size Points
        self.size_label = Label(self.configuration_graph_data, text = "Points size: ")
        self.size_label.grid(row = 1, column = 2, pady = 5, padx = 5)
        # Caja de entrada para el tamaño de los puntos
        self.size_var = DoubleVar()
        self.size_var.set(5.0)
        self.size_point = Spinbox(self.configuration_graph_data, from_=0.1, increment=0.1,to = 5.0, width = 7, textvariable = str(self.size_var))
        self.size_point.config(justify = CENTER)

        self.size_point.grid(row = 1, column = 3, pady = 5, columnspan = 2, sticky = "s")

        # button

        self.graph_buttom = Button(
            self.configuration_graph_data, text = "Graph", command = self.graph)
        self.graph_buttom.grid(row = 2,pady = 5,columnspan = 3, column = 0)
        

        self.root.mainloop()
        
    def search_file(self):

        self.path_file = filedialog.askopenfilename(initialdir="./", title="Select file", 
            filetypes=(("Excel file", "*.xlsx"), 
                       ("csv file", "*.csv"),
                       ("all files", "*.*")))
        self.path.set(self.path_file)
        self.get_title_columns()

    def select_colour_points(self):
        __, self.color_points = sc(title = "Color points")

        if self.color_points == None:
            self.color_points = "#FF0000"
        self.color_buttom.config(bg = self.color_points)
    
    def select_colour_ecuation(self):
        __ , self.color_curve = sc(title = "Curve color")

        if self.color_curve == None:
            self.color_curve = "#1F77B4"
        self.color_ecuation_buttom.config(bg = self.color_curve)

    def get_title_columns(self):
        if self.path_file != "":
            if self.path_file[-1] == "v":
                temp_file = pd.read_csv(self.path_file)
            else:
                temp_file = pd.read_excel(self.path_file)
            self.title_columns    = list(temp_file.columns)
            self.x_data['values'] = self.title_columns
            self.y_data['values'] = self.title_columns
        else:
            print("file not selected")
        
    def new_window(self):
        run(["cmd","/c","start main.py"])
    def clear(self):
        pass
    def graph(self):

        
        newGr = gr(
                   self.path_file,
                   self.title.get(),
                   self.x_name.get(),
                   self.y_name.get(),
                   self.grid_value.get(),
                   self.color_points,
                   self.line_style.get(),
                   self.size_var.get(),
                   self.ecuation.get(),
                   self.domain.get(),
                   self.legend_ecuation.get(),
                   self.color_curve,
                   self.x_data.get(),
                   self.y_data.get(),
                   self.marker_list.get()
                   )
        newGr.get_data()
        newGr.draw()

if __name__ == '__main__':
    main()
