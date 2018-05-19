import facebook

FB_APP_TOKEN = '366513340510347|xEDIJxxvB2N28q70ZTMFWWWnUNU'
USER_TOKEN = 'EAACEdEose0cBADCz2aHRl2OICfubOzFgapvY6RI4Mys0AZAz5AgFuMFBwzK6lFE3dEv8lZBVQX1LvRvpim0Txn9HERkwhErk2ZB8puifZA4JA5Typ0ZCjCYRSDdmVsl3bnsRu760kwA8cXjUeav1mAJb1jPTqk2dqK6zFJH8RuqRh6ohyErwvAhzrixwkuJmcfW034Af6OwZDZD'
graph = facebook.GraphAPI(access_token=USER_TOKEN, version = '2.7')
events = graph.get_object('100000542029347', fields='email,id,location,age_range,first_name,gender,last_name,name,verified')

print(events)
