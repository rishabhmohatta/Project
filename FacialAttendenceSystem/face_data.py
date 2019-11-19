import cv2
import csv
import pandas as pd
import face_recognition as fr
def store(i,name):
    ff1 = fr.face_locations(i)
    print(ff1)
    ke1 = fr.face_encodings(i,ff1)[0]
    print(ke1)
    ke1 = list(ke1)
    s = '' 
    for i in range(0,len(ke1)):
        ke1[i] = str(ke1[i])
        s = s+ke1[i]+','
    values = [name,s]
    with open("test.csv",'a') as csv_file:
        csv_append = csv.writer(csv_file)
        csv_append.writerow(values)
    print('Done')
##i = fr.load_image_file('/Users/apple/Desktop/Python+ML/adit.jpg')
##store(i,'Adit')
##i = fr.load_image_file('/Users/apple/Desktop/Python+ML/kaushal.jpg')
##store(i,'Kaushal')
##with open("face_data.csv",'r') as new_file:
##    csv_reader= csv.reader(new_file)
##    for line in csv_reader:
##        lst = line[1].split(',')
##        print(lst)
####        for i in range(0,len(lst)-1):
##            lst[i] = float(lst[i])
##        print(lst)
##        print(lst)
##        print(len(lst))
##        break
####        
##
v = cv2.VideoCapture(0)
r,img = v.read()
store(img,'img')
v.release()
cv2.destroyAllWindows()
