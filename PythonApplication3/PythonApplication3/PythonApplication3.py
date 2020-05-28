print('-------------------------HELLO KKU-------------------------------')
from datetime import date
loop = 1
fdata = open("C:\\aof.py\\data_friends.txt","w")
while loop <= 5:
    Name,Nickname,Birth,Province,School = input("Name : Nickname : Date of Birth : Province : School =====> ").split(':')
    fdata.write('%s,%s,%s,%s,%s\n'%(Name,Nickname,Birth,Province,School))
    loop += 1
fdata.close()

def Show():
    fdata = open("C:\\aof.py\\data_friends.txt","r")
    print("---------------------------------------------------------------------------------------------------------------------")
    print("[No.]\t[Name]\t\t[Nickname]\t   [Date of Birth]\t[Age]\t    \t[Province]\t \t[School]\t")
    print("---------------------------------------------------------------------------------------------------------------------")
    count = 1
    while True:
        information = fdata.readline().split(',')
        if information[0] == "":
            break
        Birth = information[2]
        year = Birth[-4:len(Birth)]
        daynow = date.today().strftime('%Y')
        age = int(daynow)-int(year)
        print('{0:<5}'.format(str(count)),end="")
        print('{0[0]:<25}{0[1]:<15}{0[2]:<20}'.format(information),end="")
        print('{0:<15}'.format(str(age)),end="")
        print('{0[3]:<23}{0[4]:<40}'.format(information),end="")
        count += 1
        print()
    print("---------------------------------------------------------------------------------------------------------------------")
    fdata.close()
Show()
