class Inter:
    def __init__(self):
        print('hello')

    def yes(self):
        print('yes man')


class Extra(Inter):
    def __init__(self):
        Inter.__init__(self)
        print('okay')



    
p = Extra()
p.yes()
    