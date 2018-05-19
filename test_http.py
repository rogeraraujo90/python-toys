import urllib.request, json
from urllib.error import HTTPError

req = urllib.request.Request('https://api.fullcontact.com/v3/person.enrich')
req.add_header('Authorization', 'Bearer cpJpgKpKk9ANa9UmDwbcjEhxmbjCSllg')
data = json.dumps({
    "email": "Rogeralves_90@hotmail.com",
}).encode('utf')

try:
    response = urllib.request.urlopen(req,data)
    string = response.read().decode('utf-8')

    print(string)
    
   # json_obj = json.loads(string)

    #print(json_obj.keys())
    #print(json_obj['test'] if 'test' in json_obj else 'None')
    #print(json_obj['location'])
    #print(json_obj['ageRange'])
    #print(json_obj['gender'])
    #print(json_obj['organization'])
    #print(json_obj['details']['education'])

    #for formation in json_obj['details']['education']:
     #   if(formation.get('degree')):
     #       print(formation['degree'])

    #print(json_obj['details']['age'])
    #print(json_obj['details']['employment'])
    #print(json_obj['facebook'])
    #print(json_obj['linkedin'])

except HTTPError as e:
    print ('Erro')
    print(e.read())
    print(e.code)
