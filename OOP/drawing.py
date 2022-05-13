class Drawing:
    def __init__(self, row, column, symbol):
        self.row = row
        self.column = column
        self.symbol = symbol
        self.image = []
        for _ in range(self.column):
            self.image.append([symbol] * row)
        self.img_column = [symbol] * column

    def print(self):
        for x in self.image:
            print(*x)

    def setPoint(self, x, y, char):
        self.image[y - 1][x - 1] = char

    def drawVerticalLine(self, column, y1, y2, char):
        for i in range(y1, y2 + 1):
            self.image[i - 1][column - 1] = char

    def drawHorizontalLine(self, row, x1, x2, char):
        for i in range(x1, x2 + 1):
            self.image[row - 1][i - 1] = char

    def drawRectangle(self, x1, y1, x2, y2, char):
        for i in range(y1, y2 + 1):
            self.image[i - 1][x1 - 1] = char
        for i in range(x1, x2 + 1):
            self.image[y1- 1][i - 1] = char
        for i in range(y1, y2 + 1):
            self.image[i - 1][x2 - 1] = char
        for i in range(x1, x2 + 1):
            self.image[y2 - 1][i - 1] = char

def Home():
    home = Drawing(20, 10, ' ')
    home.drawRectangle(5, 6, 15, 10, '*')
    home.drawRectangle(9, 7, 11, 10, '*')
    home.setPoint(6, 5, '*')
    home.setPoint(7, 4, '*')
    home.setPoint(8, 3, '*')
    home.setPoint(9, 2, '*')
    home.setPoint(10, 1, '*')
    home.setPoint(11, 2, '*')
    home.setPoint(12, 3, '*')
    home.setPoint(13, 4, '*')
    home.setPoint(14, 5, '*')
    home.print()
Home()

img = Drawing(5, 5, '.')
img.setPoint(5, 3, 'x')
img.setPoint(1, 3, 'a')
img.drawVerticalLine(1, 3, 5, '+')
img.drawHorizontalLine(2, 2, 5, '/')
img.drawHorizontalLine(3, 1, 3, '*')
img.drawVerticalLine(4, 2, 3, 'o')
img.drawRectangle(2, 2, 4, 5, '-')
img.print()
