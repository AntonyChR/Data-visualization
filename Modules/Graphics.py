import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import Modules.Features as ft


class graph():

    def __init__(self, path,    title, xtitle,    ytitle,   rej, col,
                 line_style, size, ecuation, domain, legend_ec, color_ec, title_x, 
                 title_y, marker_):

        self.path       = path
        self.title      = title
        self.xtitle     = xtitle
        self.ytitle     = ytitle
        self.rej        = rej
        self.col        = col
        self.size       = size
        self.domain     = domain
        self.legend_ec  = legend_ec
        self.color_ec   = color_ec
        self.ecuation   = ecuation
        self.title_x    = title_x
        self.title_y    = title_y
        self.line_style = "None" if line_style == "" else ft.line_style[line_style]
        self.marker     = ft.marker_style[marker_] if marker_ != "" else "o"
        self.font       = {"fontname": "Times New Roman", "size": 14}

        self.x = 1
        self.y = 1


    def get_data(self):
        #v: csv else excel
        if self.path[-1] == "v":
            data = pd.read_csv(self.path)
        else:
            data = pd.read_excel(self.path)

        self.x = list(data[self.title_x])
        self.y = list(data[self.title_y])

    def insert(self):
        funciones = ["exp", "ln", "sin", "cos",
                     "tan", "arctan", "arcos", "sec", "arcsin"]

        for fun in funciones:
            i = self.ecuation.find(fun)
            if i != -1:
                self.ecuation = self.ecuation[:i] + "np." + self.ecuation[i:]

    def draw(self):

        if self.ecuation != "": 
            self.insert()
            if self.domain != "":
                a, b = self.domain.split(":")
            else:
                a, b = self.x[0], self.x[-1]

            dom  = np.linspace(float(a), float(b), num = 100)
            ran  = [eval(self.ecuation) for x in dom]
            plt.plot(dom, ran, label=self.legend_ec)
            

        plt.plot(self.x, self.y, linestyle = self.line_style)   
        plt.plot(self.x, self.y, marker = self.marker,linestyle = "None",color = self.col, markersize=self.size)
        plt.title(self.title, self.font)
        plt.xlabel(self.xtitle, self.font)
        plt.ylabel(self.ytitle, self.font)
        plt.grid(self.rej)

        if self.legend_ec != "":
            plt.legend(loc = "best")

        plt.show()
