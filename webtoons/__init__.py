from bs4 import BeautifulSoup as bs
import requests
import time
import random

class Webtoons:
    def __init__(self):
        self.genres = self.getGenres()
        

# generates a list of webtoon genres
def getGenres(self):
    page=requests.get("https://www.webtoons.com/en/challenge/list?genreTab=ALL&sortOrder=")
    soup=bs(page.content, 'html.parser')

    ultag = soup.find("ul", {"class":"snb challenge"})
    ultag2 = soup.find("ul", {"class":"ly_lst_genre"})
    litags = []

    for litag in ultag.find_all("li"):
        litags.append(litag.find('a').text)

        ultag = soup.find("ul", {"id": "othersGenreLayer"})

        for litag in ultag2.find_all("li"):
            litags.append(litag.find('a').text)

        litags = list(map(lambda x : x.rstrip(), litags))
        litags = list(map((lambda x : ''.join(["_"+i for i in x.split()])), litags))
        litags = list(map(lambda x : x.lower(), litags))
        
        litags.remove("_home")
        litags.remove("_others")
        
    return litags


# returns popular comics based on age and sex specified. if not specified python's random module chooses
    def popularity_age(self,age=random.choice([10,20,30]),sex=random.choice(["M", "F"]), toShow=5):
        age=int(round(age/10)*10)
        if age>30:
            age=30
        else:
            pass
        sex=sex.upper()
        if sex=="M":
            sex = "MALE"
        elif sex=="F":
            sex = "FEMALE"
        elif sex=="MALE" or sex == "FEMALE":
            pass
        else:
            return "Invalid sex..!"
        url = "http://www.webtoons.com/en/top?rankingGenre=ALL&target="+sex+str(age)
        page_data=requests.get(url)
        if page_data.status_code==200:
            soup=bs(page_data.content,"html.parser")
        else:
            return page_data.status_code," :  error"
        data=soup.find_all("h3",class_="blind")
        list_data=data[1].findNextSibling('ul')
        list_of_names=list_data.find_all(class_="subj")

        toReturn = []
        for i in list_of_names:
            toReturn.append(i.get_text())

        return toReturn[:toShow]


# returns comics created by authors
# No need for param toShow practically since no author has more than 5 or so
    def author_comics(self,author):
        search_url="http://www.webtoons.com/search?keyword="+author
        search_data=requests.get(search_url)
        if search_data.status_code==200:
            soup=bs(search_data.content,'html.parser')
        else:
            return search_data.status_code, ": error"
        search_result=soup.find("ul",class_="card_lst")
        all_result=search_result.find_all(class_="subj")

        toReturn = []
        for i in all_result:
            toReturn.append(i.get_text())

        return toReturn


# returns all comics released on that day
    def new_releases(self, toShow):
        day = time.strftime("%A")
        day_sched= requests.get("http://www.webtoons.com/en/dailySchedule")
        soup=bs(day_sched.content,'html.parser')
        
        x = "daily_section _list_"+day.upper()
        ls=soup.find("div",{'class':x})


        self.s=ls.find_all(class_="subj")

        released_list=[e.get_text() for e in self.s]

        if toShow > len(released_list):
            return "Error: too many comics were requested to show, and not enough comics exist!"

        return released_list[:toShow]


# returns the top 10 comics of the day
    def top10_of_day(self):
        released=self.new_releases(12)
        toReturn = []
        for i in range(0,10):
            toReturn.append(str(i+1) + ' '+released[i])
            
        return toReturn


# returns the most popular comics. optional param toShow for how many comics to return
    def best_rated(self, toShow=5):
        page=requests.get('http://www.webtoons.com/en/top')
        soup=bs(page.content,'html.parser')
        ls=soup.find(class_="ranking_lst top")
        subjall=ls.find_all(class_="subj")

        new=soup.find(class_="lst_type1")
        for e in new.find_all('a',href=True):
            requests.get(e['href'])

        count, toReturn = 1, []
        for i in subjall:
            toReturn.append(str(count)+' ' +i.get_text())
            count+=1

        if toShow > len(toReturn):
            return "Error: too many comics were requested to show, and not enough comics exist!"

        return toReturn[:toShow]


# returns the most popular comics in a specific genre. optional param toShow for how many comics to return
    def top_in_genre(self,g,toShow=5):
        page=requests.get('http://www.webtoons.com/en/genre')
        soup=bs(page.content,'html.parser')

        g = "_".join(g.lower().split())
        gen = "_"+g

        genre = "g"+gen

        if gen not in self.genres:
            return "Genre not found. Try again"
        
        ls=soup.find(class_="sub_title "+genre)
        ul=ls.findNextSibling('ul')
        names=ul.find_all(class_="subj")
        count, toReturn = 1, []
        for i in names:
            toReturn.append(str(count)+' '+ i.get_text())
            count+=1

        if toShow > len(toReturn):
            return "Error: too many comics were requested to show, and not enough comics exist!"

        return toReturn[:toShow]
