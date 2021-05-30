from bs4 import BeautifulSoup

#used this source.html to srape the data
with open("source.html") as fh:
    soup = BeautifulSoup(fh, 'html.parser')
#print(soup.prettify)

heading = soup.find('h1').text
print(heading)

deg_name = soup.find_all('h3', 'deg-title')
deg_subtitle = soup.find_all('h4')
deg_description = soup.find_all('p')
print("\n")

# top 5 degrees in mumbai
for i in range(5):
    print(i+1, end=". ")
    print(deg_name[i].string)
    print(deg_subtitle[i].string)
    print("Analysis : ", deg_description[i].string)
    print("\n")





