import cv2
import csv
import numpy as np
import face_recognition as fr
import datetime
import pandas as pd
def store(i,name,em):
            ff1 = fr.face_locations(i)
            ke1 = fr.face_encodings(i,ff1)[0]
            ke1 = list(ke1)
            s = '' 
            for i in range(0,len(ke1)):
                ke1[i] = str(ke1[i])
                s = s+ke1[i]+','
            values = [name,s]
            with open("face_data.csv",'a') as csv_file:
                csv_append = csv.writer(csv_file)
                csv_append.writerow(values)
            row = [name,em]
            with open('attendence.csv', 'a') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(row)
            print('Done')
##date = datetime.datetime.now()
##s = str(date)
##date = s[0:10]
##d1 = date[8:10]
##d2 = date[5:7]
##d3 = date[2:4]
##final = d1+'/'+d2+'/'+d3
date = datetime.date.today()
date = str(date)
print(date)
d = pd.read_csv('attendence.csv')
if date not in d.head(0):
    d[date] = 'A'
    d.to_csv('attendence.csv' , index=0)
while 1:
    inp = input('Enter c to capture image and q to quit ')
    if inp=='c':
        v = cv2.VideoCapture(0)
        print('Capturing Image....')
        count = 0
        with open("face_data.csv",'r') as new_file:
            csv_reader= csv.reader(new_file)
            for line in csv_reader:
                if line[0]:
                    count = count+1
                else:
                    break
        r,img = v.read()
        flag = 0
        fl = fr.face_locations(img)
        print("Loactions")
        print(fl)
        if len(fl) >0:
            e = fr.face_encodings(img,fl)[0]
            print("Encodings")
            print(e)
            for k in range(0,count+1):
                with open("face_data.csv",'r') as new_file:
                    csv_reader= csv.reader(new_file)
                    for line in csv_reader:
                        lst = line[1].split(',')
                        for i in range(0,len(lst)-1):
                            lst[i] = float(lst[i])
                        lst.pop()
                        lst1 = np.array(lst)
                        f = fr.compare_faces([lst1],e)
                        if True in f:
                            name = line[0]
                            d = pd.read_csv('attendence.csv')
                            names = d['Name']
                            names = list(names)
                            if name in names:
                                index = names.index(name)
                            d[date][index] = 'P'
                            d.to_csv('attendence.csv',index=0)
                            print(name + ' marked as Present')
                            flag=1
                            break
                    if flag==1:
                        break
                    else:
                        print('New Student')
                        name = input('Enter Name ')
                        e1 = 1
                        while e1:
                            email = input("Enter email ")
                            s1 = email.split('@')
                            if len(s1)==2:
                                s2 = s1[1].split('.')
                                if len(s2)==2:
                                    e1 = 0
                                    break
                                else:
                                    print("Invalid Email ")
                            else:
                                print("Invalid Email")
                        store(img,name,em)
                        break
        else:
            print("No face detected")
    else:
        v.release()
        cv2.destroyAllWindows()
        break
