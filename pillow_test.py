from PIL import Image
import math
def make_position_map_cartesian (image): #give simple cartesian coordinates for the pixels. Hoping to give (row, column)
    size = image.size
    rows, cols = size
    arr = [[(i, j) for j in range(cols)] for i in range(rows)]
    return arr
    #dlist = list(data) # note, might be needed, x.getdata() gives an internal data type, not an actual list\

def make_position_map_radial (image): #Create the much more painful radial representation in cartesian coordinates. Hoping to give (radius, angle). measuring radius from the center
    size = image.size
    rows, cols = size
    midpoint = (rows/2.0, cols/2.0)
    distance = [[math.sqrt((i - midpoint[0])**2 + (j - midpoint[1])**2)  for j in range(cols)] for i in range(rows)] #Create array of distances for calculation of the angle using distance formula
    arr = [[(distance[i][j], math.acos((j-midpoint[1])/distance[i][j]))  for j in range(cols)] for i in range(rows)] #Find angle using acos(x/r) = theta
    return arr
    
class tIm: #tIm == "Ty's image"
    def __init__(self, image_name, choice):
        self.image = Image.open(image_name)
        if choice == 'c':
            self.position = make_position_map_cartesian(self.image)
        if choice == 'r':
            self.position = make_position_map_radial(self.image)



im = tIm("./pillow/images/trance.jpg", 'r')
print(im.image.format, im.image.size, im.image.mode)
data = im.image.getdata()
print(im.position)
print(im.image.format, im.image.size, im.image.mode)
