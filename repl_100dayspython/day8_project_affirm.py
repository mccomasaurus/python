print("AFFIRMATIONS CHALLANGE")
print("----------------------")
print()
name = input("Whats your name? ")
if name == "matt" or name == "Matt" or name == "matthew" or name == "Matthew" or name == "anelisse" or name == "Anelisse" or name == "Alina" or name == "alina":
  print("Hello",name,"!")
  mood = input("How are you feeling today on a scale from 1-10, with 1 being the worst and 10 being the best? ")
  if mood == "1" or mood == "2" or mood =="3":
    print("The sun will rise, and the sun will set, and you too will make it through this day. Keep your head up",name)
    improve_mood = input("Maybe we can do something to improve your mood. Would you like to go for a walk, take a nap, or eat? ")
    if improve_mood == "walk":
      print("Excellent lets go get our shoes!")
    elif improve_mood == "nap" or improve_mood == "take a nap":
     print("A good nap always helps me too!")
    elif improve_mood == "eat":
      print("Great I'm starving!") 
    else:
     print("Invalid option, please pick one of the 3 options listed ('run, nap, eat'")
  elif mood == "4" or mood == "5" or mood == "6":
    print("Well things could be worse, but it also sounds like they could be better. Don't worry things will improve",name)
  elif mood == "7" or mood == "8":
    print("Hey thats not bad look at you go")
  elif mood == "9" or mood == "10":
    print("Look at you go",name,"you are feeling fantastic!")
  else:
    print("thats not a number thats 1-10...try again",name)

