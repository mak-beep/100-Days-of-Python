from bs4 import BeautifulSoup

# import lxml

with open(file="website.html", encoding='utf-8') as page:
    content = page.read()
    # print(content)

soup = BeautifulSoup(content, 'html.parser')

# if for some website html parser is not working, use xml parser
# soup = BeautifulSoup(content, 'lxml')

# print(soup.title.string)
# print(soup.prettify())

all_anchor_tags = soup.find_all(name ='a')
# print(all_anchor_tags)

for tag in all_anchor_tags:
    # text = tag.text
    text = tag.get_text()
    link = tag.get("href")
    # print(link)

heading = soup.find(name="h1", id="name")
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

# using CSS selectors
# for an anchor tag that is in a p tag
company_url = soup.select_one(selector="p a")
# for an id
name = soup.select_one(selector="#name")
print(name)