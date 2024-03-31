from datetime import datetime

print("----------------------------Welcome---------------------------")
name=input("enter your  name:")
#list of items
lists='''
Rice     Rs   20/kg
Sugar    Rs   30/kg
Salt     Rs   20/kg
Oil      Rs   80/Liter
Panner   Rs   110/kg
Maggi    Rs   50/kg
Boost    Rs   90/Each
Colgate  Rs   85/each
'''
#declaration
price=0
pricelist=[]
totalprice=0
finalamount=0
ilist=[]
qlist=[]
plist=[]

#rates for items
items={'Rice':20,
       'Sugar':30,'Salt':20,'Oil':80,
       'Panner':110,'Maggi':50,
       'Boost':90,'Colgate':85}

option=int(input("For list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("If you want to buy press1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("enter your items:")
        quantity=int(input("enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you enered item is not available")
    else:
        print("you entered wrong number")
    inp=input("Can i bill the items yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","Radhe SuperMarket",25*"=")
            print(28*" ","Wanaparthy")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",6*" ",'items',8*" ",'quantity',8*" ",'price')
            for i in range(len(pricelist)):
                print(i,8*' ',5*' ',ilist[i],3*' ',qlist[i],8*" ",plist[i])
            print(75*"-")    
            print(50*" ",'TotalAmount:','Rs',totalprice)
            print("gstAmount:",40*" ",'Rs',gst)
            print(75*"-")
            print(50*" ",'finalAmount:','Rs',finalamount)
            print(75*"-")
            print(20*" ","Thanks for visiting")
            print(75*"-")
          







