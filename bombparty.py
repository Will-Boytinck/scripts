import random
from bs4 import BeautifulSoup as BS
import requests

'''
This script generates a random word (with preference to the longest word found)
from merriam webster, that contains the prompt. the prompt is a series of letters where the word contains the prompt
this was made as a fun experiment for the game 'bombparty'
'''

def main() -> None:
    '''
    main flow
    '''
    # get mode
    mode = input("mode: ")
    
    # auto mode (wip)
    if mode == 'auto':
        bp_url = input("url: ")
        #while True:
        data = requests.get(bp_url)
        print(data.text)
        '''
            soup = BS(data.text, 'html.parser')
            prompt = soup.find_all("div", {"class": "syllable"}) # this doesn't work because it goes to the 'loading' page first, id have to bypass it
            #prompt = soup.find('div', class_='quickRules')
            if prompt:
                print(prompt.text)
            else:
                print("prompt not found")
        '''
                
            #random_word = scrape(prompt.text)
            #print(f"--------------{random_word}--------------")
        
    # manual mode    
    else:
        while True:
            prompt = input("Words containing: ")
            if prompt == "exit":
                exit()
            # get list of words
            random_word = scrape(prompt)
            print(f"--------------{random_word}--------------")

    

def scrape(prompt: str) -> str:
    '''
    get an array of the largest words containing the prompt
    '''
    # https://www.merriam-webster.com/wordfinder/classic/any-order/all/15/hi/1
    url = f"https://www.merriam-webster.com/wordfinder/classic/any-order/all/15/{prompt}/1"
    try:
        for i in range(15):
            length = 15 - i
            url = f"https://www.merriam-webster.com/wordfinder/classic/any-order/all/{length}/{prompt}/1"     
            data = requests.get(url)
            list_of_words = parse_data(data, prompt)
            if len(list_of_words) >= 1:
                random_word = list_of_words[random.randint(0, len(list_of_words)-1)]
                return random_word
    except Exception as e:
        print(f"Something bad happened: {e}")
    
    
def parse_data(list_of_words, prompt) -> list:
    '''
    parse the html/js to just contain the stuff we want
    '''
    soup = BS(list_of_words.text, 'html.parser')
    words = [a.text for a in soup.find_all("a") if prompt in a.text]
    return words
    
    
if __name__ == '__main__':
    main()
