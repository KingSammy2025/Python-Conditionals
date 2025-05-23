 print("Welcome to the neighbourhood survey!")

print("Answer the following questions to find out the type of neighbours we have")



print("Question 1: ")

quest1 = input("What is your full name? ")
print("Your full name is: " + quest1)
 

print("Question 2: ")

quest2 = input("What is your favorite color? ")
quest2_answer = quest2
print("Your favorite Color is: " + quest2)


print("Question 3: ")

quest3 = print("Do you prefer to 'make plans ahead of time' or 'go with the flow'? ")
quest3_A = print("A. Make plans ahead of time ")
quest3_B = print("B. Go with the flow" )
user_response3 = input()
  
while  user_response3 != "A" and user_response3 != "B":
  print("Select an option")
  user_response3 =  input()     
if user_response3 == "A":
    print("Your Choice: A")
elif user_response3 == "B":
    print("Your Choice: B")
    
    
    
print("Question 4: ")

quest4 = print("When interacting with a new person, do you prefer...")
quest4_A = print("A. Short and sweet introductions ")
quest4_B = print("B. Engaging in deeper conversations" )
quest4_C = print("C. Focusing on details and facts" )
quest4_D = print("D. Quickly creating a connection")
user_response4 = input()
while  user_response4 != "A" and user_response4 != "B" and user_response4 != "C" and user_response4 != "D":
  print("Select an option")
  user_response4 =  input() 
if user_response4 == "A":
    print("Your Choice: A")
elif user_response4 == "B":
    print("Your Choice: B")
elif user_response4 == "C":
    print("Your Choice: C")
elif user_response4 == "D":
    print("Your Choice: D")    
 

  
    
print("Question 5: ")

quest5 = print("When facing a challenge, do you typically...")
quest5_A = print("A. Focus on improving and finding the best solution")
quest5_B = print("B. Seek reassurance from others" )
quest5_C = print("C. Consider the impact on others" )
quest5_D = print("D. Refocus on what you can control")
user_response5 = input()
while  user_response5 != "A" and user_response5 != "B" and user_response5 != "C" and user_response5 != "D":
  print("Select an option")
  user_response5 =  input() 
if user_response5 == "A":
    print("Your Choice: A")
elif user_response5 == "B":
    print("Your Choice: B")
elif user_response5 == "C":
    print("Your Choice: C")
elif user_response5 == "D":
    print("Your Choice: D")



print("Your type of neighbour is... ")

if user_response3 == "B" or user_response4 == "A"  or user_response5 == "B":
      print("You are a Gentle friendly neighbour! ")
      
elif user_respomse3 =="A" or user_response4 == "A"  or user_response5 == "A":
       print("You are a strong independent neighbour! ")
       
else:
    print("You are a nice sweet neighbour!")       
 
print("Thanks for participating in this quiz!") 