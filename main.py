#this program is named CraFinder for a company named AutoCountry.
#the program enables users to navigate through the menu options.

#start your loop 
while True:

   print()
   print("*******************************")

   print("AutoCountry Vehicle Finder v0.4")
   print("*******************************")
# define each element in the menu, and return each element (choice-num1, choice-num2, choice-num3,choice_num4, choice_num5)
   def choice_num1():
    return("1. PRINT all Authorized Vehicles") 
   def choice_num2():
    return("2. SEARCH for Authorized Vehicle")
   def choice_num3():
    return("3. add authorized vehicle")
   def choice_num4():
    return("4. DELETE Authorized Vehicle")
   def choice_num5():
    return("5. Exit")

#allow the user to enter a number from 1 to 5 of the menue after you call your menu elements. 
#use "\n" to print the menu's elements in seperate lines.
   user_input=input("Please Enter the following number below from the following menu:"+"\n"+ choice_num1() + "\n" + choice_num2() + "\n" + choice_num3() + "\n" + choice_num4() + "\n" + choice_num5() + "\n")

  # start your if statement to direct the user to the correct path after the user chooses a number from the menu.

   if user_input == "1":
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
# this program will end the current iteration of the and start from the top of the loop, when the users input is 1.

# this program will read the "test.txt" file and print the contents of the file.

    with open("test.txt") as test:
      content_read = test.read()
      print(content_read)

    continue

   elif user_input=="5":
# this program will end after the user input 5. 

      print("Thank you for using the AutoCountry Vehicle Finder, good-bye! " )

      break
    