# WAP to convert temperature from Celcius to Farenheit
# Formula: F = (C * 9/5) + 32

def celcius_to_farenheit(celcius):
    farenheit = (celcius * 9/5) + 32
    return farenheit

celcius = int(input("Enter temperature in Celcius : "))
farenheit = celcius_to_farenheit(celcius)
print("Temperature in Farenheit is : ", farenheit)

