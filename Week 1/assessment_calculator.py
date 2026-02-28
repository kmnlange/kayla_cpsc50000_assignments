'''
Kayla Lange
January 25, 2026
assessment_calculator.py

Description: 
Annual Property Tax Assessment Calculator and Purchase Advisor 
for properties located in Cook County, Illinois.
'''
print()
print("Welcome to the Cook County, Illinois Home Purchase Advisor.") 
print("This program helps you decide whether a residential home is a " \
"good purchase based on its annual property taxes.")
print()

input("Press ENTER to continue:")

print()
print("Let's start by entering some information about the property...")
print()

Value = input("Please enter the residential property's value?:")     #value?
Value = float(Value)                                       #conversion
print()
Rate = input("Please enter the local tax rate percentage for the location of the property you are interested in?:")  #Tax Rate

Rate = float(Rate)          # Conversion
decimal_value = Rate / 100      # Decimal Value

print()
input("Press ENTER to review your entries:") 

print('Your Entries:')
print()
print(f'Value of Property:      ${Value:.02f}')
print(f"Property's Local Tax Rate:    {Rate:.02f}%")
print()
input("Press ENTER to view calculated property tax:") 
print()
print('Calculating...')
print()

EAV = (Value * 0.1)*3.0355 # (Value * Assessment Level (.1)) *  State Equalizer Value (3.0355)
Annual_Tax = EAV*decimal_value # EAV * Local Tax Rate as decimal = Annual Tax

print(f'The calculated Annual Total Property Tax for this property is ${Annual_Tax:.02f}.')
print()

input("Press ENTER to view purchasing recommendation:")  

print()
print('Analyzing...')
print()

print('Based on this annual property tax, consider the following:')
print()

if Annual_Tax < 12500:
    print('Recommend Purchase Property.')
elif Annual_Tax < 18200:
    print('Further Research Needed')
else:
    print('Recommend No Purchase')

print()
print('Completed, please restart to get another recommendation.')

'''
End
'''