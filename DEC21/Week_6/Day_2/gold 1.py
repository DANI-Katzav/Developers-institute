
# ex1:

print( ("Hello world \n")*4 + ('I love python \n')*4)


#ex2
# Spring runs from March (3) to May (5)
# Summer runs from June (6) to August (8)
# Autumn runs from September (9) to November (11)
# Winter runs from December (12) to February (2)
month = int(input('Enter a number of a month 1-12: '))


if month >= 3 and month <= 5 :
    print('Spring ')

elif month >= 6 and month <= 9 :
    print('Summer ')

elif month >= 9 and month <= 11 :
    print('Fall ')

else month == 12 or month <= 2 :
    print('Winter')
