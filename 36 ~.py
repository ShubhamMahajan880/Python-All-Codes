import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.magicbricks.com/flats-in-vadodara-for-sale-pppfs?mbtracker=google_paid_brand_desk_vadodara&ccode=brand_sem&gclid=Cj0KCQjwyOuYBhCGARIsAIdGQROElOaUgMTGYnUE-MFzG5_GTy7O6Ocl7Y3OZaXXLBFV20-e88z0yjsaAm7DEALw_wcB")
print(response)#<Response [200]> it means that i can go eith scrapping part of it
#print(response.content)
print(response.status_code)#200 (Uses for varification that site is exist corrwectly or not)
soup = BeautifulSoup(response.content,"html.parser")
print(soup)# It shows the entire html code
print(soup.prettify())# This prettify command provide us the entire html content with proper indentation

srp = soup.find("div",attrs={"class":"mb-srp__left"})
print(srp)


 





             
