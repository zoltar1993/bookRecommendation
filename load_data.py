import pandas as pd
import sys
from sklearn.model_selection import  train_test_split

lst=[]
#book_rating='BX_Book_Ratings.csv'


for line in open(book_rating,encoding=''):
    print(type(line))
