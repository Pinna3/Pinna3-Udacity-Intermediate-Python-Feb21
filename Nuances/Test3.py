# This one's a bit different, representing an unusual (and honestly,
# not recommended) strategy for tracking users that sign up for a service.

class User:
    # An (intentionally shared) collection storing users who sign up for some hypothetical service.
    # There's only one set of members, so it lives at the class level!
    members = set()
    def __init__(self, name):
        self.name = name
        # self.members = set()  # Not signed up to begin with.
    def sign_up(self):
        self.members.add(self.name)

# Change the code above so that the following lines work:
#
if __name__ == '__main__':
    sarah = User('sarah')
    heather = User('heather')
    cristina = User('cristina')
    print(User.members)  # {}
    heather.sign_up()
    cristina.sign_up()
    print(User.members)  # {'heather', 'cristina'}
