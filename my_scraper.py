import requests


url = 'https://www.dmacc.edu/schedule/Pages/result.aspx?Term=201903&Campus1;4&S'
response = requests.get(url)
html = response.content
f = open("requestResult.txt","w+")
f.writelines(str(html))
f.close()


soup = bs.BeautifulSoup(open("requestResult.txt"), 'html.parser')
print(soup.prettify())