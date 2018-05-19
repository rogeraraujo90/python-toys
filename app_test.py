import csv
import urllib.request, json
import time
from person import Person
from urllib.error import HTTPError

req = urllib.request.Request('https://api.fullcontact.com/v3/person.enrich')
req.add_header('Authorization', 'Bearer CvIRCOBjXDYH9jPB7jTE0bQGn3OydhlM')

personArray = []
with open('/home/roger/Downloads/contatos.csv') as csvfile:
    fileReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for email in fileReader:
        data = json.dumps({
            "email": email[0],
            }).encode('utf')

        try:
            response = urllib.request.urlopen(req,data)
            string = response.read().decode('utf-8')
            json_obj = json.loads(string)

            fullName = json_obj['fullName'] if 'fullName' in json_obj else None
            location = json_obj['location'] if 'location' in json_obj else None
            ageRange = json_obj['ageRange'] if 'ageRange' in json_obj else None
            gender = json_obj['gender'] if 'gender' in json_obj else None
            organization = json_obj['organization'] if 'organization' in json_obj else None
            age = json_obj['age'] if 'age' in json_obj else None
            employment = json_obj['employment'] if 'employment' in json_obj else None
            facebook = json_obj['facebook'] if 'facebook' in json_obj else None
            linkedin = json_obj['linkedin'] if 'linkedin' in json_obj else None

            person = Person(fullName, location, ageRange, gender, organization, age, employment, facebook, linkedin)

            personArray.append(person)

            print('Person saved')
            time.sleep(5)

        except HTTPError as e:
            print('Not data found for email: ', email[0])
            time.sleep(5)

        
with open('people_data.csv', 'w') as csvfile:
    fieldnames = ['full_name', 'location', 'age_range', 'gender', 'organization', 'age', 'employment', 'facebook_profile', 'linkedin_profile']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for person in personArray:
        writer.writerow({'full_name': person.fullName, 'location': person.location, 'age_range': person.ageRange, 'gender': person.gender, 'organization': person.organization, 'age': person.age, 'employment': person.employment, 'facebook_profile': person.facebook, 'linkedin_profile': person.linkedin})

    
    
