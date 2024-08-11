"""
This python script contains a number of simple python codes/games/functions written in my spare time to test my knowledge and practice my coding skills.
"""
import time
import requests
from bs4 import BeautifulSoup
from pprint import pprint

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
    URL = 'https://www.bbc.com/news'
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the titles of the first 5 articles
    titles = []
    for item in soup.find_all('h3')[:5]:  # Adjust the tag and class based on the website's HTML structure
        titles.append(item.get_text())
    
    pprint(titles)


def main():
    print('Hello there, which function of this challenge serrie do you want to view? Simply type "challenge 1" or "challenge 2 and so on" but if you don\'t want to view anything, can type "none" to exit the session!')

    userchoice = ''
    count = 0
    while userchoice != 'none':
        if count == 0:
            userchoice = input("Please choose an option ('challenge 1', 'challenge 2', or 'none' to exit): ").lower()
        else: 
            userchoice = input("If you want to view another challenge, same option as before ('challenge 1', 'challenge 2', or 'none' to exit: )").lower()

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
            print(challenge_3())
            count +=1
            
        else:
            pass

if __name__ == "__main__":
    main()