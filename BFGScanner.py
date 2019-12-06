from urllib.request import urlopen
from html.parser import HTMLParser


class TitleParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.match = False
        self.title = ''

    def handle_starttag(self, tag, attributes):
        self.match = True if tag == 'title' else False

    def handle_data(self, data):
        if self.match:
            self.title = data
            self.match = False
i=1
while i < 5630:
 try:
    url = 'http://forums.bigfishgames.com/forums/show/{}.page'.format(i)
    html_string = str(urlopen(url).read())

    parser = TitleParser()
    parser.feed(html_string)
    print(parser.title)
 except Exception:
    print ("ERROR - " + str(i))
 i=i+1

