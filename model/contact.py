from sys import  maxsize

class Contact:

    # def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None, home=None, mobile=None, work=None, fax=None, email=None, email2=None, email3=None, homepage=None, byear=None, ayear=None, address2=None, phone2=None, notes=None, id = None):
    def __init__(self, id=None, firstname=None, lastname=None, notes=None, home=None, mobile=None, work=None, phone2=None ):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.notes = notes
        self.home = home
        self.mobile = mobile
        self.work = work
        self.phone2=phone2
        # self.middlename = middlename
        # self.nickname = nickname
        # self.title = title
        # self.company = company
        # self.address = address

        # self.fax = fax
        # self.email = email
        # self.email2 = email2
        # self.email3 = email3
        # self.homepage = homepage
        # self.byear=byear
        # self.ayear=ayear
        # self.address2=address2



    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname,self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize