import pandas as pd
import sys
from sklearn.model_selection import  train_test_split

lst=[]
book_rating='BX_Book_Ratings.csv'

out_train = open('train.csv', 'w')
out_test = open('test.csv', 'w')

for line in open(book_rating):
    items = line.strip().split()
    lst.append(items)

train_set,test_set=train_test_split(lst,test_size=0.25,random_state=33)
print(test_set)


for i in train_set:
    out_train.write(' '.join(i) + '\n')
for i in test_set:
    out_test.write(' '.join(i) + '\n')