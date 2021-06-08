# Python 3.8.5
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
from tkinter.colorchooser import askcolor as sc

import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)


from Modules.Graphics import graph as gr
# import Modules.Features as ft
from Modules.Features import marker_style, line_style

from win32api import GetSystemMetrics

class main():
    def __init__(self):

        self.y_resolution = GetSystemMetrics(1)
        self.x_resolution = GetSystemMetrics(0)
        # var
        self.path_file     = None
        self.data_frame    = None
        self.data          = None
        self.title_columns = ["..."]
        self.line_styles   = list(line_style.keys())
        self.marker_style  = list(marker_style.keys())

        # Window container
        self.root = Tk()
        self.root.title("Graph")
        self.root.minsize(800,550)
        self.root.geometry("900x550")
        self.root.resizable(height = None, width = None)
        #Contains the graph configuration that user set
        self.config_graph_frame =Frame(self.root, borderwidth = 1)
        self.config_graph_frame.pack(side = LEFT,pady=5) 

        self.conf_container=Frame(self.config_graph_frame)
        self.conf_container.pack()

        #input boxes container
        self.input_frame = Frame(self.conf_container)
        self.input_frame.pack(side = RIGHT)
        #labels container
        self.text_frame = Frame(self.conf_container)
        self.text_frame.pack()

        
        #-----------------------------------------------------------

        self.path_label = Label(self.text_frame, text="File data: ")
        self.path_label.pack(pady=5, anchor ="e")

        self.import_data_Btn = Button(
            self.input_frame, text=". . .", command=self.import_data)
        self.import_data_Btn.pack(side = RIGHT, anchor ="n")

        self.path = StringVar()
        self.path_box = Entry(self.input_frame,
                              textvariable=self.path, width=15)
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
        self.x_name_box.pack(pady=5)

        #nombre del eje x
        self.y_label = Label(self.text_frame, text="Y-axis title:")
        self.y_label.pack(pady=5, anchor ="e")
        
        
        self.y_name = StringVar()
        self.y_name.set("name (units)")
        self.y_name_box = Entry(self.input_frame,
                                textvariable=self.y_name, width=15)
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
        self.equation_label = Label(self.text_frame, text="Equation")
        self.equation_label.pack(pady=5, anchor ="e")

        self.equation = StringVar()
        self.equation.set("x**2")
        self.equation_box = Entry(
            self.input_frame, textvariable=self.equation, width=15)
        self.equation_box.pack(pady=5)

        #dominio de la ecuacion
        self.domain_label = Label(self.text_frame, text="Domain a:b")
        self.domain_label.pack(pady=5, anchor ="e")

        self.domain = StringVar()
        self.domain.set("")
        self.domain_box = Entry(self.input_frame,
                                textvariable=self.domain, width=15)
        self.domain_box.pack(pady=5)

        #legenda de la grafica
        self.legend_label = Label(self.text_frame, text="Legend")
        self.legend_label.pack(pady=5, anchor ="e")

        self.legend_equation = StringVar()
        self.legend_equation.set("")
        self.legend_equation_box = Entry(
            self.input_frame, textvariable=self.legend_equation, width=15)
        self.legend_equation_box.pack(pady = 5)

        # color de la curva de la ecuacion
        self.color_curve_label = Label(self.text_frame, text="Color de curva: ")
        self.color_curve_label.pack(pady=5, anchor ="e")

        self.color_curve = "#1F77B4"
        self.color_equation_button = Button(
            self.input_frame, bg=self.color_curve, width=1, command=self.select_colour_equation)
        self.color_equation_button.pack(anchor = "sw", pady = 5)

        
        #color de los puntos de los datos
        self.color_label = Label(self.text_frame, text="Color Points:")
        self.color_label.pack(pady=5)
        self.color_points = "#FF0000"
        self.color_button = Button(self.input_frame,
                                   bg=self.color_points, width=1,command=self.select_colour_points)
        self.color_button.pack(anchor ="w", pady = 5)

        self.marker_label = Label(self.text_frame, text="Marker: ")
        self.marker_label.pack(pady=5, anchor ="e")

        self.marker_list = ttk.Combobox(self.input_frame, width=15)
        self.marker_list.pack(pady=5)
        self.marker_list['values'] = self.marker_style

        #plot grid 
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
        self.grid.pack(anchor = "sw")


        # Lyne styles
        self.line_style_label = Label(
            self.text_frame, text="Line Style: ")
        self.line_style_label.pack(pady=5, anchor ="e")

        self.line_style = ttk.Combobox(self.input_frame, width=15)
        self.line_style.pack(pady=5)
        self.line_style['values'] = self.line_styles

        # Size Points
        self.size_label = Label(self.text_frame, text="Points size: ")
        self.size_label.pack(pady=5, anchor ="e")
        # Caja de entrada para el tamaño de los puntos
        self.size_var = DoubleVar()
        self.size_var.set(5.0)
        self.size_point = Spinbox(self.input_frame, from_=0.1,
                                  increment=0.1, to=5.0, width=7, textvariable=str(self.size_var))

        self.size_point.pack(pady=5)

        
        #-----------------------------------------------------
        # plot frame
        self.plot_frame = Frame(self.root)

        #create canvas
        self.fig = Figure(figsize = (12, 10), dpi = 100)
        #adding the subplot
        plot1 = self.fig.add_subplot()

        #containing the Matplotlib figure
        self.canvas = FigureCanvasTkAgg(self.fig, master = self.plot_frame)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.plot_frame)
        self.canvas.draw()
        #placing the canvas on the tkinter plot_frame
        self.plot_frame.pack(side=TOP,fill =BOTH, expand = True)
        self.canvas.get_tk_widget().pack(side = TOP, fill = X)
        
        #creating the Matplotlib toolbar
        self.toolbar.pack()
        self.toolbar.update()
        # button
        self.graph_button = Button(self.config_graph_frame, text="Graph", command=self.graph)
        self.graph_button.pack(pady = 10, side=BOTTOM)

        self.root.bind("<Configure>", self.resize)
        self.root.mainloop()

    def resize(self, event):
        if self.x_resolution == event.width:
            for label_el in self.text_frame.winfo_children():
                label_el.configure(pady = 5)

            for input_el in self.input_frame.winfo_children():
                if input_el != self.color_button:
                    print("sii")
                    input_el.pack(pady = 10)
            self.grid.pack(pady = 1)


    def import_data(self):

        self.path_file = filedialog.askopenfilename(initialdir="./", title="Select file", 
            filetypes=(("Excel file", "*.xlsx"), 
                       ("csv file", "*.csv"),
                       ("all files", "*.*")))
        self.path.set(self.path_file)
        if self.path_file != "":
            if self.path_file[-1] == "v":
                self.data_frame = pd.read_csv(self.path_file)
            else:
                self.data_frame = pd.read_excel(self.path_file)
            self.set_title_columns()

    def get_data(self):
        temp_x, temp_y = self.x_data.get(), self.y_data.get()
        self.data_frame.rename(columns ={self.x_data.get() : "X", self.y_data.get() : "Y"}, inplace=True)
        self.data = self.data_frame.to_dict("list")
        self.data_frame.rename(columns ={"X" : tempx, "Y" : tempy}, inplace=True)
        return self.data

    def set_title_columns(self):
        self.title_columns    = list(self.data_frame.columns)
        self.x_data['values'] = self.title_columns
        self.y_data['values'] = self.title_columns
    
    def select_colour_points(self):
        __, self.color_points = sc(title = "Color points")
        if self.color_points == None:
            self.color_points = "#FF0000"
        self.color_button.config(bg = self.color_points)
    
    def select_colour_equation(self):
        __ , self.color_curve = sc(title = "Curve color")
        if self.color_curve == None:
            self.color_curve = "#1F77B4"
        self.color_equation_button.config(bg = self.color_curve)
    
    def get_marker_style(self):
        return marker_style[self.marker_list.get()]

    def get_line_style(self):
        return line_style[self.line_style.get()]
    
    def graph(self):
        #data: dict(x:list, y:list)
        #marker: str
        newGr = gr(data       = self.get_data(),
                   title      = self.title.get(),
                   x_name     = self.x_name.get(),
                   y_name     = self.y_name.get(),
                   grid       = self.grid_value.get(),
                   color_pt     = self.color_points,
                   size_pt    = self.size_var.get(),
                   line_style = self.get_line_style(),
                   equation   = self.equation.get(),
                   domain     = self.domain.get(),
                   legend_eq  = self.legend_equation.get(),
                   color_eq   = self.color_curve,
                   marker     = self.get_marker_style()
                   )
        newGr.draw()

if __name__ == '__main__':
    main()
