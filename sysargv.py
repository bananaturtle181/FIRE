import sys

arguments = sys.argv

if len(arguments) != 3:
    sys.exit("Incorrect number of arguments provided")

try:
    price = int(arguments[1])
except ValueError:
    sys.exit("Provided price is not an integer")
try:
    discount = int(arguments[2])
except ValueError:
    sys.exit("Provided discount is not an integer")

final_price = price * (1 - discount/100)


print(price, discount, final_price)