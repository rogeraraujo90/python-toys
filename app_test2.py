import csv
import urllib.request, json
import time
from person import Person
from urllib.error import HTTPError

req = urllib.request.Request('https://api.fullcontact.com/v3/person.enrich')
req.add_header('Authorization', 'Bearer CvIRCOBjXDYH9jPB7jTE0bQGn3OydhlM')

personArray = []
with open('/home/roger/Downloads/contatos3.csv') as csvfile:
    fileReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for email in fileReader:
        data = json.dumps({
            "email": email[0],
            }).encode('utf')

        try:
            response = urllib.request.urlopen(req,data)
            string = response.read().decode('utf-8')
            personData = email[0] + ": " + string
            personArray.append(personData)
            print('Person saved')
            time.sleep(10)

        except HTTPError as e:
            if (e.code == 404):
                print('Not data found for email: ', email[0])
                time.sleep(10)
            else:
                if (e.code == 400):
                    print('Blacklist case: ', email[0])
                    time.sleep(10)
                else:
                    print('Erro')
                    print(e.read())
                    break

        
with open('people_data.csv', 'w') as csvfile:
    fieldnames = ['data']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for person in personArray:
        writer.writerow({'data': person})

    
    
