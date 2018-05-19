import csv

with open('/home/roger/Downloads/contatos.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print (row[0])
