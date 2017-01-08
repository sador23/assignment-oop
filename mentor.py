from db import Database

class Mentor():
    def __init__(self, raw_data):
        self.id = raw_data[0]
        self.first_name = raw_data[1]
        self.last_name = raw_data[2]
        self.nick_name = raw_data[3]
        self.phone_number = raw_data[4]
        self.email = raw_data[5]
        self.city = raw_data[6]
        self.favourite_number = raw_data[7]

    @staticmethod
    def get_all():
        return Database.get_mentors()

    # Return the 2 name property of all the mentors
    # returns: list of dictionaries
    # example: [{
    #    first_name: 'Bill',
    #    last_name: 'Wilkinson'
    # }, ...]
    
    @classmethod
    def _1_list_mentors(cls):
        mentors = cls.get_all()
        miskolc_list=[]
        for i in range(len(mentors)):
            miskolc_list.append({"first_name":mentors[i].first_name,"last_name":mentors[i].last_name})
        return miskolc_list

    # Return the nick_name property of all the mentors located in Miskolc
    # returns: list of dictionaries
    # example: [{
    #    nick_name: 'Billy'
    # }, ...]
    @classmethod
    def _2_list_mentors_from_miskolc(cls):
        mentors = cls.get_all()
        miskolc_list=[]
        for i in range(len(mentors)):
            if mentors[i].city=="Miskolc":
                miskolc_list.append({"nick_name":mentors[i].nick_name})
        return miskolc_list

    # Return the highest favourite number of all mentors
    # returns: integer
    # example: 927
    @classmethod
    def _3_greatest_favourite_number(cls):
        mentors = cls.get_all()
        maximum=0
        for i in range(len(mentors)):
            if mentors[i].favourite_number !=None and int(mentors[i].favourite_number)>maximum:
                maximum = int(mentors[i].favourite_number)
        return maximum
