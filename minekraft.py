import pandas as pd
import math
import csv
import socket
import PIL.Image


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
                
        return int(most_common_choice)
        

    def send_message(self, message:str):
        # Création d'une socket pour communiquer sur un réseau
        # informatique en TCP
        ma_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connexion au serveur
        ma_socket.connect(("10.229.253.48", 4711))
        # Préparation et envoi de la requête selon le protocole MCPI
        requete = f"chat.post({message})\n"
        ma_socket.send(requete.encode())
        # Déconnexion du serveur
        ma_socket.close()


    def open_socket(self):
        # Création d'une socket pour communiquer sur un réseau
        # informatique en TCP
        self.ma_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connexion au serveur
        self.ma_socket.connect(("127.0.0.1", 4711))


    def close_socket(self):
        # Déconnexion du serveur
        self.ma_socket.close()

    def set_block(self, x:int, y:int, z:int, block:int):

        # Préparation et envoi de la requête selon le protocole MCPI
        requete = f"world.setBlock({x}, {y}, {z}, 35, {block})\n"

        self.ma_socket.send(requete.encode())


    def set_blocks(self, x1, y1, z1, x2, y2, z2, block_id=0, block_data=0):
        requete = f"world.setBlocks({x1}, {y1}, {z1}, {x2}, {y2}, {z2} {block_id}, {block_data})\n"

        self.ma_socket.send(requete.encode())


    def convert_to_grayscale(self, r, g, b):
        return r*0.3 + g*0.59 + b*0.11


    def poser_image(self, img_path:str):
        self.open_socket()
        image = PIL.Image.open(img_path)
        image.load()
        image.convert("RGB")
        for h in range(image.height):
            for w in range(image.width):
                pixel = image.getpixel((w, h))
                col = self.find_closest_brick_color(pixel[0], pixel[1], pixel[2], 5)
                print(w, h, col, pixel)
                if col != 0:
                    print(col)
                    z = self.convert_to_grayscale(pixel[0], pixel[1], pixel[2]) // 25
                    for e in range(int(z)):
                        self.set_block(w + 400, 200 - h, 70 + e, col)
                    self.set_block(w+0, 10-h, 0+int(z), col)

        self.close_socket()


susamongus = MinetestKNN()
susamongus.open_socket()
susamongus.open("minetest_colors.csv")
susamongus.poser_image("amongus.jpg")
#susamongus.set_blocks(-500, -500, -500, 1000, 1000, 1000)
print(susamongus.find_closest_brick_color(0, 0, 0, 23))