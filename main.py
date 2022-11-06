import getpass
users = {"Zeeya":"1234","Nuru":"abcd"}
username = str(input('Enter Your Username: '))
password = str(getpass.getpass('Enter Your Password: '))
global user
for i in users.keys():
    if username == i:
        while password != users.get(i):
            password = str(getpass.getpass('Enter Your Password Again: '))
        break
    else:
        print('Invalid Input...')
def print_options():
    print('___________________')
    print('1 - Change Username')
    print('2 - Change Password')
    print('3 - Quit System')


def change_username(user):
    new_username = str(input('Choose New Username: '))
    
    if user in users:
        users[user] = users[new_username]
        del users[user]
        print(f'Done!...Your new username is {new_username}')
    else:
        print('Sorry, Username not valid')
        
        
def change_password(user):
    old_password = str(getpass.getpass('Enter Old Password: '))
    while old_password != users.get(user):
        print('Wrong Password...Try Again!')
        old_password = str(getpass.getpass('Enter Old Password Again: '))
    new_password = str(getpass.getpass('Enter New Password: '))
    users.update(user=new_password)
    print('Password Changed successfully!')


print(f'Logged in...Welcome {username}!')
user = username
option = 0
while True:
    print_options()
    try:
        option = int(input())
    except:
        print('Input not valid...')
            
    if (option == 1):
        change_username(user)
    elif (option == 2):
        change_password(user)
    elif (option == 3):
        break
    else:
        print('Input not valid...')

