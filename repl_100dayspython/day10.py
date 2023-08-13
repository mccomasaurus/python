bill = float(input("What was the bill?: "))
number_of_people = int(input("How many people?: "))
tip = input("Was your service good, bad or excellent, or other (I'd like to choose my own tip percentage thank you) ")
if tip == "good":
  answer = ((.20 + 1) * bill) / number_of_people
  answer = round(answer,2)
  print("you all owe", answer)
elif tip == "bad":
  answer = ((.10 + 1) * bill) / number_of_people
  answer = round(answer,2)
  print ("you all owe", answer)
elif tip == "excellent":
  answer = ((.30 + 1) * bill) / number_of_people
  answer = round(answer,2)
  print ("you all owe", answer)
elif tip == "other":
  other_tip = float(input("what is the percent you'd like to tip? "))
  answer = (((other_tip / 100) + 1) * bill) / number_of_people
  answer = round(answer,2)
  print ("you all owe", answer)
else:
  print("please choose good, bad, excellent, or other as a tip option")
