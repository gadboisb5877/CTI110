# CTI-110
# M3HW2 - Software Sales
# Brian Gadbois
# 10/5/2017
# This programs totals up all the packages and decides if you need a discount.

def main():

    package = 99

    #This area is to find out the total before possible discounts.
    print ("The software package costs $99.")
    quantity = float (input ('How many packages have you bought?'))
    print ('  ')

    subTotal = package * quantity
    print ('Your total will be', subTotal)
    print ('   ')

    # To find out whether or not you should have discounts or not.
    if quantity >= 100:
        discount = 0.40
        print ('Your discount will be 40%.')
    elif quantity >= 50:
        discount = 0.30
        print ('Your discount will be 30%.')
    elif quantity >= 20:
        discount = 0.20
        print ('Your discount will be 20%.')
    elif quantity >= 10:
        discount = 0.10
        print ("Your discount will be 10%.")
    elif quantity < 10:
        discount = 0
        print ('No discount')

    # The final price with discounts.
    discountPrice = subTotal * discount
    Total = subTotal - discountPrice
    print ("Your grand total will be", Total)






main()
main()
main()
main()
main()

