import random
from bs4 import BeautifulSoup as BS
import requests

def main() -> None:
    '''
    main flow
    '''
    # get prompt
    prompt = input("Words containing: ")
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
