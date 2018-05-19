class Person(object):
    fullName = ""
    location = ""
    ageRange = ""
    gender = ""
    organization = ""
    age = ""
    employment = ""
    facebook = ""
    linkedin = ""

    def __init__(self, fullName, location, ageRange, gender, organization, age, employment, facebook, linkedin):
        self.fullName = fullName
        self.location = location
        self.ageRange = ageRange
        self.gender = gender
        self.organization = organization
        self.age = age
        self.employment = employment
        self.facebook = facebook
        self.linkedin = linkedin
