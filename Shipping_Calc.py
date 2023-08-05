weight = 5
premium_ground = 125.00
#ground shipping
if weight <= 2:
  cost = (weight * 1.50 + 20.00)
elif weight <= 6:
  cost = (weight * 3.00 + 20.00)
elif weight <=10:
  cost = (weight * 4.00 + 20.00)
elif weight > 10:
  cost = (weight * 4.75 + 20.00)
else:
  print('Please reweigh parcel.')

print('Total ground:',cost)

#drone shipping 
if weight <= 2:
  cost = (weight * 4.50)
elif weight <= 6:
  cost = (weight * 9.00)
elif weight <=10:
  cost = (weight * 12.00)
elif weight > 10:
  cost = (weight * 14.25)
else:
  print('Please reweigh parcel.')

print('Total drone:',cost)

#ground premium is a flat rate of 125.00
print('premium ground flat fee:', premium_ground)
