#--------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------IMPORTANT!!!------------------------------IMPORTANT!!!------------------------------IMPORTANT!!!----------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------- CREATE A FILE definition1.csv BEFORE RUNNING AND RENAME IT definition.csv AFTER AND DELETE THE ORIGINAL!!! ----------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------IMPORTANT!!!------------------------------IMPORTANT!!!------------------------------IMPORTANT!!!----------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------

#province id int;red int;blue int;green int;province type lake land sea string; coastal boolean; terrain type string; continent int

#set true the ones you want to be checked
requirements = [True,False,False,False,False,False,False,False]

#set or add the values to be required to change a province
checks = [[788,803,805,2247,2248,2291,2842,2843,2844,5608,5615,5616,5617,5706,6984,7748,8598,8600,8601,8818,8836,9595,9598,9622,9652,9655,9705,9707,9714,9715,9719,9725,11301,11302,11303,11305,11336,11344,11347,11351,11353,11414,11423,11427,11437,11439,11440,11453,11473,11479,11487,11499,11512,11518,11525,11528,11556,11601,11607,11609,11615,11616,11645,11654,11655,11666,11667,11713,11743,11751,11752,11755,11761,11762,11763,11765,11766,11768,11770,11778,11782,11784,11785,11789,11796,11799,11800,11801,11805,11807,11812,11816,11840,11952,11955,11957,11959,11960,11964,11967,11968,11969,11971,11976,11985,11986,11988,11995,12039,12070,12341,12342,12343,12344],0,0,0,'',False,'',0]

#set true the ones you want to be changed
changes_done = [False,False,False,False,False,False,True,False]

#set values to what you want edited provinces to have changed
change_to = [0,0,0,0,'',False,'urban',0]

import csv

province_list=[]

with open ('map/definition.csv','r') as csvfile:
    temp_file=csv.reader(csvfile)
    for a in temp_file:
        temp_split_holder = a[0].split(";")
        temp_split_holder[0]=int(temp_split_holder[0])
        temp_split_holder[1]=int(temp_split_holder[1])
        temp_split_holder[2]=int(temp_split_holder[2])
        temp_split_holder[3]=int(temp_split_holder[3])
        temp_split_holder[7]=int(temp_split_holder[7])
        if(temp_split_holder[5]=='false'):
            temp_split_holder[5]=False
        else:
            temp_split_holder[5]=True
        temp_split_holder[4]=temp_split_holder[4].strip("'")
        temp_split_holder[6]=temp_split_holder[6].strip("'")
        province_list.append(temp_split_holder)
# print(province_list)


amt_req = 0
for i in range(len(requirements)):
    if requirements[i]==True:
        amt_req+=1
for a in range(len(province_list)):
    prov_req_ful=0
    for b in range(len(requirements)):
        if (requirements[b]==True) and ((province_list[a][b]==checks[b]) or (province_list[a][b] in checks[b])):
            prov_req_ful+=1
    if prov_req_ful==amt_req:
        for b in range(len(changes_done)):
            if (changes_done[b]==True):
                province_list[a][b]=change_to[b]

with open('map/definition1.csv','w',newline='') as csvfile:
    writer=csv.writer(csvfile,delimiter=';')
    writer.writerows(province_list)
    # print(writer)

with open ('map/definition1.csv','r') as csvfile:
    temp_file=csv.reader(csvfile)
    for a in temp_file:
        print(a)