from selenium import webdriver
import time
import random
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import re
from geopy.geocoders import Nominatim
import uuid
import urllib

def elmo_scrap(url):
        
    try:
        nom = Nominatim(user_agent="elmo")
        ID_restaurant = str(uuid.uuid4())
        path = '/run/user/1000/gvfs/smb-share:server=nas.local,share=projets/restaurants/'
    
        driver = webdriver.Chrome()
        
        driver.get(url)
        try : 
            img = driver.find_element_by_css_selector(".large_photo_wrapper > div:nth-child(1) > div:nth-child(1) > img:nth-child(1)")
            
            src = img.get_attribute('src')
        
            urllib.request.urlretrieve(src, path + 'images/' + ID_restaurant +".jpeg")
        except:
            pass
        time.sleep(6)
        
        page = driver.page_source
        soup = BeautifulSoup(page,"lxml")
        
        restaurant = soup.findAll('h1',{"data-test-target":'top-info-header'})[0].text
        extended_address = soup.findAll('a',{'class': '_15QfMZ2L'})[1].text
        try :
            ticket_moyen_resto = re.findall(r'\d+[€]\s[-]\s\d+[€]',str(soup.findAll("div")))[0]
        except :
            ticket_moyen_resto = "NA"
            
        
        try :
            nb_pages = len(soup.findAll("div",{"class":"pageNumbers"})[0])
        except:
            nb_pages = 1
        mapping = nom.geocode(extended_address)
        
        if mapping == None:
            gps = "NA"
        else :
            gps = (mapping.latitude, mapping.longitude)
        df = []
        df1 = []
        if nb_pages < 1 :
            
        
            
            for i in range(nb_pages-1):
                    page_temp = driver.page_source
                    page_temp_soup = BeautifulSoup(page_temp,'html.parser')
                    time.sleep(3)
                    driver.execute_script("window.scrollTo(0,1000)")
                    time.sleep(1)
                    try :
                        driver.find_element_by_css_selector('.ulBlueLinks').click()
                    except :
                        pass
                    time.sleep(random.random() * random.randint(6,15))
                    page_temp_loaded = BeautifulSoup(driver.page_source,'html.parser')
                    containers = page_temp_loaded.findAll("div",{"class":"review-container"})
            
            
                    reviews = []
                    for container in containers:
                        review = container.find('p',{'class':'partial_entry'}).text
                        review_title = container.find('span',{'class':'noQuotes'}).text
                        review_rating = container.select('.ui_bubble_rating')
                        review_date = container.find('span',{'class':'ratingDate'}).text
                        if container.select('.pointer_cursor div') == []:
                            review_author = container.select('.info_text div')
                        else:
                            review_author = container.select('.pointer_cursor div')
                        
                        
                        reviews_item = {
                            'review_title' : review_title,
                            'review' : re.sub("\s+"," ",review),
                            'rating' : re.findall(r'\d+',review_rating[0]['class'][1])[0],
                            'author' : review_author[0].text,
                            'date' : review_date.replace('Avis écrit le ','')
                        }
                
                        reviews.append(reviews_item)
                    df = pd.DataFrame(reviews)
                    df1.append(df)
                    next_url_part = page_temp_soup.select('#taplc_location_reviews_list_resp_rr_resp_0 .primary')[1]['href']
                    next_url = "https://www.tripadvisor.fr" + next_url_part
                    driver.get(next_url)
                    
                
            page_temp = driver.page_source
            page_temp_soup = BeautifulSoup(page_temp,'html.parser')
            time.sleep(3)
            driver.execute_script("window.scrollTo(0,1000)")
            time.sleep(1)
            try :
                driver.find_element_by_css_selector('.ulBlueLinks').click()
            except :
                pass
            time.sleep(random.random() * random.randint(6,15))
            page_temp_loaded = BeautifulSoup(driver.page_source,'html.parser')
            containers = page_temp_loaded.findAll("div",{"class":"review-container"})
        
        
            reviews = []
            for container in containers:
                review = container.find('p',{'class':'partial_entry'}).text
                review_title = container.find('span',{'class':'noQuotes'}).text
                review_rating = container.select('.ui_bubble_rating')
                review_date = container.find('span',{'class':'ratingDate'}).text
                if container.select('.pointer_cursor div') == []:
                    review_author = container.select('.info_text div')
                else:
                    review_author = container.select('.pointer_cursor div')
                
                
                reviews_item = {
                    'review_title' : review_title,
                    'review' : re.sub("\s+"," ",review),
                    'rating' : re.findall(r'\d+',review_rating[0]['class'][1])[0],
                    'author' : review_author[0].text,
                    'date' : review_date.replace('Avis écrit le ','')
                }
        
                reviews.append(reviews_item)
                df = pd.DataFrame(reviews)
            df1.append(df)
                    
            driver.quit()
            data = pd.concat(df1)
            data["latitude"],data["longitude"],data["adresse"],data["ID_restaurant"],data["ticker_moyen_resto"] = gps[0],gps[1], extended_address, ID_restaurant, ticket_moyen_resto
        
        else :
            page_temp = driver.page_source
            page_temp_soup = BeautifulSoup(page_temp,'html.parser')
            time.sleep(3)
            driver.execute_script("window.scrollTo(0,1000)")
            time.sleep(1)
            try :
                driver.find_element_by_css_selector('.ulBlueLinks').click()
            except :
                pass
            time.sleep(random.random() * random.randint(6,15))
            page_temp_loaded = BeautifulSoup(driver.page_source,'html.parser')
            containers = page_temp_loaded.findAll("div",{"class":"review-container"})
        
        
            reviews = []
            for container in containers:
                review = container.find('p',{'class':'partial_entry'}).text
                review_title = container.find('span',{'class':'noQuotes'}).text
                review_rating = container.select('.ui_bubble_rating')
                review_date = container.find('span',{'class':'ratingDate'}).text
                if container.select('.pointer_cursor div') == []:
                    review_author = container.select('.info_text div')
                else:
                    review_author = container.select('.pointer_cursor div')
                
                
                reviews_item = {
                    'review_title' : review_title,
                    'review' : re.sub("\s+"," ",review),
                    'rating' : re.findall(r'\d+',review_rating[0]['class'][1])[0],
                    'author' : review_author[0].text,
                    'date' : review_date.replace('Avis écrit le ','')
                }
        
                reviews.append(reviews_item)
                df = pd.DataFrame(reviews)
            df1.append(df)
                    
            driver.quit()
            data = pd.concat(df1)
            data["latitude"],data["longitude"],data["adresse"],data["ID_restaurant"],data["ticker_moyen_resto"] = gps[0],gps[1], extended_address, ID_restaurant, ticket_moyen_resto
        
        data.to_csv(path + 'data/' + restaurant +'.csv', sep='\t', encoding= 'utf-8', index=False) 
    except:
        driver.quit()                
        f = open("failed.txt","a+")
        f.write("\n" + url)
   
    
   

