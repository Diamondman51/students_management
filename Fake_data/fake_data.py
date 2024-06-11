from faker import Faker

fake = Faker()

name_male = [(fake.name_male(), 'Male') for _ in range(50)]
name_female = [(fake.name_female(), 'Female') for _ in range(50)]
names = name_female + name_male
id = [fake.random_number(digits=20) for _ in range(100)]
classes = [f'Grade {fake.random_number(digits=1)}' for _ in range(100)]
birthday = [fake.birth_number() for _ in range(100)]
print(classes)
