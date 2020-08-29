import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(str)

if __name__ == '__main__':
    url = "http://newsapi.org/v2/top-headlines?country=in&category=ent" \
          "ertainment&apiKey=04c7ce65d7e5492a93b9821bfd0143e6"
    news=requests.get(url).text
    news_dict=json.loads(news)
    NumberOfResults = news_dict['totalResults']
    # print(NumberOfResults)
    # print(news_dict["articles"])
    arts = news_dict['articles']
    i=0
    speak("The total number of results are..")
    speak(NumberOfResults)
    speak("News for Today....Lets Begin!")
    for a in arts:
        speak(a['title'])
        i=i+1
        if i<NumberOfResults :
            speak("Moving on to the next news")
    speak("Thanks for listening....")
