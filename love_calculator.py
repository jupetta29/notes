print("Welcome to the Love Calculator!")

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names = name1.lower() + name2.lower()
t = names.count('t')
r = names.count('r')
u = names.count('u')
e = names.count('e')
l = names.count('l')
o = names.count('o')
v = names.count('v')
true = str(t + r + u + e)
love = str(l + o + v + e)
love_score = int(true + love)

if love_score < 10 or love_score > 90:
    print(f'Your score is {love_score}, you go together like coke and mentos.')
elif love_score > 40 and love_score < 50:
    print(f'Your score is {love_score}, you are alright together.')
else:
    print(f'Your score is {love_score}.')