class Page:
    def __init__(self):
        self.url = 'www.amazon.com'

    def open(self):
        print('Url Open', self.url)

    def close(self):
        print('Closing the page', self.url)


p = Page()

p.open()