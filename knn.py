import pandas as pd
import math
import csv

class MinetestKNN:
    def __init__(self):
        pass
        
        
    def open(self, csv_file:str):

        with open('minetest_colors.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=';')
            self.csv_data = []
            for row in csv_reader:
                self.csv_data.append(row)



    def find_closest_brick_color(self, red:int, green:int, blue:int, k:int):
        liste = []
        for col in self.csv_data:
            d = math.sqrt((red - int(col["red"]))**2  + (green - int(col["green"]))**2 + (blue - int(col["blue"]))**2)
            liste.append((col, d))
        liste.sort(key=lambda x:x[1])
        liste = liste[0:k]
        
        choice_counts = {}
        most_common_choice = None
        highest_count = 0

        for d, _ in liste:
            choice = d['choice']
            if choice in choice_counts:
                choice_counts[choice] += 1
            else:
                choice_counts[choice] = 1
            if choice_counts[choice] > highest_count:
                most_common_choice = choice
                highest_count = choice_counts[choice]
                
        return self.colors[highest_count-1]
        
       

susamongus = MinetestKNN()
susamongus.open("minetest_colors.csv")
print(susamongus.find_closest_brick_color(0, 0, 0, 23))