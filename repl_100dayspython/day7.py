print("FAKE FAN FINDER")
print("---------------")
print()
team = input("Whats your favorite NFL team? ")
if team == "Steelers":
  print("Yeah now thats what I'm talking about!")
  player = input("Who is your favorite player? ")
  if player == "Pickett":
    print("The hometown boy")
    question = input("Do you think he's improved a lot since last season? ")
    if question =="yes":
      print("I think so too!")
    else:
      print("I think he will do well")
  elif player == "Watt":
    print("I hope he can stay healthy through the full season")
    question = input("Do you You think his brother come out of retirement to play with his brother? ")
    if question =="yes":
      print("I think so too!")
    else:
      print("He's earned his retirement!")
  elif player == "Harris":
    print("The beast Najee Harris")
    question = input("Do think Steelers will do more of a RB by committee? ")
    if question == "yes":
      print("I think so too!")
    else:
      print("I'd like to see them use the other running backs more to keep Harris fresh")
  elif player == "Fitzpatrick":
    print("The speedster")
    question = input("Do you think he was worth the 1st round pick? ")
    if question == "yes":
      print("I think so too!")
    else:
      print("I think he was definately worth the pick trade!")
  else:
    print("I think we will have a good season this year")
elif team == "Browns":
  print("Are the Cleveland Clowns still a team?")
elif team == "Bengals":
  print("It's been a long time for Begals fans, I'm glad to see they have a team now")
elif team == "Cowboys":
  print("I'd rather watch their cheerleaders then their players")
else:
  print("good luck this season!")
