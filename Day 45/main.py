from bs4 import BeautifulSoup
'''lxml is another type of parser to read through HTML, in case some websites do not parse well.'''
#import lxml 

with open("100-days-of-code\Day 45\website.html", encoding="utf-8") as website:
    html = website.read()
    print(html)
    
soup = BeautifulSoup(html, 'html.parser')
#print(soup.title)
#print(soup.title.name) # prints "title"
print(soup.title.string) #prints "Angela's Personal Site"
#print(soup.prettify()) 

all_anchor_tags = soup.find_all(name="a") #This uses kwargs, you can basically search for anything here.
print(all_anchor_tags)

for tag in all_anchor_tags:
    #print(tag.getText())
    print(tag.get("href")) # Can get value of any attribute
    
heading = soup.find(name="h1",id="name") #The name of the tag is h1, and its id is "name"
print(heading)
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

company_url = soup.select_one(selector="p a")
