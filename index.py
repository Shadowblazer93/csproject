import mysql.connector
from tabulate import tabulate
import os

# VARS
w_loop=1
i_loop=1
r_snacks=[[1,'Coca Cola',60],[2,'Coffee',85],[3,'Tea',45],[4,'Potato Chips',75],[5,'Cheese sandwich',140],
          [6,"Chicken Tikka Masala", 140],[7,"Beef Burger", 200],[8,"Margherita Pizza", 240]]

def info(): print("""HEY THERE!! Dusty traveller, need a place to rest?
Why not stay here? We are the best in Meghalaya!
We have the best beds and the best views of East Khasi hills
As the name suggests we have the most beautiful view of the valley
and if you are here in monsoon you will be able to see the beautiful waterfalls from the balcony
and don't worry if you came in winter or summer. 'Cause we have starry nights to keep
you in awe and to make you have a time of your life from your comfort!""")

#FUNCS
def t_clear():
    print('\n'+'-'*100+'\nPress ENTER to continue')
    input('')
    os.system('cls' if os.name == 'nt' else 'clear')

def t_dryclear():
    os.system('cls' if os.name == 'nt' else 'clear')


# INITIAL CLEANING
t_dryclear()
info()
t_clear()


# MYSQL DB CONNECTION
con=mysql.connector.connect(
    host='localhost',
    user='root',
    password=os.environ.get('mysql_password'),
    database='csproj')
if con.is_connected(): print("✅ Connection to database established\n" + "-"*38)
cur=con.cursor()


# WELCOME => RETURNING OR CHECKING IN
while w_loop==1:
    w_choice=input('Welcome to Serenity Inn\nAre you "CHECKING IN" or "RETURNING" to your room? : ')

    if w_choice.lower() in 'returning':
        # RETURNING
        g_room=int(input("Enter your room number : "))
        g_name=input("Enter your name : ")

        cur.execute(f'select room,guest from rooms where room={g_room} and guest="{g_name}";')
        g_match=cur.fetchall()

        if len(g_match)==0:
            t_dryclear()
            print("Sorry, but there are no rooms with that name and number.")
        else:
            if(g_room==g_match[0][0] and g_name.lower()==g_match[0][1].lower()):
                g_room,g_name=g_match[0][0],g_match[0][1]
                print(f"Welcome back {g_name}! Here's the key for room {g_room}.")
                t_clear()
                w_loop=0
                break

    else:
        # CHECKING IN
        cur.execute('select count(*) from rooms where status="vacant" group by status;')
        if cur.fetchall()[0][0]==0:
            print('Sorry, all our rooms are booked!')
            g_room=0
            break

        print('Please fill out these details and we will check you in.')
        g_name=input("Name : ")
        g_days=int(input("How long will you be staying (in days) : "))
        g_checkin=input("Check-in date : ")
        g_checkout=input("Check-out date : ")

        cur.execute('select * from rooms where status="vacant";')
        g_room=cur.fetchall()[0][0]
        print(f'Your room number is {g_room}\nHave a nice stay!')

        cur.execute(f"""update rooms set status='occupied',
                    guest='{g_name}',checkin='{g_checkin}',
                    checkout='{g_checkout}',cost={g_days*2500},tab=0
                    where room={g_room}""")
        con.commit()
        t_clear()
        w_loop=0
        break

if g_room==False: os.abort()

#Input loop
while i_loop==1:
    print('Hello, what would you like to do?\n')
    print(tabulate([ [1,'Information'],[2,'Room Service'],[3,'Laundry'],
                    [4,'Leave'],[5,'Checkout'] ],headers=['ID','Service']))
    
    i_choice=input("\nEnter Service Name/ID : ")


# INFORMATION
    if i_choice.lower() in 'information' or i_choice=='1':
        cur.execute('select count(*) from rooms where status="occupied" group by status;')
        f_occupied = cur.fetchall()[0][0]
        t_dryclear()

        print(tabulate([['Rooms Occupied',f_occupied],
                        ['Rooms Vacant',9-f_occupied],
                        ['Restaurant Dishes',len(r_snacks)],
                        ['Laundry price','₹50'],
                        ['Room Cost','₹2500'] ],
                       headers=['Information','Value']))
                       
        
        print('\n\n'+tabulate([['Room',g_room],['Name',g_name]], headers=['Your Info','Value']))
        t_clear()

    # ROOM SERVICE
    if i_choice.lower() in 'room service' or i_choice=='2':
        t_dryclear()
        print(tabulate(r_snacks,headers=['No.','Snack','Price'])+'\n')

        r_input=input("What would you like to have ? : ")
        r_id=0

        for s in r_snacks:
            if len(r_input)<3:
                print('Sorry, but please be more specific.')
                break
            if r_input.lower() in s[1].lower(): r_id+=s[0]

        if r_id==0:
            print("That item is not on the menu.\nPlease try again.")
            t_clear()
        else:
            r_dish=r_snacks[r_id-1][1]
            r_price=r_snacks[r_id-1][2]
                
            r_confirm=input(f"You are purchasing {r_dish}. {r_price} will be added to your tab.\nConfirm by typing 'YES' : ")
            if (r_confirm.lower()=='yes'):
                cur.execute(f'update rooms set tab=tab+{r_price} where room={g_room};')
                con.commit()
                print("Success! Your order has been placed and will arrive at your room shortly.")
            else: print('Order cancelled!')
            t_clear()

    
    # LAUNDRY
    if i_choice.lower() in 'laundry' or i_choice=='3':
        t_dryclear()
        l_no=int(input("Our rate is ₹50 per clothing.\nHow many clothes are you giving for laundry? : "))
        cur.execute(f'update rooms set tab=tab+{l_no*50} where room={g_room}')
        con.commit()
        print(f"₹{l_no*50} has been added to your tab.\nYour cleaned clothes will arrive soon.")
        t_clear()


    # LEAVE
    if i_choice.lower() in 'leave' or i_choice=='4':
        t_dryclear()

        print('Leave your keys at the reception before you leave.\nSee you soon!')
        i_loop=0
        break


    # CHECKOUT
    if i_choice.lower() in 'checkout' or i_choice=='5':
        t_dryclear()

        cur.execute(f'select cost,tab from rooms where room={g_room}')
        c_total=cur.fetchall()[0]
        c_bill,c_tab=c_total[0],c_total[1]
        print(f'Your bill is ₹{c_bill} with an additional tab of ₹{c_tab}.')
        print(f'This brings your total amount due to ₹{c_bill+c_tab}')
        
        c_confirm=input("Type 'I CONFIRM' to automatically pay for your bill using your account : ")

        if c_confirm.lower()=='i confirm':
            print('Thank you for visiting Serenity Inn. We hope you enjoyed your stay!')
            cur.execute(f"""update rooms set status='vacant',guest=null,
                        checkin=null,checkout=null,cost=null,tab=0
                        where room={g_room};""")
            con.commit()
            i_loop=0
            break

        else: 
            print('Checkout cancelled, please try again.')
            t_clear()

con.close()