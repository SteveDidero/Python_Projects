"""
This python script contains a number of simple python codes/games/functions written in my spare time to test my knowledge and practice my coding skills.
"""
import time
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import sqlite3

def challenge_1():
    """
    A simple game. The program generates a list of number from 1 and 100 and print the number or Fizz(if the number is a multiple of 3) or Buzz(if the number is multiple of 5) or FizzBuzz(if the number is a multiple of 3 and 5).
    """
    nums = [x for x in range(1, 101)]
    for i in nums:
        if (i % 3 == 0) and (i % 5 == 0):
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

def challenge_2(str1, str2):
    """
    A function that takes two string and check if the two strings are anagram of each other. Return True if there are and False if there are not.
    """
    str1_ls = sorted([x for x in str1])
    str2_ls = sorted([x for x in str2])

    return str1_ls == str2_ls

"""def challenge_3():
    URL = 'https://www.google.com/search'
    term = 'Percy Jackson and the Olympians'
    PARAMS = {'q': term}

    data = requests.get(url = URL, params = PARAMS)
    data_soup = BeautifulSoup(data.content, 'html.parser')
    pprint(data_soup)"""

def challenge_3():
    URL = 'https://www.nytimes.com/'
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')

    titles = []
    for item in soup.select('p[class*="indicate-hover"]')[:5]:
        titles.append(item.get_text())
        
    pprint(titles)

def challenge_4(n):
    pass

class challenge5:
    """
    I decided to create a class for this challenge because I wanted to created different methods, one for getting information about the database being used and another method to set/add data to the databse

    Args: 
    firstname, lastname, age, school, year_status(Freshmen, sophemore, junior, or senior)

    Returns:
    None

    Prints:
    The value of data inserted in the database
    
    """
    def __init__(self, firstname, lastname, age, school, year_status = 'freshmen'):
        """
        class construtor, takes firstname, lastname, age, school, and keyargs year_status defaulted to Freshmen
        """
        self.__firstname = firstname
        self.__lastname = lastname
        self.__age = age
        self.__school = school
        self.__year_status = year_status



    def challenge_5():
        pass

def challenge_6(slist = [[1,2,3,4], [2,1,4,3], [4,1,3,2]]):

    lenght = len(slist[0])
    l_sort = sorted(slist[0])

    s_set = set()
    

    for i in slist:
        for j in i:
            s_set.add(j)

    s_set = sorted(s_set)
    if (lenght == len(s_set)) and (l_sort == s_set):
        return True
    else:
        return False

def challenge_7(str1 = 'steve', str2 = 'eetvs'):
    """
    This function check if two string of equal lenght are the same if at most only once swap can be performed for the two string to be same. Simply put, only one swap can be performed to make the two string the same.

    Args:
    string 1 and string 2

    Returns:
    Boolean(True or False)
    
    Prints:
    None
    """

    l_str1 = [x for x in str1]
    l_str2 = [x for x in str2]

    lenght = len(l_str1)
    
    count = 0
    for i,j in enumerate(l_str2):
        if j != l_str1[i]:
            count +=1

    if count > 2:
        return False
    
    s1 = []
    s2 = []

    for i in l_str1:
        s1.append(i)

    for i in l_str2:
        s2.append(i)

    ss1 = sorted(s1)
    ss2 = sorted(s2)
    if ss1 == ss2:
        return True
    else:
        return False
    

    



def main():
    print('Hello there, which function of this challenge serrie do you want to view? Simply type "challenge 1" or "challenge 2 and so on" but if you don\'t want to view anything, can type "none" to exit the session!')

    userchoice = ''
    count = 0
    while userchoice != 'none':
        if count == 0:
            userchoice = input("Please choose an option ('challenge 1', 'challenge 2', or 'none' to exit): ").lower()
        else: 
            userchoice = input("If you want to view another challenge, same option as before ('challenge 1', 'challenge 2', or 'none' to exit): ").lower()

        if userchoice == 'challenge 1':
            print(challenge_1())
            count +=1

        elif userchoice == 'challenge 2':
            print('Sure thing, challenge two it is. But for this challenge, I\'ll need two string from you.')

            time.sleep(2)
            string1 = input('Please type the first string: ')
            time.sleep(2)
            string2 = input('And the second string please: ')
            time.sleep(2)
            print('Now let\'s find out if there are anagram of earch other')
            time.sleep(2)
            print(f"well, the answer is {challenge_2(string1, string2)}!")
            count +=1
        elif userchoice == 'challenge 3':
            print('This challenge uitilizes web scaping to get the top 5 news articles from the New York Time and print it for you in a list. ')

            time.sleep(2)
            print(challenge_3())
            count +=1
        elif userchoice == 'challenge 6':
            print(challenge_6())
            count +=1
        elif userchoice == 'challenge 7':
            print('This function checks if two string of equal lenght are the same if at most only one swap can be performed for the two string to be same. Simply put, the two strings has to be of equal lenght and only two character can be at different location on string 2 than from string 1.')

            time.sleep(1)
            choice = input('If you would you like to provide two string for this challenge type "yes" or "defualt" to use the default arguments or "none" to stop: ').lower()

            if choice == 'default':
                print(challenge_7())
                count +=1
            elif choice == 'yes':
                print('Sure but remember, two string of equal lenght and only two character placed differently in string 2 from string 1 for the challenge to evaluate to true!')
                st1 = input('Please the first the string: ').lower()
                st2 = input('And the second: ').lower()

                print(challenge_7(st1, st2))
                count +=1
            elif choice == 'none':
                continue

        else:
            pass

if __name__ == "__main__":
    main()