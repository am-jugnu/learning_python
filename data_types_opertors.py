#Python is case sensitive.

#Spacing is important.

#Use error messages to help you learn.
# + Addition
# - Subtraction
# * Multiplication
# / Division
# % Mod (the remainder after dividing)
# ** Exponentiation 
# // Divides and rounds down to the nearest
# this example we use the string "\n" as the separator so that there is a newline between each element.
# We can also use other strings as separators with .join. Here we use a hyphen.
# A helpful method called append adds an element to the end of a list.
# A tuple is another useful container. It's a data type for immutable ordered sequences of elements.
# They are often used to store related pieces of information. Consider this example involving latitude and longitude:
# Chandrayaan was launched on : 22 July 2019
x = 'fight'
y = 'me'
print(x + " " + y)
x = "shridhan"
print(x * 3)
x = '"I like mangoes but not apple"'
print(x)
selfmade_car = len("selfmade")
age = 13
is_teen = age > 12 and age < 20
print(is_teen)
x = 'I love Soha but not "Farah" and "Muskan"'
print(x)
y = "2+2 makes 4 why don't they make 5"
print(y)
f = 4>5
print(f)
g = '"i like mangoes, rather i love mongoes because mangoes\' taste is really very fine"'
print(g) 
v = "soha i love you"
print(5*v)
Soha_is_my_love = len("soha")
print(Soha_is_my_love)
Shridhan_want_to_marry_Soha = len("Shridhan Soha")
print(Shridhan_want_to_marry_Soha)
ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'
print(ford_quote)
print(type(34))
print(type(67.4))
print(type("46"))
house_number = 3
street_name = "sarai tareen"
district_name = "sambhal"
address = str(house_number) + " " + street_name + " " + district_name
print(address)
mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"
weekly_sale = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)
weekly_sale = str(weekly_sale )
print("This week's total sales: " + weekly_sale)
print("soha is my love".title())
name = "SDFFFA"
print(name. islower())
x = "dog bark"
y = "your"
print("Does {} {}?" .format(y , x))
s = "Soha is my love"
print(s .split())
print("farha, muskan, aashi, farha".count('farha'))
print( 5 % 2)
print( 4 // 3)
print( 4 ** 4)
print( 4/ 3 ) 
print( 3 *2)
print( 5 - 3)
print( 5 + 3)
print(float("45"))
f = "fight"
d = "with me"
print("Can you {} {}" .format( f , d ))
bal_vidya_mandir = len("bal vidya")
print(bal_vidya_mandir )
print("Gaurav has {} mangoes" . format(45))
print("farha, muskan,aashi, kushi, mahima," .count('farha'))
g  = 4>=4
print(g) 
my_str = "this is very deep hole."
print(my_str.split())
my_str = "this is very deep hole."
print(my_str.split(" " , 1))
my_str = "this is very deep hole."
print(my_str.split(None,5))
v = '34'
print('v-=6')
love = "India"
days = [ 'monday', 'tuesday', 'wednusday' , 'thuraday' , 'friday' , 'saturday' , 'sunday']
print(len(love), len(days))
print(days[0])
print(days[1])
print(days[3])
print(days[2])
print(days[-2:])
first_half = days[:3]
print(first_half)
q1 = days[0:2]
print(q1)
second_half = days[3:]
print(second_half)
friendship = "Talha is my best friend"
print('alha' in friendship, 'alha' not in friendship)
days[3] = 'January'
print(days)
books = ['maths' , 'science' , 'english' , 'social science']
kiatabe = books
print(books)
print(kiatabe)
books[0] = 'hindi'
print(books)
print(kiatabe)
c = [3,4,3,4,5,3,4,3,4,45,37,7,77,5,5565,5,5,6]
print(max(c))
print(min(c))
print(sorted(c))
print(sorted(c, reverse = True))
t = [ 'Soha' , 'Fehmi' , 'Gousiya' , 'Hafsha' , 'Sadaf' , 'Shreen']
print(max(t))
print(min(t))
print(sorted(t))
print(sorted(t , reverse=True))
names = "\n" .join(["Soha" , "Shridhan"])
print(names)
name= "-" .join(["Soha" , "Mobeen"])
print(name)
my_love = ['Family' , 'Country' , 'Adventure']
my_love.append('Soha')
print(my_love)
y = 's'
print(y)
print(t[:2])
length, width, height = 37,34,766
print("Dimensions are {}x{}x{}" .format(length, width, height ))
friends = { "Yashdeep" , "Talha" , "Asad" , "Sarwer" ,"Keshav"}
print("Gaurav" in friends, "Talha" not in friends)
friends.add("Gaurav")
print(friends)
print(friends.pop())
c = [344,344,34,2,2,3,2,4,2,4,2,4,2,4,2,3]
v = set(c)
print(v)
print(636*4)
elements = { 'calcium' : 20 , 'Sodium':11, 'Neon': 10}
elements[ ' Potassium'] = 19
print(elements)
Cities = { 'Shanghai' : 17.8 , 'Istanbul' : 13.3 , 'Karachi' : 13.0, 'Mumbai' : 12.5}
print(Cities)
print(Cities)
animals = {'dogs': [20, 10, 15, 8, 32, 15], 'cats': [3,4,2,8,2,4], 'rabbits': [2, 3, 3], 'fish': [0.3, 0.5, 0.8, 0.3, 1]}
print(animals)
print(animals['dogs'][3])
elements = { 'Hydrogen' :{ 'atomic numbber' :1,
                           'atomic mass' : 1,
                           'symbol' : "H"},
           "Helium" :{'atomic numbber' : 2,
                      'atomic mass':4,
                       'symbol' : "He"}
                    }
print(elements)
print(elements["Helium"])
print(elements["Helium"]['symbol'])