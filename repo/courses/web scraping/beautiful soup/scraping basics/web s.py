from bs4 import BeautifulSoup

with open('back up\web scraping\scraping basics\home.html', 'r') as html_file:
    content = html_file.read()
    #print(content)
   
    soup = BeautifulSoup(content, 'lxml')
    #print(soup.prettify())
    #tags = soup.find('h5') searches just the first
    #course_html_tags = soup.find_all('h5')
    #for course in course_html_tags:
    #    print(course.text)
     
    course_cards = soup.find_all('div', class_='card')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text
        
        print(course_name)
        print(course_price)
