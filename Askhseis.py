"""
important pages
the pages mentioned below are for reference as per the files total pages, not as per the printed numbering pages
21 - basic printing
26 - if statements
32,35 - strings
39 - maths
44 - for loops
48,49 - while loops
54 - Random
66 - 69 - Tuples, Lists and Dictionaries
75 - 76 - More String Manipulation
80 - 81 - Numeric Arrays
87 - 89 - 2D lists and Dictionaries
94 - 95 - Reading and Writing to a Text File
99 - 102 - Reading and Writing to a .csv File
"""

import math
import random
from array import *
#from decimal import Decimal, ROUND_UP, ROUND_HALF_UP #to address the float decimals round error
from decimal import *
import csv

def askhsh_1():
    name = input("Give me your first name please: ")
    print("Hello",name)

def askhsh_2():
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    print("Hello",first_name,last_name)

def askhsh_3():
    print("What do you call a bear with no teeth?\nA gummy bear!")

def askhsh_4():
    num_one = int(input("Give me a number: "))
    num_two = int(input("Give me another number to add on the first one: "))
    print("The summary of",num_one,"and",num_two,"is",num_two+num_one)

def askhsh_5():
    print("Now let's try something a little bit more trickier\nYou will give me 3 numbers")
    print("The first two will be added and the sum of them will be multiplied by the third number")
    num_one = int(input("Give me the first number: "))
    num_two = int(input("Give me the second number: "))
    num_multi = int(input("Give me the third number which we will multiply by it:"))
    print(
        "("+str(num_one)+"+"+str(num_two)+")*"+str(num_multi)+"=",((num_one+num_two)*num_multi)
    )

def askhsh_6():
    pizza_full = int(input("How many slices did the pizza had? "))
    pizza_eat = int(input("And how many pizza slides did you ate? "))
    pizza_left = pizza_full - pizza_eat
    print("The pizza had "+str(pizza_full)+" slices, and you ate "+str(pizza_eat)+" of them.\nNow there are "+str(pizza_left)+" pizza slices left.")

def askhsh_7():
    name = input("What is your name? ")
    age = int(input("and what is your age? "))
    print(name,"on your next birthday you will be "+str(age+1))

def askhsh_8():
    billys = float(input("How much is the bill? "))
    people = int(input("and how many of you are in the table? "))
    to_be_paid = billys / people
    print("the bill is "+str(billys)+ " and since you are "+str(people)+" people in the table, each one of you should pay "+str(to_be_paid) +" euros.")

def askhsh_9():
    days = int(input("Give a number of days, to calculate how many hours, minutes and seconds exist in them: "))
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    print(days,"Days contain",hours,"hours,",minutes,"minutes and",seconds,"seconds!")

def askhsh_10():
    print("This is a kilograms to pounds converter")
    kilos = float(input("Give me some weight in kilos: "))
    pounds = kilos * 2.204
    print(kilos,"kilos are equal to",pounds,"pounds!")

def askhsh_11():
    major = int(input("Give me a number above 100: "))
    minor = int(input("Give me a number below 10: "))
    times_in = major / minor
    print("Number "+str(minor)+" goes in number "+str(major)+" aproximately "+str(times_in)+ " times."  )

def askhsh_12():
    num_one = int(input("Give me a number: "))
    num_two = int(input("Give me a number: "))
    if num_one > num_two:
        print(num_two , num_one)
    else:
        print(num_one , num_two)

def askhsh_13():
    number = int(input("Please give a number under 20: "))
    if number < 20:
        print("Thank you!")
    else:
        print("The number you have gives is too high.")

def askhsh_14():
    number = int(input("Give a number between 10 and 20, inclusive: "))
    if number<10 or number>20:
        print("Incorrect answer.")
    else:
        print("Thank you!")

def askhsh_15():
    users_colour = input("Please enter your favourite colour: ")
    if users_colour == "RED" or users_colour == "Red" or users_colour == "red":
        print("I like red too!")
    else:
        print("I don't like",users_colour,", i prefer red.")

def askhsh_16():
    rainy = input("Is it raining? ").lower()
    windy = input("Is it windy? ").lower()
    if rainy == "yes" and windy == "yes":
        print("It's too windy for an umbrella!")
    elif rainy == "yes" and windy != "yes":
        print("Take an umbrella.")
    elif rainy != "yes" and windy != "yes":
        print("Enjoy your day.")

def askhsh_17():
    age = int(input("What is your age? "))
    if age >= 18:
        print("You can vote.")
    elif age == 17:
        print("You can learn to drive.")
    elif age == 16:
        print("You can buy a lottery ticket.")
    elif age <= 15:
        print("You can go for trick-or-treat")

def askhsh_18():
    users_number = int(input("Please give me a number between 10 and 20: "))
    if users_number < 10:
        print("The number given is too low.")
    elif users_number >= 10 and users_number <= 20:
        print("Correct.")
    elif users_number > 20:
        print("Too high.")

def askhsh_19():
    users_number = int(input("Please give a number from 1 through 3: "))
    if users_number  == 1:
        print("Thank you.")
    elif users_number == 2:
        print("Well done.")
    elif users_number == 3:
        print("Correct")
    else:
        print("Error message")

def askhsh_20():
    name = input("Please enter your first name: ")
    num_of_letters = len(name)
    print("Your first name",name+", contains",str(num_of_letters),"letters")

def askhsh_21():
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    full_name = first_name + " " + last_name
    print("Your full name is: "+full_name)

def askhsh_22():
    first_name_lower = input("Please enter your first name in lowercase: ")
    last_name_lower = input("Please enter your last name in lowercase: ")
    full_name_upper = first_name_lower.capitalize() + " " + last_name_lower.capitalize()
    print("Your name is:",full_name_upper)

def askhsh_23():
    rhyme = input("Please insert a rhyme: ")
    starting_number = int(input("Give me a starting number: "))
    ending_number = int(input("Give me a ending number: "))
    cropped_text = rhyme[starting_number:ending_number]
    print(cropped_text)

def askhsh_24():
    any_word_lower = input("Enter any word: ")
    any_word_upper = any_word_lower.upper()
    print("The word you entered in uppercase is:",any_word_upper)

def askhsh_25():
    first_name = input("Please enter your first name: ")
    if len(first_name) <= 5 :
        last_name = input("Please enter your last name:")
        full_name = (first_name+last_name).upper()
    else:
        full_name = first_name.lower()
    print(full_name)

def askhsh_26():
    consonants = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
    word = input("type a word to translate it to pig latin: ").lower()
    if word[0:1] in consonants:
        new_word = word[1:] + word[0:1] + "ay"
    else:
        new_word = word + "way"
    print("The word",word,"in \"Pig Latin\" is "+new_word)

def askhsh_27():
    users_number = float(input("Give a number with lots of decimal places (separate decimal with the dot): "))
    multi2 = users_number * 2
    print("If we multiply",users_number,"by 2, we will get:",multi2)

def askhsh_28():
    users_number = float(input("Give a number with lots of decimal places (separate decimal with the dot): "))
    multi2 = users_number * 2
    rounded = round(multi2,2)
    print("If we multiply",users_number,"by 2 and round it, we will get:",rounded)

def askhsh_29():
    users_number = int(input("Please give a number that is bigger than 500: "))
    root_of_users_number = math.sqrt(users_number)
    print("The square root of",users_number,"is",round(root_of_users_number,2))

def askhsh_30():
    print(round(math.pi,5))

def askhsh_31():
    radius_of_circle = float(input("Please enter the circle's radius (cm) : "))
    circles_area = math.pi * (radius_of_circle ** 2)
    print("A circle with a radius of",radius_of_circle,"cm will have an area of",circles_area,"cm^2")

def askhsh_32():
    cylinders_radius = float(input("Give the radius of the cylinder: "))
    cylinders_depth = float(input("Give the depth of the cylinder: "))
    circle_area = math.pi * (cylinders_radius ** 2)
    total_volume = circle_area * cylinders_depth
    print("A cylinder with a radius of",cylinders_radius,"and a depth of",cylinders_depth,"will have a total volume of:",total_volume)

def askhsh_33():
    first_variable = float(input("Please give me a number: "))
    second_variable = float(input("Give me another number to divide the first one: "))
    division = first_variable // second_variable
    remainder = first_variable % second_variable
    print("If we divide "+str(first_variable)+" with "+str(second_variable)+" we will have a result of "+str(division)+" with a remainder of "+str(remainder))

def askhsh_34():
    print("1) Square")
    print("2) Triangle")
    print()
    choice = int(input("Enter a number: "))
    if choice == 1:
        length_of_side = float(input("Please give the side of the square (cm) : "))
        square_area = length_of_side ** 2
        print("A square with a side of "+str(length_of_side)+" cm will have an area of "+str(square_area)+" cm^2")
    elif choice == 2:
        triangles_base = float(input("Please give the length of the base of the triangle (cm) : "))
        triangles_height = float(input("Please give the length of the height of the triangle (cm) : "))
        triangles_area = (triangles_base * triangles_height) ** 1/2
        print("A triangle with a base of",triangles_base,"cm and a height of",triangles_height,"cm, will have an area of",triangles_area,"cm^2")

def askhsh_35():
    users_name = input("Please enter your name: ")
    for i in range(0,3):
        print(users_name)

def askhsh_36():
    users_name = input("Please enter your name: ")
    number_of_times = int(input("Please enter how many times to print your name: "))
    for i in range(0,number_of_times):
        print(users_name)

def askhsh_37():
    users_name = input("Please enter your name: ")
    for i in users_name:
        print(i)

def askhsh_38():
    users_name = input("Please enter your name: ")
    number_of_times = int(input("Please enter how many times to print your name: "))
    for i in range(0,number_of_times):
        for i in users_name:
            print(i)

def askhsh_39():
    users_input = int(input("Please give a number between 1 and 12, to display the times table of that number: "))
    for i in range(1,10+1):
        print(i,"x",users_input,"=",i*users_input)

def askhsh_40():
    users_input = int(input("Please give a number below 50: "))
    for i in range(users_input,0,-1):
        print(i)

def askhsh_41():
    users_name = input("Please enter your name: ")
    number_of_times = int(input("Please insert how many times to print the name (better be less than 10!): "))
    if number_of_times < 10:
        for i in range(1,number_of_times+1):
            print(users_name)
    else:
        for i in range(1,3+1):
            print("Too high.")

def askhsh_42():
    total = 0
    for i in range(1,5+1):
        users_input = int(input("Please enter a number: "))
        inclusion = input("Do you want to include this number in the total? type yes or no: ").lower()
        if inclusion == "yes":
            total = total + users_input
    print("The summary of the numbers you' ve asked me to calculate is:",total)

def askhsh_43():
    direction = input("Which direction you want to count? please insert up or down: ").lower()
    if direction == "up":
        top_number = int(input("Please give me a top number:"))
        for i in range(1,top_number+1):
            print(i)
    elif direction == "down":
        bottom_number = int(input("Please give me from which number you want me to count down (let that number be below 20): "))
        for i in range(bottom_number,0,-1):
            print(i)

def askhsh_44():
    number_of_party_guests = int(input("How many people do you want to invite to the party? "))
    if number_of_party_guests > 9:
        print("Too many people")
    else:
        for i in range(1,number_of_party_guests+1):
            name = input("Give the name of your guest: ")
            print(name,"has been invited.")

def askhsh_45():
    total = 0
    while total <= 50:
        number_input = int(input("Please give me a number to add to the total: "))
        total = total + number_input
        print("The total is now: "+str(total))
    print("The total has surpassed 50. The program will conclude.")

def askhsh_46():
    number = 0
    while number < 6:
        number = int(input("Please enter a number: "))
    print("The last number you entered was: "+str(number))

def askhsh_47():
    value_1 = int(input("Please give me a number: "))
    value_2 = int(input("Please give me anotehr number to add to the first one: "))
    total = value_1 + value_2
    question = input("Would you like to add another number? type y for yes: ")
    while question == "y":
        value_3 = int(input("Please give another number to add to the previous ones: "))
        total = total + value_3
        question = input("Would you like to add another number? type y for yes: ")
    print("The summary of the numbers you' ve entered is:",total)

def askhsh_48():
    count = 0
    invitee = input("Who do you want to invite to the party? ")
    while invitee != "":
        print(invitee,"has been invited.")
        count = count + 1
        invitee = input("Who do you want to invite to the party? ")
    print("You have invited",count,"guests to the party.")

def askhsh_49():
    compnum = 50
    attemps_count = 0
    users_guess = 0
    while compnum != users_guess:
        users_guess = int(input("Take a guess for the number i am thinking: "))
        attemps_count += 1
        if users_guess > compnum:
            print("Too high")
        elif users_guess < compnum:
            print("Too low")
    print("Well done, the number is",compnum,"and it took you "+str(attemps_count)+" guesses to find it.")

def askhsh_50():
    users_input = 0
    while users_input < 10 or users_input > 20:
        users_input = int(input("Please input a number between 10 and 20: "))
        if users_input < 10:
            print("Too low.")
        elif users_input > 20:
            print("Too high")
        else:
            print("Thank you")

def askhsh_51():
    num_of_bottles = 10
    while num_of_bottles != 0:
        print("----------------------------------------------------------------------")
        print("There are",num_of_bottles,"green bottles hanging on the wall,\n",num_of_bottles,"green bottles hanging on the wall,\nand if 1 green bottle should accidentally fall.")
        print("----------------------------------------------------------------------")
        users_input = int(input("How many bottles will be hanginbg on the wall? "))
        if users_input == num_of_bottles - 1:
            print("There will be",num_of_bottles,"green bottles hanging on the wall.")
            num_of_bottles = num_of_bottles - 1
        else:
            print("No, try again")
    print("There are no more green bottles hanging on the wall.")

def askhsh_52():
    random_value = random.randint(1,100)
    print("Here is a random value between 1 and 100: "+str(random_value))

def askhsh_53():
    fruits_list = ["banana" , "cherry" , "watermelon" , "apple" , "strawberry"]
    fruit_picked = random.choice(fruits_list)
    print("Here is a random fruit:",fruit_picked)

def askhsh_54():
    pc_pick = random.choice(["h" , "t"])
    users_pick = input("Pick between heads or tails, type h or t: ")
    if users_pick == pc_pick:
        print("You win!")
    else:
        print("Bad luck.")
    if pc_pick == "t":
        print("The computer had selected tails")
    if pc_pick == "h":
        print("The computer had selected heads")

def askhsh_55():
    pc_pick = random.randint(1,5)
    users_input = int(input("Guess which number did the pc pick between 1 and 5: "))
    if users_input == pc_pick:
        print("Well done you guessed right.")
    else:
        if users_input > pc_pick:
            print("Too high")
        elif users_input < pc_pick:
            print("Too low")
        users_input = int(input("Take another guess on which number did the pc pick between 1 and 5: "))
        if users_input == pc_pick:
            print("Correct")
        else:
            print("You lose")

def askhsh_56():
    pc_pick = random.randint(1,10)
    users_pick = 0
    while users_pick != pc_pick:
        users_pick = int(input("Guess which number did the computer think? hint: it is between 1 and 10: "))
    print("Correct, it's "+str(pc_pick))

def askhsh_57():
    pc_pick = random.randint(1,10)
    users_pick = 0
    while users_pick != pc_pick:
        users_pick = int(input("Guess which number did the computer think? hint: it is between 1 and 10: "))
        if users_pick > pc_pick:
            print("Too high")
        elif users_pick < pc_pick:
            print("Too low")
    print("Correct, it's "+str(pc_pick))

def askhsh_58():
    num_of_question = 0
    score = 0
    while num_of_question != 5:
        random_value_one = random.randint(1,10)
        random_value_two = random.randint(1,10)
        correct_summary = random_value_one + random_value_two
        print("How much is",random_value_one,"+",random_value_two,"?")
        users_input = int(input("The Answer is: "))
        if users_input == correct_summary:
            score += 1
        num_of_question += 1
    print("You scored "+str(score))

def askhsh_59():
    colours = ["blue", "green" , "red" , "yellow" , "white"]
    pc_pick = random.choice(colours)
    print("The choices are:",colours)
    users_pick = input("Guess which colour did the computer pick: ").lower()
    if users_pick == pc_pick:
        print("Well done")
    else:
        while users_pick != pc_pick:
            if pc_pick == "red":
                print("I guess you are seeing RED right now.")
            if pc_pick == "blue":
                print("I guess you are BLUE right now.")
            if pc_pick == "green":
                print("I guess you are GREENING right now.")
            if pc_pick == "yellow":
                print("I guess you are YELLOWING right now.")
            if pc_pick == "white":
                print("Come on, what is the brightest colour of all?")
            print("The choices are:",colours)
            users_pick = input("Guess again which colour did the computer pick: ").lower()

def askhsh_60():
    import turtle

    for i in range(0,4):
        turtle.forward(100)
        turtle.right(90)
    
    turtle.exitonclick()

def askhsh_69():
    countries = ("Cyprus" , "Greece" , "Italy" , "Japan" , "Indonesia")
    print(countries)
    users_pick = input("Pick one country from the above choices: ")
    print("You have chosen the country in position:",countries.index(users_pick)+1,)

def askhsh_70():
    countries = ("Cyprus" , "Greece" , "Italy" , "Japan" , "Indonesia")
    print(countries)
    users_pick = input("Pick one country from the above choices: ")
    print("You have chosen the country in position:",countries.index(users_pick)+1,)
    users_pick_number = int(input("Pick the number of a country from the above choices: "))
    print("The country in position:",users_pick_number,"is",countries[users_pick_number-1])

def askhsh_71():
    sports_list_one = ["football" , "basketball"]
    sport_input = input("Please insert another sport: ")
    sports_list_one.append(sport_input)
    sports_list_one.sort()
    print(sports_list_one)

def askhsh_72():
    school_subjects = ["History" , "Mathematics" , "Gymnastics" , "Algebra" , "Geometry" , "Electronics"]
    print("Current school subjects:",school_subjects)
    subject = input("Choose which subject you want to remove: ")
    school_subjects.remove(subject)
    print("Lessons look better this way:",school_subjects)

def askhsh_73():
    foods = {}
    while len(foods) !=4:
        users_input = input("Please insert a food: ")
        foods[users_input] = len(foods)+1
    print("The list of foods is the following:\n",foods)
    users_input_food_remove = input("Which food do you want to remove from the list? ")
    del foods[users_input_food_remove]
    #foods.sort()
    print("The current list of foods sorted is the following: ",sorted(foods))

def askhsh_74():
    colours = {}
    while len(colours) != 10:
        users_input = input("Please insert a colour: ")
        colours[len(colours)] = users_input
    print("The list of colours you have entered is the following:",colours)
    start_number = int(input("Give me a number between 0 and 4: "))
    end_number = int(input("Give me a number between 5 and 9: "))
    for i in range(start_number,end_number):
        print(colours[i])

def askhsh_75():
    numbers_list = []
    for i in range(1,4+1):
        new_number = random.randint(100,999)
        numbers_list.append(new_number)
    print("The current list of numbers is:",numbers_list)
    users_input = int(input("Please give me one of the above 3 digit numbers: "))
    while users_input not in numbers_list:
        print("That is not in the list.")
        users_input = int(input("Please give me one of the above 3 digit numbers: "))
    print("The position of this number is:",numbers_list.index(users_input))

def askhsh_76():
    guests = []
    for i in range(1,3+1):
        users_input = input("Please enter the name of a guest: ")
        guests.append(users_input)
    users_input_query = input("Do you want to insert the name of another guest? type yes or no: ")
    while users_input_query != "no":
        users_input = input("Please enter the name of a guest: ")
        guests.append(users_input)
        users_input_query = input("Do you want to insert the name of another guest? type yes or no: ")
    print("The guests of the part are the following:",guests)
        
def askhsh_77():
    guests = []
    for i in range(1,3+1):
        users_input = input("Please enter the name of a guest: ")
        guests.append(users_input)
    users_input_query = input("Do you want to insert the name of another guest? type yes or no: ")
    while users_input_query != "no":
        users_input = input("Please enter the name of a guest: ")
        guests.append(users_input)
        users_input_query = input("Do you want to insert the name of another guest? type yes or no: ")
    print("The guests of the part are the following:",guests)
    users_input = input("Type the name of one of your guests: ")
    print("The position of that name in the guests list is:",guests.index(users_input))
    users_input_query = input("Are you sure you want this guest to be invited to the party? type yes or no: ")
    if users_input_query == "no":
        guests.remove(users_input)
    print("The final list of guests is the following:",guests)

def askhsh_78():
    list_of_movies = ["Lord of  the Rings" , "He was a quiet man" , "Matrix" , "Star Wars"]
    for i in list_of_movies:
        print(i)
    users_input_movie = input("Please give another movie: ")
    users_input_place = int(input("Please give the position of the movie on the list: "))
    list_of_movies.insert(users_input_place,users_input_movie)
    print("The new list of movies is the following: ")
    for i in list_of_movies:
        print(i)

def askhsh_79():
    nums = []
    while len(nums) != 3:
        users_input = int(input("Please insert  a number: "))
        nums.append(users_input)
        print("The current list is the following:",nums)
    last_number_query = input("Do you need me to keep the last number? type yes or no: ")
    if last_number_query == "no":
        nums.pop(-1)
    print("The final list of numbers is the following:",nums)

def askhsh_80():
    first_name = input("Please enter your first name: ")
    print("The length of your first name is",len(first_name),"characters.")
    last_name = input("Please enter your last name: ")
    print("The length of your last name is",len(last_name),"characters.")
    full_name = first_name + " " + last_name
    print("Your full name is",full_name,"and is consisted of",len(full_name),"characters.")

def askhsh_81():
    user_favourite_subject = input("Please type your favourite subject: ")
    for i in user_favourite_subject:
        print(i,end="-")

def askhsh_82():
    poem = "I’ll take an uphill road. I’ll take the paths to find the stairs that lead to freedom."
    print(poem)
    starting_point = int(input("Please give a starting point: "))
    ending_point = int(input("Please give a ending point: "))
    for i in range(starting_point,ending_point):
        print(poem[i],end="")

def askhsh_83():
    users_word = "notupper"
    users_word = input("Please enter a word in full uppercase: ")
    while not users_word.isupper():
        users_word = input("Please try again and enter a word in full uppercase: ")
    print("Your last word was in full uppercase. Thank you.")

def askhsh_84():
    users_postcode = input("Please enter a word with at least 3 letters in lowercase ")
    for i in range(0,2):
        print(users_postcode[i].upper(),end="")
    for i in range(2,(len(users_postcode))):
        print(users_postcode[i],end="")

def askhsh_85():
    vowels = ["a" , "e" , "i" , "o" , "u" , "y"]
    users_name = input("Please enter your name and we will count the vowels: ")
    vowels_count = 0
    for i in range(0,len(users_name)):
        if users_name[i] in vowels:
            vowels_count += 1
    print("Your name "+str(users_name+" contains "+str(vowels_count)+" vowels."))
            
def askhsh_86():
    case_count = 0
    wrong_character = 0
    users_password = input("Please enter a password: ")
    password_verification = input("Please enter your password again for verification: ")
    if users_password == password_verification:
        print("Thank you")    
    elif len(users_password) > len(password_verification) or len(users_password) < len(password_verification):
        print("Incorrect")
    else:
        for i in range(0,len(users_password)):
            if users_password[i] != password_verification[i]:
                if users_password[i] == password_verification[i].lower() or users_password[i] == password_verification[i].upper():
                    case_count += 1
                else:
                    wrong_character += 1
        if case_count != 0:
            print("The two passwords must be in the same case")
        elif wrong_character != 0:
            print("Incorrect")

def askhsh_87():
    users_input = input("Please enter a word: ")
    for i in range(len(users_input),0,-1):
        print(users_input[i-1])

def askhsh_88():
    array_of_5 = array('i',[])
    print("Please enter 5 integer values")
    for i in range(0,5):
        users_input = int(input("Please enter a value: "))
        array_of_5.append(users_input)
    array_of_5 = sorted(array_of_5)
    for i in range(len(array_of_5),0,-1):
        print(array_of_5[i-1])

def askhsh_89():
    pinakas = array('i',[])
    for i in range(0,5):
        new_value = random.randint(1,100)
        pinakas.append(new_value)
    for i in pinakas:
        print(i)

def askhsh_90():
    pinakas = array('i',[])
    while len(pinakas) != 5:
        users_input = int(input("Please enter a number between 10 and 20: "))
        if users_input < 10 or users_input > 20:
            print("The number you' ve entered is outside of range")
        else:
            pinakas.append(users_input)
    print("Thank you")
    for i in pinakas:
        print(i)

def askhsh_91():
    pinakas = array("i",[])
    for i in range(0,4):
        new_value = random.randint(100,999)
        pinakas.append(new_value)
    print("Table 1:",pinakas)
    for i in range(0,2):
        new_value = random.choice(pinakas)
        pinakas.append(new_value)
    print("Table 2:",pinakas)
    users_input = int(input("Please give a number to count how many times it exists in the table: "))
    print("Number",users_input,"exists",pinakas.count(users_input),"times in the array.")

def askhsh_92():
    user_array = array("i",[])
    pc_array = array("i", [])
    for i in range(0,3):
        users_input = int(input("Please give a number to insert to the users table: "))
        user_array.append(users_input)
    for i in range(0,5):
        new_value = random.randint(1,999)
        pc_array.append(new_value)
    user_array.extend(pc_array)
    sorted_array = sorted(user_array)
    for i in sorted_array:
        print(i)

def askhsh_93():
    user_array = array("i", [])
    for i in range(0,5):
        user_input = int(input("Please enter an integer value: "))
        user_array.append(user_input)
    sorted_array = sorted(user_array)
    print("The current array holds the following values:",sorted_array)
    user_input = int(input("Pick a value to remove from the array: "))
    new_array = sorted_array
    new_array.remove(user_input)
    print("The array now is the following:",new_array)

def askhsh_94():
    random_array = array("i", [])
    for i in range(0,5):
        random_array.append(random.randint(0,100))
    print(random_array)
    user_input = int(input("Select one of the numbers from the array: "))
    while user_input not in random_array:
        user_input = int(input("The number you have selected does not exist in the array, please try one of the following numbers: "))
        for i in random_array:
            print(i)
    print("The number",user_input,"exists in position",random_array.index(user_input),"of the array.")


#me array double. an to array kamw to float tote oi metavlhtes mes  ton pinaka apoktoun panw apo 2 dekadika j en tropo os twra na to saso. edokimasa thn vivliothiki decimal alla tipote. to numpy en to dokimasa alla mes to internet grafun oti enna exei paromoia provlhmata
def askhsh_95():
    #getcontext().prec = 2
    pinakas = array("d", [])
    divided_pinakas = array("d", [])
    for i in range(0,5):
        rounded = round(random.uniform(10,100),2)#outputs a float number
        pinakas.append(float(rounded))
    #pu dame j katw na ginei copy paste j sto epomeno programma
    print("The generated values are the following:",pinakas)
    users_input = int(input("Choose a value between 2 and 5 to divide the values of the array: "))
    while users_input < 2 or users_input > 5:
        users_input = int(input("Incorrect. Please choose a value between 2 and 5 to divide the values of the array: "))
    for i in range(0,len(pinakas)):
        divided_value = round( (pinakas[i]/users_input), 2)
        divided_pinakas.append(divided_value)
    print("The array with the divided values is the following:",divided_pinakas)

def askhsh_96():
    simple_list = [[2,5,8],[3,7,4],[1,6,9],[4,2,1]]
    print(simple_list)

def askhsh_97():
    simple_list = [[2,5,8],[3,7,4],[1,6,9],[4,2,1]]
    print(simple_list)
    user_input_row = int(input("Select a row: "))
    user_input_column = int(input("Select a column: "))
    print("In row",user_input_row,"and column",user_input_column,"the value",simple_list[user_input_row][user_input_column],"exists.")

def askhsh_98():
    simple_list = [[2,5,8],[3,7,4],[1,6,9],[4,2,1]]
    print(simple_list)
    user_input_row = int(input("Select a row: "))
    print(simple_list[user_input_row])
    new_value = int(input(f"Please insert a new value to add it to row {user_input_row}: "))
    simple_list[user_input_row].append(new_value)
    print(simple_list[user_input_row])

def askhsh_99():
    simple_list = [[2,5,8],[3,7,4],[1,6,9],[4,2,1]]
    print(simple_list)
    user_input_row = int(input("Select a row: "))
    print(simple_list[user_input_row])
    user_input_column = int(input("Select a column: "))
    print(f"The value that currently exists in position {user_input_row},{user_input_column} of the list is {simple_list[user_input_row][user_input_column]}")
    user_input_replace = input("Do you want to have that value replaced? type yes or no: ")
    if user_input_replace == "yes":
        new_value = int(input("Please insert a new value: "))
        simple_list[user_input_row][user_input_column] = new_value
    print("The row now is the following:",simple_list[user_input_row])

def askhsh_100():
    sales_dictionary = { 
        #"Name" : {"N":XXX,"S":XXX,"E":XXX,"W":XXX},
        "John" : {"N":3056,"S":8463,"E":8441,"W":2694},
        "Tom" : {"N":4832,"S":6786,"E":4737,"W":3612},
        "Anne" : {"N":5239,"S":4802,"E":5820,"W":1859},
        "Fiona" : {"N":3904,"S":3645,"E":8821,"W":2451}
        }
    print("These are the sales of each salesperson:\n",sales_dictionary)

def askhsh_101():
    sales_dictionary = { 
        "John" : {"N":3056,"S":8463,"E":8441,"W":2694},
        "Tom" : {"N":4832,"S":6786,"E":4737,"W":3612},
        "Anne" : {"N":5239,"S":4802,"E":5820,"W":1859},
        "Fiona" : {"N":3904,"S":3645,"E":8821,"W":2451}
        }
    print("These are the sales of each salesperson:\n",sales_dictionary)
    user_input_name = input("Pick a name of a salesperson: ")
    user_input_region = input("Pick a region ")
    user_input_neovalue = int(input(f"Insert a new value for region {user_input_region} of {user_input_name}: " ))
    sales_dictionary[user_input_name][user_input_region] = user_input_neovalue
    print(sales_dictionary[user_input_name])

def askhsh_102():
    pinakas = {}
    print("Please insert 4 people's names, their ages and shoe sizes")
    for i in range(0,4):
        user_input_name = input(f"Please enter the name of person number {i+1}: ")
        user_input_age = int(input(f"Please enter the age of {user_input_name}: "))
        user_input_size = int(input(f"Please enter the shoe size of {user_input_name}: "))
        pinakas[user_input_name] = {"Age":user_input_age , "Shoe size":user_input_size }
    print("The list is the following:",pinakas)
    user_choice_name = input("Please select one of the persons listed: ")
    print(f"The information we got for {user_choice_name} are the following:",pinakas[user_choice_name])

def askhsh_103():
    pinakas = {}
    print("Please insert 4 people's names, their ages and shoe sizes")
    for i in range(0,4):
        user_input_name = input(f"Please enter the name of person number {i+1}: ")
        user_input_age = int(input(f"Please enter the age of {user_input_name}: "))
        user_input_size = int(input(f"Please enter the shoe size of {user_input_name}: "))
        pinakas[user_input_name] = {"Age":user_input_age , "Shoe size":user_input_size }
    print("The list is the following:",pinakas)
    print("The list without their ages is the following: ")
    for i in pinakas:
        print(f"{i} is {pinakas[i]['Age']} years old.")

def askhsh_104():
    pinakas = {}
    print("Please insert 4 people's names, their ages and shoe sizes")
    for i in range(0,4):
        user_input_name = input(f"Please enter the name of person number {i+1}: ")
        user_input_age = int(input(f"Please enter the age of {user_input_name}: "))
        user_input_size = int(input(f"Please enter the shoe size of {user_input_name}: "))
        pinakas[user_input_name] = {"Age":user_input_age , "Shoe size":user_input_size }
    print("The list is the following:",pinakas)
    user_deletion = input("Type the name of someone from the list above you want to remove his/hers details: ")
    del pinakas[user_deletion]
    print("The list is the following:",pinakas)

def askhsh_text_example_1():
    #file creation + data insertion + close file
    file = open("Countries.txt","w")#file creation
    file.write("Greek\n")#data insertion
    file.write("Cyprus\n")
    file.write("Italy\n")
    file.close()#close the file
    #open a file and print its content
    file = open("Countries.txt","r")
    print(file.read())
    file = open("Countries.txt","a")
    file.write("France\n")
    file.close()

def askhsh_105():
    file = open("Numbers.txt","w")
    for i in range(0,5):
        new_value = random.randint(0,100000)
        file.write(str(new_value)+",")

def askhsh_106():
    file = open("Names.txt","w")
    file.write("Kosths\n")
    file.write("Andreas\n")
    file.write("Giannis\n")
    file.write("Antonis\n")
    file.write("Marios")

def askhsh_107():
    file = open("Names.txt","r")
    print(file.read())

def askhsh_108():
    file = open("Names.txt","a")
    user_input = input("Please enter a name to add it to the Names.txt file: ")
    file.write("\n"+user_input)

def askhsh_109():
    print("1) Create a new file")
    print("2) Display the file")
    print("3) Add a new item to the file")
    user_menu_choice = int(input("Make a selection 1, 2 or 3: "))
    while user_menu_choice not in [1 , 2, 3]:
        print("Please make a valid selection")
        user_menu_choice = int(input("Make a selection 1, 2 or 3: "))
    if user_menu_choice == 1:
        file = open ("Subject.txt","w")
        user_input_subject = input("Enter a school subject: ")
        file.write(user_input_subject)
    if user_menu_choice == 2:
        file = open("Subject.txt","r")
        print(file.read())
    if user_menu_choice == 3:
        file = open("Subject.txt","a")
        user_input_subject = input("Add another subject to the file: ")
        file.write("\n"+user_input_subject)

def askhsh_110():
    file = open("Names.txt","r")
    file_new = open("Names2.txt","w")
    print(file.read())
    #file.close()
    print("---------")
    user_input_name_remove = input("Select a name to remove from the list above: ")
    print("---------")
    file = open("Names.txt","r")
    new_list = file.readlines()
    #begin - to clean the \n characters
    for i in range(0,len(new_list)):
        if "\n" in new_list[i] :
            new_list[i] = new_list[i].rstrip("\n")
    #end - to clean the \n characters
    print(new_list)
    new_list.remove(user_input_name_remove)
    print(new_list)
    for i in new_list:
        file_new.write(i+"\n")
    file_new.close()
    #while str(file.readline()) != user_input_name_remove:
    #    file_new.write_through(str(file.readline()))

def askhsh_111():
    file = open("Books.csv", "w")
    lista = [
        "To Kill A Mockingbird"+","+"Harper Lee"+","+"1960"+"\n",
        "A Brief History of Time"+","+"Stephen Hawking"+","+"1988"+"\n",
        "The Great Gatsby"+","+"F. Scott Fitzgerald"+","+"1922"+"\n",
        "The Man Who Mistook His Wife for a Hat"+","+"Oliver Sacks"+","+"1985"+"\n",
        "Pride and Prejudice"+","+"Jane Austen"+","+"1813"+"\n",
    ]
    for i in range(0,5):
        new_record = lista[i]
        file.write(new_record)
    file.close()

def askhsh_112():
    file = open("Books.csv","a")
    user_entry_book = input("Please enter a new book: ")
    user_entry_author = input("Please enter the author: ")
    user_entry_year = input("Please enter the year that the book was written: ")
    new_record = user_entry_book+","+user_entry_author+","+user_entry_year+"\n"
    file.write(new_record)
    file.close()

    file = open("Books.csv","r")

    for i in file:
        print(i)

def askhsh_113():
    file = open("Books.csv","a")
    number_of_new_entries = int(input("How many new entries do you want to insert? "))
    for i in range(0,number_of_new_entries):
        user_entry_book = input("Please enter a new book: ")
        user_entry_author = input("Please enter the author: ")
        user_entry_year = input("Please enter the year that the book was written: ")
        new_record = user_entry_book+","+user_entry_author+","+user_entry_year+"\n"
        file.write(new_record)
    file.close()

    file = open("Books.csv","r")
    author_search = input("Enter the name of an author to present you with his/her books: ")
    reader = csv.reader(file)
    for row in file:
        if author_search in str(row):
            print(row)

def askhsh_114():
    start_year = int(input("Enter a starting year: "))
    end_year = int(input("Enter an ending year: "))
    file = open("Books.csv","r")
    for row in file:
        for i in range(start_year,end_year):
            if str(i) in str(row):
                print(row)

def askhsh_115():
    file = open("Books.csv","r")
    counter = 0
    for row in file:
        counter += 1
        print(str(counter)+"."+str(row))

def askhsh_116():
    file = open("Books.csv","r")
    temporary_storage =[]
    for row in file:
        x = row.replace("\n","")
        temporary_storage.append(x)
    file.close()
    for i in range(0,len(temporary_storage)):
        print(i,"-",temporary_storage[i],end="\n")
    user_delete = int(input("Choose a row to delete: "))
    del temporary_storage[user_delete]
    for i in range(0,len(temporary_storage)):
        print(i,"-",temporary_storage[i],end="\n")
    user_change = int(input("Choose which row you want to alter: "))
    new_text = input(f"Insert new text for place {user_change}: ")
    del temporary_storage[user_change]
    temporary_storage.insert(user_change,new_text)
    for i in range(0,len(temporary_storage)):
        print(i,"-",temporary_storage[i],end="\n")
    file = open("Books.csv","w")
    for i in range(0,len(temporary_storage)):
        file.write(temporary_storage[i]+"\n")
    file.close()
    
def askhsh_117():
    file = open("math_problems.csv","a")
    userinput_name = input("Please enter your name: ")
    score = 0
    x_one = random.randint(0,10)
    y_one = random.randint(0,10)
    answer_one = x_one + y_one
    x_two = random.randint(0,10)
    y_two = random.randint(0,10)
    answer_two = x_two + y_two
    userinput_problem_one_question = (f"What is the sum of {x_one} and {y_one}? ")
    userinput_problem_one = int(input(userinput_problem_one_question))
    userinput_problem_two_question = (f"What is the sum of {x_two} and {y_two}? ")
    userinput_problem_two = int(input(userinput_problem_two_question))
    if userinput_problem_one == answer_one:
        score += 1
    if userinput_problem_two == answer_two:
        score += 1
    new_record = "user's name: "+userinput_name+",1st question: "+str(userinput_problem_one_question)+",2nd question: "+str(userinput_problem_two_question)+",answer given for 1st problem: "+str(userinput_problem_one)+",answer given for 2nd problem: "+str(userinput_problem_two)+",With these answers the user's score is: "+str(score)
    file.write(new_record+"\n")
    file.close()

    '''
    while file.readline() != None:
        if file.readline() != user_input_name_remove:
            file_new.write(str(file.readline()))
    '''
    #
    #number_of_names = file.count("\n")
    
    #print("The number of names is:",number_of_names)
    #for i in 


def main():
    #dialogh_askhseis = int(input("Choose an exercise: "))
    dialogh_askhseis = input("Choose an exercise: ")
    #print("h askhsh pu dialekses  einai h: "+str(dialogh_askhseis))
    #askhsh = "askhsh_"+str(dialogh_askhseis)
    askhsh = "askhsh_"+dialogh_askhseis
    exec(askhsh+'()')

'''
    while True:
        match dialogh_askhseis:
            case 1:
                askhsh_1()
                print("Thank you, bye")
                break
            case 2:
                askhsh_2()
                print("Thank you, bye")
                break
            case 3:
                askhsh_3()
                print("Thank you, bye")
                break
            case _ :
                dialogh_askhseis = int(input("Wrong input. Put a correct input: "))
'''

main()