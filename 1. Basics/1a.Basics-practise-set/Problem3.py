# Install an external module and use it to perform an operation of your interest. 

from faker import Faker

fake = Faker().email()

print (fake)