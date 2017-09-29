# CTI-110 
# M3HW1 - Age Classifier 
# Brian Gadbois 
# 9/29/2017
# This program was made to describe people's ages and classify them.

def main():

    infant = 1
    child = 13
    teenager = 20
    adult = 45
    oldFart = 80


    age = float (input('How old are you?'))

    if age <= infant:
        print ('How is an infant able to work this computer?')
    elif age < child:
        print ('Then you are a young child.')
    elif age < teenager:
        print ('You''re probably a bratty teenager.')
    elif age <= adult:
        print ('You''re probably a crappy adult.')
    elif age < oldFart:
        print ('You have now reached old fart status now.')
    elif age >= oldFart:
        print ('You''re not just an old fart anymore, you are what is called old.')





main()
main()
main()
main()
main()
main()
