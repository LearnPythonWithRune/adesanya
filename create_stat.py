import bs4

# Read the html file (I downloaded it - you need to change it)
with open('/Users/rune/Downloads/python_class_question.html') as f:
    html = f.read()
    
# create a soup
soup = bs4.BeautifulSoup(html, "lxml")

# create a simple data structure with data
data = []

for items in soup.select('tr'):
    day_colors = item.select('td')
    data.append({
        'day': day_colors[0].getText(),
        'colors': day_colors[1].getText().split(', ')
    })

# create a simple frequency analysis
freq = {}

for item in data:
    for color in item['colors']:
        freq[color] = freq.get(color, 0) + 1

# the content of freq
# freq:
# {'GREEN': 10,
#  'WHITE': 25,
#  'BROWN': 5,
#  'BLUE': 30,
#  'BLACK': 5,
#  'ORANGE': 5,
#  'RED': 15}
