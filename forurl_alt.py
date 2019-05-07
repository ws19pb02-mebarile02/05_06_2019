"""
forurl_alt.py

This file is a combination of forurl.py and image.py.  It reads a .dat file
from a URL and uses enumerate to assign an ID to each line in a table with
a heading. The data is the average annual precipitation in the LA Area from
1878 to 2003.  It then reads in a .gif image of the data.

"""

import sys
import urllib.request
import tkinter

url = "http://fourier.eng.hmc.edu/e180/e101.1/e101/project_1/rain126.dat"

try:
    lines = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print(f"urllib.error.URLError: {error}")
    sys.exit(1)

head = " ID     Year   Precip."
print(head)
print(len(head)*'-')

for i, line in enumerate(lines, start = 1):
    try:
        s = line.decode("utf-8") #Convert sequence of bytes to string of characters.
    except UnicodeError as unicodeError:
        print(f"UnicodeError: {unicodeError}")
        sys.exit(1)

    s = s.rstrip("\r\n")         #Chop the trailing CRLF off of s.
    print(f"{i:3}     {s}")

lines.close()

##########################################################################

url = "http://fourier.eng.hmc.edu/e180/e101.1/e101/project_1/rain_plot.gif"

try:
    binaryFile = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print(f"urllib.error.URLError: {error}")
    sys.exit(1)

sequenceOfBytes = binaryFile.read()     #not string of characters
binaryFile.close()
#print(f"len(sequenceOfBytes) = {len(sequenceOfBytes):,}")

root = tkinter.Tk()

try:
    #The following statement cannot come before the tkinter.Tk().
    photoImage = tkinter.PhotoImage(data = sequenceOfBytes)
except tkinter.TclError as error:
    print(error)   #"couldn't recognize image data" when image is jpg or png.
    sys.exit(1)

width = photoImage.width()
height = photoImage.height()
root.geometry(f"{width}x{height}")
root.title("Los Angeles Civic Center Average Annual Precipitation")

label = tkinter.Label(root, image = photoImage)
label.pack()

root.mainloop()
sys.exit(0)
