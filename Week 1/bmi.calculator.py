'''
Kayla Lange
January 25, 2026
bmi_calculator.py

Description: 
Body Mass Index Calculator by height and weight
'''
#Introduction
print()
print('Welcome to the Body Mass Index Calculator (BMI).')   
print()

input('Please press ENTER if you wish to continue:')

print()
print("Let's start by getting some information.")

print()
height_inches = input('Please enter your height in inches:')        # Height in inches
height_inches = float(height_inches)                                # Conversion to float
print()
weight_pounds = input('Please enter your weight in pounds:')        # Weight in pounds
weight_pounds = float(weight_pounds)                                # Conversion to float
print()

input('Press ENTER to review your entry:')

print()
print('Your entry:')
print()
print(f'Height:      {height_inches:.02f} inches')
print(f'Weight:      {weight_pounds:.02f} lbs')
print()

input('Please press ENTER to calculate BMI:')

print()
print('Calculating...')
print()

# BMI = weight (kg) / height (m^2)
# Research: inches => square meters: (inches * 0.0254)^2 (exponential operator **)
# Research: lbs => kg: pounds * 0.4536

meters = 0.0254
kg = 0.4536
height_meters = height_inches * meters      # Conversion to meters
height_squared = height_meters ** 2         # Conversion to square meters
weight_kg = weight_pounds * kg              # Conversion to kg

BMI = weight_kg / height_squared

print()
print(f'At a height of {height_inches:.02f} inches and a weight of {weight_pounds:.02f} lbs, '
      f'your calculated BMI is: {BMI:.02f}.')                                                      #BMI output to two decimal points
print()


if BMI <= 18.5:
    print(f'Based on your BMI of {BMI:.02f}, your BMI category is '
          'Underweight (< 18.5)')                                    # Underweight
elif BMI <= 24.9:
    print(f'Based on your BMI of {BMI:.02f}, your BMI category is '      
          'Normal Weight (from 18.5 to 24.9)')                          #normal weight
    print(f'Based on your BMI of {BMI:.02f}, your BMI category is '
        'Overweight (from 25 to 29.9')                              # Overweight
else: 
    print(f'Based on your BMI of {BMI:.02f}, your BMI category is '
          'Obese (>30)')                                              # Obese

print()
print('As a gentle reminder, this is a general estimate and '
      'should not be considered a complete measure of health.')
print('Thank you!')
print()

'''
End
'''