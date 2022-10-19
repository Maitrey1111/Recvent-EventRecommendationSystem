from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd


driver = webdriver.Firefox(executable_path=r'./website/static/geckodriver.exe')
driver.maximize_window() 
driver.implicitly_wait(8) 


url='https://insider.in/online'


driver.get(url)

driver.find_element(By.CLASS_NAME, 'css-ysxxom').click()
driver.implicitly_wait(2)

driver.find_element(By.CLASS_NAME, 'css-1rueteo').click()
driver.implicitly_wait(2)
event_list=[]
citylist=[]
# description_links=[]
# citylinklist=[]

# Code to get All the names of cities and store it in citylist[]:
i=1
cities=driver.find_elements(By.CLASS_NAME, "css-71g95z")
for city in cities:
    xpcity='//*[@id="city-selector"]/div[2]/ul/li['+ str(i) +']/a'
    newcity=city.find_element("xpath", xpcity).text
    citylist.append(newcity)
    # citylink=city.get_attribute("href")
    # citylinklist.append(citylink)
     # citylist
    i=i+1
# print(citylink,citylinklist)
print(len(citylist))














for j in citylist:
    
    url='https://insider.in/all-events-in-'+(j.lower())+'?type=physical'
    # url=j
    driver.get(url)

    # driver.find_element(By.CLASS_NAME, 'css-pehcxo').click() ----> Used for Websites when linnk wasnt directly appended
    
    

    


    # text = driver.find_element_by_xpath('//*[@id="there-you-go"]/div').text------------> trial
    # print(text)------>trial
    





# Code to scroll to bottom of the page :

    try:
        time. sleep(4)
        previous_height = driver.execute_script('return document.body.scrollHeight')

        while True:
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time. sleep (4)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == previous_height:
                break 
            previous_height = new_height

        events = driver.find_elements(By.CLASS_NAME, "css-nro8na")
        # css-nro8na -----> All the Events Come under this Class... Use it to Capture all events.... all xp$ define the subclasses of each attribute
        
        i=1
        for event in events:
            xptitle = '//*[@id="there-you-go"]/div/div[2]/div/div[3]/div/ul/div/li['+ str(i) +']/div/a/div[2]/div[1]/div/span'
            xpvenue = '//*[@id="there-you-go"]/div/div[2]/div/div[3]/div/ul/div/li[' + str(i) +']/div/a/div[2]/div[1]/span[2]'
            xpprice = '//*[@id="there-you-go"]/div/div[2]/div/div[3]/div/ul/div/li['+ str(i) +']/div/a/div[2]/div[2]/div[1]'
            xpgenre = '//*[@id="there-you-go"]/div/div[2]/div/div[3]/div/ul/div/li['+ str(i) +']/div/a/div[1]/span'
            xplink = '//*[@id="there-you-go"]/div/div[2]/div/div[3]/div/ul/div/li['+ str(i) +']/div/a[@href]'

            title = event.find_element("xpath", xptitle).text
            venue = event.find_element("xpath", xpvenue).text
            price = event.find_element("xpath", xpprice).text
            genre = event.find_element("xpath", xpgenre).text
            link = event.find_element("xpath", xplink)
            linka = link.get_attribute("href")


            
            
            # print(title,venue,price,genre)---- Trial: Following line creates a list that is published as csv
            event_item = {
                'title': title,
                'city': (j.lower()),
                'venue': venue,
                'price':price,
                'genre':genre,
                'link':linka,
                'description':"des"
            }
            
            #Array to store all events till now(all cities)
            event_list.append(event_item)
            # description_links.append(linka)
            i=i+1






        # time.sleep(3)
        # element=driver.find_element("name", "body" )
        # while True:
        #     element.send_keys(Keys.PAGE_DOWN)
        #     time.sleep(3)


        


       
        

        # j=0
        # for j<length(citylist)
        #     print(citylist[j],citylinklist[j])
        #     j=j+1
    except Exception:
        pass


print(len(event_list))

n=2

for j in range(len(event_list)):
    try:
        k=event_list[j].get('link')
        driver.get(k)
        for n in range(5): 
            try:
                f='//*[@id="react-tabs-1"]/div/section['+str(n)+']'
                eventdescription= eventdescription+driver.find_element("xpath",f).text   
            except Exception:
                pass
             
            event_list[j].update({'description':eventdescription})
    except Exception:
        pass   
df = pd.DataFrame(event_list)
df.to_csv('data1.csv')



# Troublemakes:    https://insider.in/loud-cloud-i-music-and-food-festival-i-kolkata-oct15-2022/event...............experimentation in new.py




# df = pd.DataFrame(event_list)
        
# # print(df)
# df.to_csv("table.csv")  

# descriptionset=[]

# for j in description_links:
#     driver.get(j)
#     description=driver.find_element("xpath",'//*[@id="react-tabs-1"]/div/section[3]').text + driver.find_element("xpath",'//*[@id="react-tabs-1"]/div/section[4]').text
#     descriptionitem={
#         'link':j,
#         'description':description
#     }
#     descriptionset.append(descriptionitem)
#     df2=pd.DataFrame(descriptionset)
#     df2.to_csv('descr.csv')


driver.quit()
