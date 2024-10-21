#PINEDA SOPHIA KEZIAH G. ICT - 107 | CONVERSION OF DIFFERENT MEASUREMENTS | FINALS ACTIVITY  

value = int(input("Input value: "))
conversion = input("Conversion Type [1-8]: ")

if conversion == '1':
    #Celsius to Fahrenheit
    def celsius_to_fahrenheit(celsius):
        fahrenheit = round((celsius * 1.8) + 32)
        print(f'{celsius} Celsius is equivalent to: {fahrenheit} Fahrenheit')
    
    celsius_to_fahrenheit(value)

elif conversion == '2':
    #Fahrenheit to Celsius
    def fahrenheit_to_celsius(fahrenheit):
        celsius = round((fahrenheit - 32) / 1.8)
        print(f'{fahrenheit} Fahrenheit is equivalent to: {celsius} Celsius')
    
    fahrenheit_to_celsius(value)

elif conversion == '3':
    #Centimeter to Meter
    def centimeter_to_meter(centimeter):
        meter = centimeter // 100  
        print(f'{centimeter} Centimeters is equivalent to: {meter} Meter')
    
    centimeter_to_meter(value)

elif conversion == '4':
    #Meter to Centimeter
    def meter_to_centimeter(meter):
        centimeter = meter * 100
        print(f'{meter} Meters is equivalent to: {centimeter} Centimeters')
    
    meter_to_centimeter(value)

elif conversion == '5':
    #Meter to Kilometer
    def meter_to_kilometer(meter):
        kilometer = meter // 1000  
        print(f'{meter} Meters is equivalent to: {kilometer} Kilometers')
    
    meter_to_kilometer(value)

elif conversion == '6':
    #Kilometer to Meter
    def kilometer_to_meter(kilometer):
        meter = kilometer * 1000
        print(f'{kilometer} Kilometers is equivalent to: {meter} Meters')
    
    kilometer_to_meter(value)

elif conversion == '7':
    #Grams to Kilograms
    def grams_to_kilogram(grams):
        kilogram = grams // 1000  
        print(f'{grams} Grams is equivalent to: {kilogram} Kilograms')
    
    grams_to_kilogram(value)

elif conversion == '8':
    #Kilograms to Grams
    def kilogram_to_grams(kilogram):
        grams = kilogram * 1000
        print(f'{kilogram} Kilograms is equivalent to: {grams} Grams')
    
    kilogram_to_grams(value)

else:
    print("Invalid input. Please enter a conversion type [1-8]")
