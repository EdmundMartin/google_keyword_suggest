import requests
from bs4 import BeautifulSoup
from random import choice

UserAgentList = ['Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36']

def RandomUserAgent():
    UserAgent = choice(UserAgentList)
    UserAgent = {'User-Agent':UserAgent}
    return UserAgent

def get_suggestion(suggestion):
    r = requests.get('{}{}'.format('http://suggestqueries.google.com/complete/search?output=toolbar&hl=en&q=',suggestion.replace(' ','+')),headers=RandomUserAgent())
    soup = BeautifulSoup(r.text,'lxml-xml')
    suggestions = soup.find_all('suggestion')
    suggestion_list = []
    for suggest in suggestions:
        suggest = suggest['data']
        suggestion_list.append(suggest)
    return suggestion_list

def write_to_csv(suggestion_list):
    for item in suggestion_list:
        with open('Output.csv','a',encoding='utf-8') as outputfile:
            outputfile.write('{}\n'.format(item))
