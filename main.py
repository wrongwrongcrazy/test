from bs4 import BeautifulSoup
import lxml

with open("trungquandev.html") as file:
    content = file.read()
soup = BeautifulSoup(content, "html.parser")
print(soup.prettify())