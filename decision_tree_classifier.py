'''
Assume df is a pandas dataframe object of the dataset given
'''
import numpy as np
import pandas as pd
import random

'''Calculate the entropy of the enitre dataset'''
	#input:pandas_dataframe
	#output:int/float/double/large

def get_entropy_of_dataset(df):
    entropy = 0
    df1=df[df.columns[len(df.columns)-1]]
    t_c=len(df1)
    unique=df1.unique()
    l=len(unique)
    df2=df[df.columns[len(df.columns)-1]].value_counts()
    for i in range(len(unique)):
        entropy=entropy+(-(df2[i]/t_c)*(np.log2(df2[i]/t_c)))
    return entropy



'''Return entropy of the attribute provided as parameter'''
	#input:pandas_dataframe,str   {i.e the column name ,ex: Temperature in the Play tennis dataset}
	#output:int/float/double/large
def get_entropy_of_attribute(df,attribute):
    entropy_of_attribute = 0
    df1=df[attribute]
    t_c=len(df1)
    unique=sorted(df1.unique())
    l=len(unique)
    df2=df1.value_counts().sort_index()
    for j in range(l):
        df3=df[df[attribute]==unique[j]]
        df3=df3[df3.columns[len(df3.columns)-1]]
        ec=len(df3)
        un=df3.unique()
        df4=df3.value_counts()
        entropy=0
        for i in range(len(un)):
            entropy=entropy+(-(df4[i]/ec)*(np.log2(df4[i]/ec)))
        entropy_of_attribute=entropy_of_attribute+(df2[j]/t_c)*entropy
    return abs(entropy_of_attribute)


'''Return Information Gain of the attribute provided as parameter'''
	#input:int/float/double/large,int/float/double/large
	#output:int/float/double/large
def get_information_gain(df,attribute):
	information_gain = 0
	entropy = get_entropy_of_dataset(df)
	entropy_attr = get_entropy_of_attribute(df,attribute)
	information_gain = entropy - entropy_attr
	return information_gain



''' Returns Attribute with highest info gain'''  
	#input: pandas_dataframe
	#output: ({dict},'str')     
def get_selected_attribute(df):
	information_gains={}
	selected_column=''
	#entropy of each attribute with name
	entropy_list = {k:get_entropy_of_attribute(df,k) for k in df.keys()[:-1]}
	information_gains = {k:get_information_gain(df,k) for k in entropy_list}
	selected_column = max(information_gains,key=information_gains.get)
	return (information_gains,selected_column)
	

