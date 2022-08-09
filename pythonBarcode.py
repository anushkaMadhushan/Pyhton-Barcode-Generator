
import numbers
from unicodedata import name
from barcode import EAN13
from barcode.writer import ImageWriter

num_of_barcode = int(input("How many barcode do you need?"))
number = range(num_of_barcode)
for i in number:
    id =input("Enter 12-Digit Number for your id: ")
    my_code = EAN13(id,ImageWriter)
    name = input("Enter the name Of Your Barcode: ")
    my_code.save(name)

    
