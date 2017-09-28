# CTI 110
# M3T1 Area of Rectangles
# Brian Gadbois
# 9/26/2017
# This program is made to determine which rectangles are bigger.

# Length * width = area of the rectangle


# Units for first rectangle
print ('Tell me how long each part is.')
L1 = float (input ('What is the length of the first rectangle:'))
Rec1 = float (input ('What is the width of the first rectangle:'))
print ('   ')

# Units for the second rectangle
print ('Now tell me how long each part of the second rectangle is.')
L2 = float (input ('What is the length of the second rectangle:'))
Rec2 = float (input ('What is the width of the second rectangle:'))
print ('   ')

# Now to find out which is bigger
print ('Now we can tell which is bigger.')

A1 = L1 * Rec1
A2 = L2 * Rec2

if A1 > A2:
    print ('The first rectangle is bigger.')
elif A2 > A1:
    print ('The second rectangle is bigger.')
elif A1 == A2:
    print ('The two rectangles are equal.')
    
