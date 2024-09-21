import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    f1 = open(input_file_name)
    f2 = open(output_file_name, 'w')
    reader = csv.reader(f1)
    password_with_hash_password = {}
    for row in reader:
        user_name = row[0]
        for password in range(0,10000):
            hashed_password = hashlib.sha256(b'%i'%password).hexdigest()
            if hashed_password == row[1]:
                f2.write(user_name+','+str(password)+'\n')