# Ethan Lawrence
# Nov 11 2024
# zip

names = ['Alicia', 'Alexander', 'Connor']
ages = [17, 18, 17]
for name, age in zip(names, ages):
    print(f'{name} {age}')
print('')

lname = ['CLAPTON', 'WAYNE', 'SANTANA']
fname = ['Eric', 'Bruce', 'Carlos']
for lname, fname in zip(lname, fname):
    print(f'{lname} {fname}')
print('')

items = ['Corn flakes', 'Cocoa Puffs', 'Wheaties']
prices = [5.99, 6.75, 4.50]
for item, price in zip(items, prices):
    print(f'A box of {item} costs ${price:,.2f}')
print('')

students = ['Lucas', 'Keily']
schools = ['Interlochen', 'Elk Rapids']
countys = ['Grand Traverce County', 'Antrim County']
for student, school, county in zip(students, schools, countys):
    print(f'{student} lives near {school} in {county}')