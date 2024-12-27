def calculate(mile,minute,surge):
    base_fare=2.50
    if mile>0:
        c=1.50*mile
        print("$",c,"for",mile,"miles")
    else:
        raise ValueError("mile can't be less than zero")
    if minute>0:
        m=0.25*minute
        print("$",m,"for",minute,"minutes")
    else:
        raise ValueError("minutes can't be less than zero")
    tot=(base_fare+c+m)*surge
    print("$",tot,"for your travel")
try:
    mile=float(input("Enter the miles:"))
    minute=int(input("Enter the minutes:"))
    surge=float(input("Enter the surge:"))
    calculate(mile,minute,surge)
except ValueError as e:
    print(e)


def cal(base_price,discount,tax):
    if base_price>0:
        print("The original price of the product:$",base_price)
    else:
        raise ValueError("base price can't be zero or less than zero")
    if discount>0:
        print("Your discount is",discount,"%")
    elif discount==0:
        print("there is no discount")
    else:
        raise ValueError("discount can't be less than zero")
    if tax>0:
        print("Your tax is",tax,"%")
    elif tax==0:
        print("there is no tax")
    else:
        raise ValueError("tax can't be less than zero")
    discount_amount=base_price*(discount/100)
    price_after_discount=base_price-discount_amount
    tax_amount=price_after_discount*(tax/100)
    price=price_after_discount+tax_amount
    print("The total price of your product is $",price) 
try:
    base_price=float(input("Enter the base price:"))
    discount=float(input("Enter the discount percentage:"))
    tax=float(input("Enter the tax percentage:"))
    cal(base_price,discount,tax)
except ValueError as e:
    print(e)



    
