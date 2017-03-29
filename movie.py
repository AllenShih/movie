import csv
class Movie:
    def __init__(self, title, genres, time, href):
        self.title = title
        self.genres=genres
        self.time=time
        self.href=href
        self.Temp=''
        for genre in self.genres:
            self.Temp+=genre.text+' '
    
    def print_all(self):
        print('Title:'+self.title)
        print('Time:'+self.time)
        print('Genre:'+self.Temp)
        print('URL:'+self.href)
    def createCSV(self,w):
        temp=[self.title,self.time,self.Temp,self.href]
        w.writerow(temp)
    def __str__(self):
        return 'movie'
