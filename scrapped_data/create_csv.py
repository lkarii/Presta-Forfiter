import json
import csv
import random
import re

#TODO fix images and image link formatting
#TODO add sub-categories

cat_file = open('categories.json', encoding='UTF8')
cat_data = json.load(cat_file)
cat_file.close()

with open('categories.csv', 'w', encoding='UTF8', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=';')
    writer.writerow(["ID","Nazwa","Opis","Pozycja","Wyświetlane"])
    id = 3
    for i in range(len(cat_data)):
        writer.writerow([id, cat_data[i]['name'], "", id - 1, 1])
        id += 1

prod_file = open('products.json', encoding='UTF8')
prod_data = json.load(prod_file)
prod_file.close()

with open('products.csv', 'w', encoding='UTF8', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=';')
    writer.writerow(["Product ID","Obraz","Nazwa","Kategoria","Cena (netto)","Cena (brutto)","Ilość"])
    id = 1
    for i in range(len(prod_data)):
        if random.random() > 0.88:
            amount = 0
        else:
            amount = random.randint(1, 10)
        writer.writerow([id, "https://raw.githubusercontent.com/WallyS02/Presta-Forfiter/master/scrapped_data/images/" + re.sub(r'[&\'%,]', '', (prod_data[i]['name'].strip()).replace(" ", "-")) + "-BIG.jpg", prod_data[i]['name'].strip(), prod_data[i]['category'], (prod_data[i]['price'][:-3]).replace(" ", ""), prod_data[i]['price'][:-3].replace(" ", ""), amount])
        id += 1
