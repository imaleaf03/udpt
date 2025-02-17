from pickledb import PickleDB

# Initialize the database
db = PickleDB('my_db.db')
# Store a dictionary
db.set('user', {'name': 'Alice', 'age': 30, 'city': 'Wonderland'})
db.set('user2', {'name': 'Tinkerbell', 'age': 30, 'city': 'Wonderland'})
db.set('user3', {'name': 'Wendy', 'age': 30, 'city': 'Wonderland'})
# Retrieve and update it
db.remove('user2')
print(db.all())
db.save()