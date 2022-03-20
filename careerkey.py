import csv
import requests
from bs4 import BeautifulSoup

csv_file = csv.reader(open('by_major.csv', 'r'))
rows = list(csv_file)

print("Welcome to...")
print("""
 .d8888b.                                             888    d8P                    
d88P  Y88b                                            888   d8P                     
888    888                                            888  d8P                      
888         8888b.  888d888  .d88b.   .d88b.  888d888 888d88K      .d88b.  888  888 
888            "88b 888P"   d8P  Y8b d8P  Y8b 888P"   8888888b    d8P  Y8b 888  888 
888    888 .d888888 888     88888888 88888888 888     888  Y88b   88888888 888  888 
Y88b  d88P 888  888 888     Y8b.     Y8b.     888     888   Y88b  Y8b.     Y88b 888 
 "Y8888P"  "Y888888 888      "Y8888   "Y8888  888     888    Y88b  "Y8888   "Y88888 
                                                                                888 
                                                                           Y8b d88P 
                                                                            "Y88P"  
""")
print("If you're a high school student struggling to decide on a career path, this is the tool for you!")
print("First of all, what's your name?")
name = input()
print("Hi " + name + ", nice to meet you! Let's help you figure out what you want to do after high school.")


def main():
    input_one = input("Do you plan on going to university? (y/n)\n")
    if input_one == "y":
        third()
    elif input_one == "n":
        print('Some other options that are available are taking a gap year or doing an apprenticeship.')
        other_options()
    else:
        print("Sorry, I don't understand. Please print 'y' or 'n'.")
        main()


def major_info():
    chosen_major = input()
    chosen_major = chosen_major.upper()
    if chosen_major == "COMPUTER SCIENCE":
        print("There's lots of types of computer science. Do you mean Artificial Intelligence, Cybernetics,")
        print("Hardware & Architecture, Information Systems, Interdisciplinary Applications, Software Engineering,")
        print("or Theory & Methods? (please print the exact name! eg. 'hardware & architecture')")
        chosen_major = "COMPUTER SCIENCE, " + input().upper()
    elif chosen_major == "CHEMISTRY":
        print("There's lots of types of chemistry. Do you mean Analytical, Applied,")
        print("Inorganic & Nuclear, Medicinal, Multidisciplinary, Organic,")
        print("or Physical? (please print the exact name! eg. 'Inorganic & Nuclear')")
        chosen_major = "CHEMISTRY, " + input().upper()
    elif chosen_major == "ENGINEERING":
        print("There's lots of types of engineering. Do you mean Aerospace, Biomedical,")
        print("Chemical, Civil, Electrical & Electronic, Environmental, Geological,")
        print("Industrial, Manufacturing, Marine, Mechanical, Multidisciplinary,")
        print("Ocean, or Petroleum? (please print the exact name! eg. 'Multidisciplinary')")
        chosen_major = "ENGINEERING, " + input().upper()
    elif chosen_major == "PHYSICS":
        print("There's lots of types of physics. Do you mean Applied, Atomic,")
        print("Molecular & Chemical, Condensed Matter, Fluids & Plasmas, Mathematical, Multidisciplinary,")
        print("Nuclear, or Particles & Fields? (please print the exact name! eg. 'Multidisciplinary')")
        chosen_major = "PHYSICS, " + input().upper()
    elif chosen_major == "MATERIALS SCIENCE":
        print("There's lots of types of material science. Do you mean Biomaterials, Ceramics,")
        print("Characterization & Testing, Coating & Films, Composites, Multidisciplinary,")
        print("Paper & Wood, or Textiles? (please print the exact name! eg. 'Multidisciplinary')")
        chosen_major = "MATERIALS SCIENCE, " + input().upper()
    elif chosen_major == "MEDICINE":
        print("There's lots of types of medicine. Do you mean Legal, Research & Experimental,")
        print("or General & Internal? (please print the exact name! eg. 'Research & Experimental')")
        chosen_major = "MEDICINE, " + input().upper()

    def find_index(my_input):
        index = 0
        for row in rows:
            if row[0] == my_input:
                return index
            else:
                index += 1
    try:
        row_num = int(find_index(chosen_major))
        top_schools = rows[row_num + 2:row_num + 12]
        answer = ""
        for item in top_schools:
            rank = item[0]
            school = item[1]
            answer = answer + rank + ". " + school + '\n'
        print("That sounds interesting! Here's a list of the top schools for " + chosen_major + ".")
        print(answer)
    except TypeError:
        print("Sorry! I don't have any information about " + chosen_major + " yet.")


def pick_major():
    bus = 0
    law = 0
    comp = 0
    edu = 0
    eng = 0

    q1 = input("I love telling or hearing stories. (y/n) \n")
    if q1 == "y":
        edu += 1
        bus += 1
        law += 1
    elif q1 == "n":
        comp += 1
        eng += 1

    q2 = input("I want to help others overcome their difficulties. (y/n) \n")
    if q2 == "y":
        edu += 1
        comp += 1
        law += 1
        eng += 1
    elif q2 == "n":
        bus += 1

    q3 = input("I like competitive sports. (y/n) \n")
    if q3 == "y":
        edu += 1
        bus += 1
        law += 1
        eng += 1
    elif q3 == "n":
        comp += 1
        eng += 1

    q4 = input("I like determining the cause of what happened. (y/n) \n")
    if q4 == "y":
        edu += 1
        comp += 1
        law += 1
        eng += 1
    elif q4 == "n":
        bus += 1

    q5 = input("I want to work with children or teens. (y/n) \n")
    if q5 == "y":
        edu += 1
    elif q5 == "n":
        bus += 1
        comp += 1
        law += 1
        eng += 1

    q6 = input("I am interested in designing things. (y/n) \n")
    if q6 == "y":
        edu += 1
        comp += 1
        eng += 1
    elif q6 == "n":
        bus += 1
        law += 1

    q7 = input("I like to stand out and be the first to do something. (y/n) \n")
    if q7 == "y":
        edu += 1
        comp += 1
        eng += 1
        bus += 1
    elif q7 == "n":
        law += 1

    q8 = input("I appreciate people's differences. (y/n) \n")
    if q8 == "y":
        edu += 1
        law += 1
        bus += 1
    elif q8 == "n":
        comp += 1
        eng += 1

    q9 = input("I like to encourage people to be healthy. (y/n) \n")
    if q9 == "y":
        edu += 1
        bus += 1
        eng += 1
    elif q9 == "n":
        comp += 1
        law += 1

    q10 = input("I want to learn more about changes in culture, society, or language. (y/n) \n")
    if q10 == "y":
        edu += 1
        eng += 1
        law += 1
    elif q10 == "n":
        comp += 1
        bus += 1

    list_pick = [bus, law, comp, edu, eng]
    high_num = max(list_pick)
    if bus == high_num:
        result = "Business"
    elif law == high_num:
        result = "Law"
    elif comp == high_num:
        result = "Computer Science"
    elif edu == high_num:
        result = "Education"
    else:
        result = "Engineering"
    print("Based on the quiz, you should study " + result + ".")


def other_options():
    input_three = input("To learn more about gap years, type '1'. To learn more about apprenticeships, type '2'.\n")
    if input_three == "1":
        print("Visit the following website for more information about taking a gap year in Canada:")
        print("https://www.cangap.ca")
        while input("Do you want more information about some other options? (y/n)\n") == "y":
            other_options()
        print("I hope I was able to help!")
        quit()
    elif input_three == "2":
        print('"Apprenticeship trains people for a wide variety of practical skills, ranging from construction')
        print("and mechanical trades to hairdressing and outdoor guiding. When you complete the program, you’ll")
        print("receive a certification or “ticket” allowing you to practice the trade independently.\n")
        print("Apprenticeship programs combine paid on-the-job training with learning in a classroom or shop setting.")
        print("In most programs, you’ll spend about 85 per cent of the time on the job. Most programs take four years")
        print("to complete.\n")
        print("To complete your training and become qualified as a certified tradesperson in B.C., you must:")
        print("  - complete the required on-the-job hours and the in-school training")
        print("  - pass the examinations")
        print('  - earn the recommendation of your sponsoring employer"\n')
        print("Visit the following website for more information about apprenticeships:")
        print("https://www.workbc.ca/training-education/trades-training/about-apprenticeship.aspx \n")
        print("For a full list of available programs, type 'ok'. Otherwise, press enter.")
        if input() == "ok":
            crawler_titles()
        input_four = input("Do you want more information about a specific trade? (y/n)\n")
        if input_four == "y":
            crawler_links()
            while input("Do you want more information about some other trades? (y/n)\n") == "y":
                crawler_links()
            while input("Do you want more information about some other options? (y/n)\n") == "y":
                other_options()
            print("I hope I was able to help!")
            quit()
        else:
            print("I hope I was able to help!")
            quit()
    else:
        print("Sorry, I don't understand. Please print '1' or '2'.")
        other_options()


def crawler_titles():
    url = "https://www.itabc.ca/discover-apprenticeship-programs/search-programs"
    source_code = requests.get(url)
    html = BeautifulSoup(source_code.text, "html.parser")
    for title in html.findAll("h3", {"class": "tsrs-item-title"}):
        print(title.text)


def crawler_links():
    url = "https://www.itabc.ca/discover-apprenticeship-programs/search-programs"
    source_code = requests.get(url)
    html = BeautifulSoup(source_code.text, "html.parser")
    trade = input("Input the trade you are interested in:\n")
    trade = trade.title()
    trade_link = ""
    for link in html.findAll("a", {"class": "tsrs-item-link"}):
        for title in link.findAll("h3", {"class": "tsrs-item-title"}):
            if trade == title.text:
                trade_link = link.get("href")
                print("Follow this link for more information about being a " + trade + ":")
                print(trade_link)
    if trade_link == "":
        print("Sorry, I don't have any information for " + trade)


def third():
    input_two = input("Do you know what you want to major in? (y/n)\n")
    if input_two == "y":
        print("Great! What do you want to major in?")
        major_info()
        while input("Do you want more information about another major? (y/n)\n") == "y":
            print("Great! Which major would you like more information about?")
            major_info()
        print("I hope I was able to help!")
        quit()
    elif input_two == "n":
        print("Let's take a short quiz to help you figure out a major! Please answer the following questions:")
        pick_major()
        while input("If you would like to retake the quiz, type 'ok'. Otherwise, press enter.\n") == "ok":
            pick_major()
        print("Now, type in your major for a list of the top 10 schools for you.")
        major_info()
        while input("Do you want more information about another major? (y/n)\n") == "y":
            print("Great! Which major would you like more information about?")
            major_info()
        print("I hope I was able to help!")
        quit()
    else:
        print("Sorry, I don't understand. Please print 'y' or 'n'.")
        third()


main()
