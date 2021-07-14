import pandas as pd
import numpy as np
#import the GoogleNews Package
from GoogleNews import GoogleNews
googlenews=GoogleNews()

#keywords
keywords=['Infosys-Stock','Infosys Revenue','Infosys','Infy']
googlenews.set_time_range('01/03/2021','01/06/2021')

#dataframe to store news article infomation
article_info=pd.DataFrame(columns=['Date','Time','Title','Articles','Link'])
#gathering all data of current page to one dataframe
#function starts
def newsfeed1(article_info,raw_dictionary):
    for i in range(len(raw_dictionary)-1):
        if raw_dictionary is not None:
            #fetch date and time and convert it into datetime format
            date=raw_dictionary[i]['datetime']
            date=pd.to_datetime(date)
            #fetch title, time and source of news articles
            title=raw_dictionary[i]['title']
            time=raw_dictionary[i]['date']
            articles=raw_dictionary[i]['desc']
            link=raw_dictionary[i]['link']
            #append all above information in single dataframe
            article_info=article_info.append({'Date':date,'Time':time,'Title':title,
            'Articles':articles,'Link':link},ignore_index=True)
        else:
            break

    return article_info
#function ends

#dataframe containing the news of all the keywords searched
articles=pd.DataFrame()
#each keyword will be searched seperately and results will be saved in a dataframe
for steps in range(len(keywords)):
    string=(keywords[steps]) 
    googlenews.search(string) 

    #fetch the results
    result=googlenews.results()
    #number of pages
    total_pages=1

    for steps in range(total_pages):
        googlenews.get_page(steps)
        feed=newsfeed1(article_info, result)
    
    articles=articles.append(feed)
    #clear off the search results of previous keyword to avoid duplication
    googlenews.clear()

shape=articles.shape[0]

#resetting index of final result
articles.index=np.arange(shape)
print(articles)
