#. Write a program that converts Fahrenheit to Centigrade

def celsiustofarenheit(fareheit):
    celsius = ((fareheit-32)*5)/9
    
    
    print("The celsius degree equivalent of input Fahrenheit = ", celsius)

# input celsius degree temperature    
fahrenheit_temp = float(input("Enter the value of fareheit:"))      

'''# calling convertFahrenheitoCelsiust() function by passing
# the input fareheit as an argument'''

celsius_temp = celsiustofarenheit(fahrenheit_temp) 
