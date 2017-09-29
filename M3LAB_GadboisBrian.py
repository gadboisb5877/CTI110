# CTI 110
# M3LAB Debugging
# 9/28/2017
# Fixing a half made program.
# Gadbois


'''
def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    # TO DO: define the rest of the scores

    
    score = int (input('Enter grade: '))

    if score >= A_score:
        print('Your grade is: A')
    else:
        if score >= B_score:
            print('Your grade is: B')
        else:
            if score >= C_score:
                print('Your grade is: C')
            else:
                if score >= D_score:
                    print('Your grade is:D')
                else:
                    print('You have failed. You received an F.')
'''

def main ():
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60

    score = float (input('Enter grade: '))

    if score >= A_score:
        print ('Your grade is: A')
    elif score >= B_score:
        print ('Your grade is: B')
    elif score >= C_score:
        print ('Your grade is: C')
    elif score >= D_score:
        print ('Your grade is: D')
    elif score:
        print ('You have failed. You recieved an F.')




# program start
main()
main()
main()
main()
main()
