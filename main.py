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
        self.path_file = None
        self.title_columns = ["there is no data"]
        self.line_styles = list(ft.line_style.keys())
        self.marker_style = list(ft.marker_style.keys())

        # Window container
        self.root = Tk()
        self.root.title("XD")
        self.root.geometry("500x700")
        #Contains the graph configuration that user set
        self.config_graph_frame =Frame(self.root, borderwidth = 1)
        self.config_graph_frame.pack(side = LEFT,pady=5) 

        #contiene los labels
        self.text_frame = Frame(self.config_graph_frame)
        self.text_frame.pack(side = LEFT)

        self.input_frame = Frame(self.config_graph_frame)
        self.input_frame.pack()

        self.graph_frame = Frame(self.root, borderwidth = 2)
        self.graph_frame.config(bg = "red")
        self.graph_frame.pack(side=RIGHT,fill =BOTH, expand = True)

        self.lb=Label(self.graph_frame, text ="este es un texto")
        self.lb.pack()

        #-----------------------------------------------------------

        self.path_label = Label(self.text_frame, text="File data: ")
        self.path_label.pack(pady=5, anchor ="e")

        self.search_file_Btn = Button(
            self.input_frame, text=". . .", command=self.search_file)
        self.search_file_Btn.pack(side = RIGHT, anchor ="n")

        self.path = StringVar()
        self.path_box = Entry(self.input_frame,
                              textvariable=self.path, width=15)
        self.path_box.config( )
        self.path_box.pack(pady=5)
        # Selecti file button
        
        # title
        self.title_label = Label(self.text_frame, text="Title: ")
        self.title_label.pack(pady=5, anchor ="e")

        # titulo de la grafica
        self.title = StringVar()
        self.title.set("titulo")
        self.title_box = Entry(self.input_frame,
                               textvariable=self.title, width=15)
        
        self.title_box.pack(pady=5)

        #nombre del eje y
        self.x_label = Label(self.text_frame, text="X-axis title:")
        self.x_label.pack(pady=5, anchor ="e")

        self.x_name = StringVar()
        self.x_name.set("name (units)")
        self.x_name_box = Entry(self.input_frame,
                                textvariable=self.x_name, width=15)
        self.x_name_box.config( )
        self.x_name_box.pack(pady=5)

        #nombre del eje x
        self.y_label = Label(self.text_frame, text="Y-axis title:")
        self.y_label.pack(pady=5, anchor ="e")
        
        
        self.y_name = StringVar()
        self.y_name.set("name (units)")
        self.y_name_box = Entry(self.input_frame,
                                textvariable=self.y_name, width=15)
        self.y_name_box.config( )
        self.y_name_box.pack(pady=5)

        #nombre de columna
        self.x_name_variable_label = Label(self.text_frame, text="X: ")
        self.x_name_variable_label.pack(pady=5, anchor ="e")

        self.x_data = ttk.Combobox(self.input_frame, width=15)
        self.x_data.pack(pady=5)
        self.x_data['values'] = self.title_columns
        
        #nombre de columna
        self.y_name_variable_label = Label(self.text_frame, text="Y: ")
        self.y_name_variable_label.pack(pady=5, anchor ="e")

        self.y_data = ttk.Combobox(self.input_frame, width=15)
        self.y_data.pack(pady=5)
        self.y_data['values'] = self.title_columns

        #ecuacion de la grafica
        self.ecuation_label = Label(self.text_frame, text="Equation")
        self.ecuation_label.pack(pady=5, anchor ="e")

        self.ecuation = StringVar()
        self.ecuation.set("ecuacion")
        self.ecuation_box = Entry(
            self.input_frame, textvariable=self.ecuation, width=15)
        self.ecuation_box.pack(pady=5)

        #dominio de la ecuacion
        self.domain_label = Label(self.text_frame, text="Domain a:b")
        self.domain_label.pack(pady=5, anchor ="e")

        self.domain = StringVar()
        self.domain.set("")
        self.domain_box = Entry(self.input_frame,
                                textvariable=self.domain, width=15)
        self.domain_box.config( )
        self.domain_box.pack(pady=5)

        #legenda de la grafica
        self.legend_label = Label(self.text_frame, text="Legend")
        self.legend_label.pack(pady=5, anchor ="e")

        self.legend_ecuation = StringVar()
        self.legend_ecuation.set("")
        self.legend_ecuation_box = Entry(
            self.input_frame, textvariable=self.legend_ecuation, width=15)
        self.legend_ecuation_box.pack(pady = 5)

        self.color_curve_label = Label(self.text_frame, text="Color de curva: ")
        self.color_curve_label.pack(pady=5, anchor ="e")

        self.color_curve = "#1F77B4"
        self.color_ecuation_buttom = Button(
            self.input_frame, bg=self.color_curve, width=1, command=self.select_colour_ecuation)
        self.color_ecuation_buttom.pack(pady=5, anchor = "sw")

        '''
        ttk.Separator(self.root, orient=HORIZONTAL).grid(
            row=1, column=1, columnspan=2, sticky='ew')
        '''
        #contenido del frame de estilos ------------------------------------
        self.grid_label = Label(self.text_frame, text = "grid")
        self.grid_label.pack(pady=5, anchor ="e") 

       
        self.grid_value = BooleanVar()
        self.grid = Checkbutton(self.input_frame,
								text="",
								variable=self.grid_value,
								onvalue=True,
								offvalue=False,
								height=1,
								width=1)
        self.grid.pack(pady=5, anchor = "sw")

        self.color_label = Label(self.text_frame, text="Color Points:")
        self.color_label.pack(pady=5)
        self.color_points = "#FF0000"
        self.color_buttom = Button(self.input_frame,
                                   bg=self.color_points,width=1, command=self.select_colour_points)
        self.color_buttom.pack(pady=5, anchor ="w")

        self.marker_label = Label(self.text_frame, text="Marker: ")
        self.marker_label.pack(pady=5, anchor ="e")

        self.marker_list = ttk.Combobox(
            self.input_frame, width=15)
        self.marker_list.pack(pady=5)
        self.marker_list['values'] = self.marker_style

        # Lyne styles
        self.line_style_label = Label(
            self.text_frame, text="Line Style: ")
        self.line_style_label.pack(pady=5, anchor ="e")

        self.line_style = ttk.Combobox(self.input_frame, width=15)
        self.line_style.pack(pady=5)
        self.line_style['values'] = self.line_styles

        # Size Points
        self.size_label = Label(
            self.text_frame, text="Points size: ")
        self.size_label.pack(pady=5, anchor ="e")
        # Caja de entrada para el tamaño de los puntos
        self.size_var = DoubleVar()
        self.size_var.set(5.0)
        self.size_point = Spinbox(self.input_frame, from_=0.1,
                                  increment=0.1, to=5.0, width=7, textvariable=str(self.size_var))
        self.size_point.config( )

        self.size_point.pack(pady=5)

        # button
        self.graph_buttom = Button(
            self.root, text="Graph", command=self.graph)
        self.graph_buttom.pack(pady=5, side = BOTTOM, anchor="w")

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
