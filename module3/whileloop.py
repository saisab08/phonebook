i = 1 
while i<10:
    print(i)
    i = i+1
    print()
#########
#    *
 #   * *
 #   * * *
 #   * *  * * 
r=4
for i in range(1,5):
    for j in range(1,i+1):
        print("*",end =" ")
    print()

 #######
r = 5
for i in range(5,0,-1):
    for j in range(i):
        print("*",end = " ")
    print()

    #####
r = 6
for i in range(r,7):
    for j in range(1, i+1):
        print(j, end = " ")

    print()
