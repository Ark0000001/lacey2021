print('\n020')
name=input('name?: ')
print('name len: ', len(name))

print('\n021')
name=input('name?: ')
surname=input('surname?: ')
total=name+" "+surname
print('name + surname: ', total.title())

print('\n022')
name=input('name?: ')
surname=input('surname?: ')
total=name+" "+surname
print('name + surname: ', total.title())

print('\n023')
stih=input('stih?: ')
start=int(input('start?: '))
end=int(input('end?: '))

print('range: \n', stih[start:end])

print('\n024')
name=input('name?: ')
print('name upper: ', name.upper())

print('\n025')
name=input('name?: ')
if len(name)<5:
    surname=input('surname?: ')
    print(str.upper(name+surname))
else:
    print(name.lower())

print('\n026')
word=input('word?: ')
n=word[0]
if n != "a" and n != "e" and n != "i" and n != "o" and n != "u":

    print(str.lower(word[1:]+n+'ay'))
else:
    print(str.lower(word+'way'))






