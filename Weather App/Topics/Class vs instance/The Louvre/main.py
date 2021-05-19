class Painting:

    museum = 'Louvre'

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

    def print(self):
        print(f'"{self.title}" by {self.artist} ({self.year}) hangs in the {self.museum}.')


current_paint = Painting(input(), input(), input())
current_paint.print()
