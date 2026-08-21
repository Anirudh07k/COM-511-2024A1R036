# WAP to take distance in kilometers and convert it into meters, centimeters, and millimeters
distance = float(input("Enter Distance (in kms) :- "))

mtr = distance * 1000
print("Distance in meters :- ",mtr)

cms = distance * 100000
print("Distance in Centimeters :- ",cms)

mms = distance * 1000000
print("Distance in Millimeters :- ",mms)