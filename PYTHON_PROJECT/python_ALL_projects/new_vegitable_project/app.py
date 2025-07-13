'''
shopkeeper:-
1.Add
2.Remove
3.Update

Customer:-
1.One person can buy multiple vegetables in a single bill.
2.Report
    ->Profit
    ->Item wise profit'''

print(''*10,'WELCOME TO V CUBE VEGETABLE MARKET',''*10)
vegetable=['TOMATO','POTATO','BRINJAL','CHILLI','COULIFLOWER','SNAKEGUARD','DRUMSTICK','CABBAGE','BEETROOT','CARROT']
stock=[12,50,15,10,25,10,5,20,18,14]
cost=[13,22,25,75,50,39,133,15,27,32]
sell=[20,30,30,90,60,50,150,20,35,40]
names=[]
mobile=[]
S_No=[]
profit=0
icart=[]
iweight=[]
iprofit=[]
while True:
    print()
    print('1.shopkeeper')
    print('2.customer')
    ch=int(input('Select your option:'))
    if ch==1:
        while True:
            user_name=input('Enter the User Id to get the access as shopkeeper: ')
            password=input('Enter the password: ')
            if user_name=='12345' and password=='Ashi@123':
                break
            else:
                print('Invalid User Id and password..!')
        while True:
            print()
            print('1.Add an item')
            print('2.Remove an item')
            print('3.Update/Modify an item')
            print('4.View Inventory')
            print('5.View user details')
            print('6.Report')
            print('7.Exit')
            op=int(input('choose your operation: '))
            if op==1:
                while True:
                    while True:
                        veg=input('Which vegetable you want to add?: ').upper()
                        if veg.isalpha():
                            vegetable.append(veg)
                            print(veg,'is added to Inventory data')
                            break
                        else:
                            print('Please enter a valid vegetable name..!')
                    while True:        
                        qnt=float(input('How much quantity you want to add?: '))
                        if qnt>0:
                            stock.append(qnt)
                            print(qnt,'kgs of',veg,'is added to Inventory data')
                            break
                        else:
                            print('Please enter valid quantity..!')
                    while True:
                        c_price=float(input('Enter the cost price of vegetable?: '))
                        if c_price>0:
                            cost.append(c_price)
                            print(c_price,'Rs. cost price of',veg,'is added to Inventory data')
                            break
                        else:
                            print('Enter valid cost price..!')
                    while True:
                        s_price=float(input('Enter the selling price of vegetable?: '))
                        if s_price>0:
                            sell.append(s_price)
                            print(s_price,'Rs.sell price of',veg,'is added to Inventory data')
                            break
                        else:
                            print('Enter valid selling price..!')
                    ve= input('Do you want to add more vegetable(yes/no)?: ')
                    if ve=='no':
                        break
            elif op==2:
                while True:
                    v=input('Which vegetable you want to remove?: ').upper()
                    if v.isalpha():
                        if v in vegetable: 
                            idx=vegetable.index(v)
                            vegetable.pop(idx) 
                            stock.pop(idx)
                            cost.pop(idx)
                            sell.pop(idx)
                            print(v,'is removed from inventory')
                            break
                        else:
                            print('Vegetable is not available in inventory')
                    else:
                        print('Please enter valid name..!')

            elif op==3:
                while True:
                    up=input('Which vegetable you want to modify?: ').upper()
                    if up.isalpha():
                        break
                    else:
                        print('Please enter a valid vegetable name..!')
                if up in vegetable: 
                    idx=vegetable.index(up)
                    while True:
                        v=input('Enter new vegetable: ').upper()
                        if v.isalpha():
                            vegetable[idx]=v
                            print(up,'is successfully modified with',v)
                            break
                        else:
                            print('Please enter a valid vegetable name..!!')
                    while True:
                        q=float(input('Enter new quantity: '))
                        if q>0:
                            stock[idx]=q
                            print(q,'kgs of',v,'is sucessfully modified.')
                            break
                        else:
                            print('Please enter valid Quantity..!')
                    while True:
                        c_price=float(input('Enter cost of vegetable: '))
                        if c_price>0:
                            cost[idx]=c_price
                            print(c_price,'Rs of',v,'is successfully modified')
                            break
                        else:
                            print('Please enter valid cost price..!')
                    while True:
                        s=float(input('Enter selling price of vegetable: '))
                        if s>0:
                            sell[idx]=s
                            print(s,'Rs of',v,'is successfully modified')
                            break

                        else:
                            print('please enter valid selling price..!')
                    
                else:
                    print(up,'is not available in inventory')
            elif op==4:
                print(''*8,'INVENTORY',''*8)
                for i,j,k,l in zip(vegetable,stock,cost,sell):
                    print(i,'=',j,k,l)
                print('*'*27)
                
            elif op==5:
                print()
                print(''*4,'USER DETAILS',''*4)
                for i,j,k in zip(S_No,names,mobile):
                    print(i,j,k)
                print('*'*22)
                
            elif op==6:
                print()
                print(''*12,'REPORT/REMAINING STOCK',''*12,end='')
                print()
                for i,j in zip(vegetable,stock):
                    print(i,'=',j)
                print()
                print(''*6,'ITEMIZED PROFIT',''*6)
                for a,b,c in zip(icart,iweight,iprofit):
                    print(a,'=',b,c)
                    print()
                print('*'*29)
                print()
                print('The total profit is',profit)
                
            elif op==7:
                print('Exiting from the shopkeeper')
                print()
                break
            else:
                print('Please choose valid option..!')
            print()
    elif ch==2:
        bill=0
        cart=[]
        weight=[]
        while True:
            print()
            print('1.Add to Cart')
            print('2.Remove from Cart')
            print('3.Modify in Cart')
            print('4.View Cart')
            print('5.Billing')
            print('6.Exit')
            op=int(input('Choose your option: '))
            if op==1:
                while True:
                    veg= input('Which vegetable you want to add in cart?: ').upper()
                    if veg.isalpha():
                        if veg in vegetable:
                            print(veg,'is added to the cart')
                            idx=vegetable.index(veg)
                            qty=float(input('How much quantity you want to add in cart in(kgs)?: '))
                            if qty<=stock[idx]:
                                cart.append(veg)
                                #stock[idx]=stock[idx]-qty
                                weight.append(qty)
                                print(qty,'kgs of',veg,'is added to the cart')
                                add=input('Anything else you want to buy(yes/no)?: ')
                                if add=='no':
                                    print()
                                    break
                            else:
                                print(veg,'is out of stock')
                        else:
                            print(veg,'is not available')
                    else:
                        print('Please enter valid name..!')
            elif op==2:
                while True:
                    rmv=input('Which vegetable you want to remove from cart: ').upper()
                    if rmv.isalpha():
                        if rmv in cart:
                            idx=cart.index(rmv)
                            cart.remove(rmv)
                            weight.pop(idx)
                            print(rmv,'is removed from the cart')
                            break
                        else:
                            print(rmv,'is not in cart!')
                    else:
                        print('Please enter valid vegetable name..!!')
                    
            elif op==3:
                while True:
                    mod=input('Which vegetable you want to modify in cart: ').upper()
                    if mod.isalpha():
                        break
                    else:
                        print('Please enter valid vegetable name..!')
                if mod in cart:
                    idx=cart.index(mod)
                    while True:
                        nw=input('Enter vegetable you want to replace?: ').upper()
                        if nw.isalpha():
                            break
                        else:
                            print('Please enter a valid vegetable name..!')
                    if nw in vegetable:
                        cart[idx]=nw
                        print(mod,'is successfully replaced with',nw)
                        while True:
                            wt=float(input('How much quantity you want to modify in cart: '))
                            if wt>0:
                                weight[idx]=wt
                                print(wt,'kgs of',nw,'is modified in cart')
                                break
                            else:
                                print('please enter a valid Quantity..!')
                    else:
                        print(nw,'is not available in cart!')
                else:
                    print(mod,'is not avaliable in cart!')
                        
            elif op==4:
                print()
                print(''*5,'CART',''*5)
                for i,j in zip(cart,weight):
                    print(i,'=',j,'Kgs',sep='')
                print('*'*16)
            elif op==5:
                name=input('Enter customer name: ')
                if name in names:
                    idx=names.index(name)
                    print('S.No: ',S_No[idx])
                    print('Name:',names[idx])
                    print('mobile:',mobile[idx])
                    print()
                else:
                    names.append(name)
                    while True:
                        mob=int(input('Enter customer mobile number: '))
                        if len(str(mob))==10:
                            mobile.append(mob)
                            break
                        else:
                            print('Please enter valid mobile number..!')    
                    S_No.append(len(S_No)+1)
                    print()
                    m=len(S_No)
                    print('S.No: ',m)
                    print('Name:',name)
                    print('Mobile:',mob)
                    print()
                print(''*9,'Bill',''*9)
                for i,j in zip(cart,weight):
                    if i in cart:
                        idx=vegetable.index(i)
                        bill=bill+(sell[idx]*j)
                        profit=profit+(j*(sell[idx]-cost[idx]))
                        i_profit=(j*(sell[idx]-cost[idx]))
                        c=sell[idx]
                        stock[idx]=stock[idx]-qty
                    if i in icart:
                        idx1=icart.index(i)
                        iweight[idx1]=iweight[idx1]+j
                        iprofit[idx1]=iprofit[idx1]+i_profit
                    else:
                        icart.append(i)
                        iweight.append(j)
                        iprofit.append(i_profit)
                    print(i,' ','=',' ',j,'kgs','x',c,'Rs.',' ','=',' ',i_profit,'Rs.',sep='')
                print('*'*24)
                print('Your total vegetable bill is',bill,'Rs')
                print()
                print('Thank you for Shopping with us!')
                print('Have a great day...!')
                cart=[]
                bill=0
                weight=[]

            elif op==6:
                print('Exiting from the customer')
                print(''*8,'Thankyou',''*8)
                break
            else:
                print('Please select the valid option..!')
    else:
        print('Please select the valid option..! ')