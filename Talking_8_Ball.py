import random

#will change these to take user input soon
name = "paul"
question = 'Can I get a buck'
answer = ''
random_number = random.randint(1, 12)
#print(random_number)
if random_number == 1:
  answer = 'Yes - definitely'
elif random_number == 2:
  answer = 'It is decidedly so'
elif random_number == 3:
  answer = 'Without a doubt'
elif random_number == 4:
  answer = 'Reply hazy, try again'
elif random_number == 5:
  answer = 'Ask again later'
elif random_number == 6:
  answer = 'Better not tell you now'
elif random_number == 7:
  answer = 'My sources say no'
elif random_number == 8:
  answer = 'Outlook not so good'
elif random_number == 9:
  answer = 'Very doubtful'
elif random_number == 10:
  answer = 'I dont think so'
elif random_number == 11:
  answer = 'Not Really'
elif random_number == 12:
  answer = 'You\'re messing with me'
else:
  answer = 'Error'

#if len(question) == 0:
  #print('Provide me an intriging question')

# print question if there is no name provided
if len(name) == 0 and len(question) >= 1:
  print('Question:', question)
#print name not very talkitive
elif len(name) >= 1 and len(question) == 0:
  print(name +', not very talkitive?')
#print name + question prompt
elif len(question) >= 1 and len(name) >= 1:
   print(name, "asks:", question)
#really messed up
else:
  print('anyone?')

if len(question) == 0:
  print('')
elif len(question) >= 1:
  print("Magic 8-Ball's answer:", answer )
else:
  print('')
