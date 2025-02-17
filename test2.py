from pickledb import PickleDB

# Initialize the database
db = PickleDB('my_database.db')

# Add a key-value pair
db.set('greeting', 'Hello, world!')

# Retrieve the value
print(db.get('greeting'))  # Output: Hello, world!
# Add a new key-value pair
db.set('username', 'admin')

# Or shorthand
db['username'] = 'admin'

# Update an existing key-value pair
db.set('username', 'superadmin')
print(db.get('username'))  # Output: 'superadmin'

# Get the value for a key
print(db.get('username'))  # Output: 'superadmin'

# Like the set() method, you can use Python syntax sugar here as well
print(db['username']) # Output: 'superadmin'

# Attempt to retrieve a non-existent key
print(db.get('nonexistent_key'))  # Output: None

# Add multiple keys
db.set('item1', 'value1')
db.set('item2', 'value2')

# Retrieve all keys
print(db.all())  # Output: ['username', 'item1', 'item2']
# Remove a key-value pair
db.remove('item1')
print(db.all())  # Output: ['username', 'item2']
# Save the current state of the database
db.save()
print("Database saved successfully!")
