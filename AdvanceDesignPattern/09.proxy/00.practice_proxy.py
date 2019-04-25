class SensitiveInfo:
    def __init__(self):
        self.users = ['nick', 'tom']
    
    def read(self):
        print("There are {} users: {}".format(len(self.users), '/'.join(self.users)))
    
    def add(self, user):
        self.users.append(user)
        print('Added user {}'.format(user))



def way_that_add_user_without_proxy():
    # claim a class with SensitiveInfo directly
    a = SensitiveInfo()
    # show the users in lists
    a.read()
    # add another user to users
    a.add("jim")
    # then check list again
    a.read()

# define another class to avoid store sensitive data
class Info:
    def __init__(self):
        self.protected = SensitiveInfo()
        self.secret = '0000'
    
    def read(self):
        self.protected.read()
    
    def add(self, user):
        sec = input('What is the secret?')
        self.protected.add(user) if sec == self.secret else print("That is wrong")
    

def way_that_add_user_with_proxy():
    # claim a class user with proxy class
    a = Info()
    a.read()

    # add another user
    a.add("jimmy")
    a.read()


if __name__ == "__main__":
    print("enter a user directly is passwordless but dangerous")
    way_that_add_user_without_proxy()
    print("enter a user with proxy need to access password")
    way_that_add_user_with_proxy()