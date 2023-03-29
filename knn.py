import pandas as pd
import math

class MinetestKNN:
    def __init__(self, colors:list) -> None:
        self.colors = colors
        
        
    def open(self, csv_file:str):
        self.csv_data =  []
        with open(csv_file, "r") as f:
            for l in f:
                self.csv_data.append(l.split(';'))
                


    def find_closest_brick_color(self, red:int, green:int, blue:int, k:int):
        liste = []
        for col in self.csv_data:
            d = math.sqrt((red - int(col[1]))**2  + )
            
        
colors = [
    "lightgrey",
    "darkorange",
    "deeppink",
    "lightseagreen",
    "yellow",
    "limegreen",
    "lightcoral",            
    "darkgrey",
    "dimgrey",
    "lightseagreen",
    "darkviolet",
    "royalblue",
    "saddlebrown",
    "darkgreen",
    "red",
    "black",
]

susamongus = MinetestKNN(colors)
susamongus.open("minetest_colors.csv")
print(susamongus.find_closest_brick_color(2, 2, 2, 1))