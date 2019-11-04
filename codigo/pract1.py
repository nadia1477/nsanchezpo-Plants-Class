
import pandas as pd
from selenium import webdriver
from urllib.request import urlretrieve
pages = 1400
labels = []
total = []
driver = webdriver.Chrome(r"C:\Users\14\Downloads\chromedriver_win32/chromedriver.exe")  

for page in range(1,pages):

    url = "http://companionplants.com/catalog/product_info.php?products_id=" + str(page) 
    
    driver.get(url)
            
    for tag in range(1):
        
        item = len(driver.find_elements_by_xpath('//h1'))
        
        if(item > 1 ):
            tabla = (driver.find_element_by_class_name('main')).text
            t  = tabla.count("Average")
            t2 = tabla.count('Uses')
                  
            if(t == 1 & t2 == 1):
                imagen = driver.find_element_by_class_name('main')
                images = imagen.find_elements_by_tag_name('img')
                
                for image in images:
                    src =(image.get_attribute('src'))
                    
                      
                Name = driver.find_element_by_xpath('//*[@id="story"]/table/tbody/tr/td/form/table/tbody/tr[1]/td/table/tbody/tr/td[1]/h1').text
                for char in Name:
                    if char in ("!@#$%^&*()[]{};:,./<>?\|`~-=_+\""):
                        Name = Name.replace(char,'')
        
                Price = driver.find_element_by_xpath('//*[@id="story"]/table/tbody/tr/td/form/table/tbody/tr[1]/td/table/tbody/tr/td[2]').text
                Lighting_Conditions = driver.find_element_by_xpath('//*[@id="story"]/table/tbody/tr/td/form/table/tbody/tr[3]/td/table[3]/tbody/tr/td/font').text       
                Category = driver.find_element_by_xpath('//*[@id="story"]/table/tbody/tr/td/form/table/tbody/tr[3]/td/table[1]/tbody/tr/td/font').text
                Longevity = driver.find_element_by_xpath('//*[@id="story"]/table/tbody/tr/td/form/table/tbody/tr[3]/td/table[2]/tbody/tr/td/font').text
                Average_Height = driver.find_element_by_xpath('//*[@id="story"]/table/tbody/tr/td/form/table/tbody/tr[3]/td/table[4]/tbody/tr/td/font').text
                Uses = driver.find_element_by_xpath('//*[@id="story"]/table/tbody/tr/td/form/table/tbody/tr[3]/td/table[5]/tbody/tr/td/font').text                              
                imagen = urlretrieve(src,  Name+ '.jpg')
                new = ((Name,Price,Category,Lighting_Conditions,Longevity,Average_Height,Uses,src))
                labels.append(new)

    df = pd.DataFrame(labels,columns=['Name','Price','Category','Lighting_Conditions','Longevity','Average_Height','Uses','Imagen'])
    df.to_csv('plantas.csv')
driver.close()

    
 