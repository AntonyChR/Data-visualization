import numpy as np
import matplotlib.pyplot as plt
import Modules.Features as ft


class graph():
    def __init__(self, **kargs):
        #data: {x:list, y:list}
        self.args = kargs
        self.font = {"fontname": "Times New Roman", "size": 14}
        self.x = None
        self.y = None
    

    def insert(self):
        functions = ["exp", "ln", "sin", "cos",
                     "tan", "arctan", "arcos", "sec", "arcsin"]
        for fun in functions:
            i = self.args["equation"].find(fun)
            if i != -1:
                self.args["equation"] = self.args["equation"][:i] + "np." + self.args["equation"][i:]

    def draw(self):
        print(self.args)
        # if self.args["equation"] != "": 
        #     self.insert()
        #     if self.args["domain"] != "":
        #         a, b = self.args["domain"].split(":")
        #     else:
        #         a, b = self.x[0], self.x[-1]

        #     dom  = np.linspace(float(a), float(b), num = 100)
        #     ran  = [eval(self.args["equation"]) for x in dom]
        #     plt.plot(dom, ran,self.args["color_eq"], label=self.args["legend_eq"])
            
        # print(self.args["marker"])
        # plt.plot(self.x, self.y, linestyle = self.args["line_style"])   
        # plt.plot(self.x, self.y, "-o",color = self.args["col"], markersize=self.args["size"])
        # plt.title(self.args["title"], self.font)
        # plt.xlabel(self.args["xtitle"], self.font)
        # plt.ylabel(self.args["ytitle"], self.font)
        # plt.grid(self.args["grid"])

        # if self.args["legend_eq"] != "":
        #     plt.legend(loc = "best")

        # plt.show()
