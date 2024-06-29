# 10. Celcious to farenhite

def celsiustofarenheit(celsius):
    fareheit = (9/5)*celsius + 32
    
    print("The Fahrenheit equivalent of input celsius  in degree = ", fareheit)

# input celsius degree temperature    
celsius_temp = float(input("Enter the value of celsius:"))      

'''# calling convertCelsiustoFahrenheit() function by passing
# the input celsius as an argument'''

fahrenheit_temp = celsiustofarenheit(celsius_temp)     

