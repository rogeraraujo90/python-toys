import http.client

c = http.client.HTTPSConnection("www.facebook.com")
c.request("GET", "/luizsotero")
response = c.getresponse()
print (response.status, response.reason)
data = response.read()
print (data)
       
