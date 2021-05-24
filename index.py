import random #importing a random module that will select the random choices.
reader_name=input("What is your name?")
print("Hello "+reader_name+","+ "Let me tell you a secret,")

# Storing random data into lists to create the story.
when = ['A long time ago', 'Yesterday', 'Before you were born', 'Before you were born']
who = ['Michelle','Jeannine','Loyce','Esther','Marie','Mary','Catherine','Grace','zillah','Irene','Gilly',
'Mandek','Janet','Sandra','Beldine','Linda','Samantha','Caroline','Jane','Wato','Akal','Diana','Aisha','Babra']
went = ['Y Combinator headquarters', 'Sahara desert', 'Somalia', 'Iraq','AkiraChix','the cookie jar','the hanging lines',
'the kitchen']
what = ['to eat the cakes', 'to fight for justice', 'to steal ice cream', 'to dance','to pitch her business',
'to ice skate','to fetch water','to learn how to code','to eat all the cookies','to play kati','to test her new car',
'to steal chapati','to give a motivational speech']

#combining elements from the choices to make a story.
print(random.choice(when) + ', ' + random.choice(who) + ' went to ' + random.choice(went) + ' ' + random.choice(what) + '.')