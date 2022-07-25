# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 17:57:12 2022

@author: Chuma Obasi
"""
import numpy as np
import pandas as pd
T1=[]
T2=[]
T3=[]
PR=[]
L=[]
I=[]
n=0
s=0
while n<5:
    print('\nRound '+str(n+1))
    if n==0 and s==0:
        print('''\t\t\t\tWelcome to Roll_A_Die game, enjoy!.
              In each round you will have trials to guess the right number.
              if your answer is correct at the 1st trial, you will have 3 points;
              if it\'s at the 2nd, you will have two points; if it\'s at the 3rd, you will have a point;
              if none is correct, you have 0 points in that round. Goodluck!!!
              ''')
    elif s/(n*3)>=0.5:
        print('So far you have scored '+str(s)+' points out of possible '+str(n*3)+' points, you are left with '+str(5-n)+' round(s).')
        print('\t\t\t\t\tYou are doing well!')
    else:
        print('So far you have scored '+str(s)+' points out of possible '+str(n*3)+' points, you are left with '+str(5-n)+' round(s).')
        print('\t\t\t\t\tYou are not doing well!')  
    nn=0
    L1=np.random.randint(1,6)
    I1='Round '+str(n+1)
    while nn<3:
        T=input('I pick a number from 1 to 6, guess the number: ')
        if T=='1' or T=='2'or T=='3' or T=='4' or T=='5' or T=='6':
            T=int(T)
        else:
            T=None
            print('You have picked a wrong number, pick a number from 1 to 6')
        if T==L1:
            print('Congrats! you got it after ' +str(nn+1)+' trial(s), I picked number '+str(L1))
            if nn==0:
                s+=3
                T11=T
                T21=None
                T31=None
                PR1=3
            elif nn==1:
                s+=2
                T21=int(T)
                T31=None
                PR1=2
            elif nn==2:
                s+=1
                T31=int(T)
                PR1=1
            nn=3
        else:
            if nn==0:
                T11=T
            elif nn==1:
                T21=int(T)
            elif nn==2:
                T31=int(T)
            PR1=0
            nn+=1
            print('Ouw! you missed it, try again')
    if PR1==0:   
        print('Sorry! you missed it after 3 trials, I picked number '+str(L1))
    n+=1
    L.append(L1)
    T1.append(T11)
    T2.append(T21)
    T3.append(T31)
    PR.append(PR1)
    I.append(I1)
print('\nEnd of game! you have scored '+str(s)+' points out of '+str(n*3)+' points.')
D=pd.DataFrame({'1st guess': T1,
    '2nd guess': T2,
    '3rd guess': T3,
    'True value': L,
    'Points per round': PR
    },index=I)
print(D.head(5))
try:
    C0=pd.value_counts(D['Points per round']==0)[1]
except:
    C0=0
try:
    C1=pd.value_counts(D['Points per round']==1)[1]
except:
    C1=0
try:
    C2=pd.value_counts(D['Points per round']==2)[1]
except:
    C2=0
try:
    C3=pd.value_counts(D['Points per round']==3)[1]
except:
    C3=0
prob_1=C3/5
prob_2=C2/5
prob_3=C1/5
prob_0=C0/5
m1=D['Points per round'].max()
m0=D['Points per round'].min()
print('\n\nBest round(s)')
print(D[D['Points per round']==m1])
print('\n\nWorst round(s)')
print(D[D['Points per round']==m0])
GA1=['very poor','poor','average','good','very good']
if s/(n*3)<=0.3:
    GA=GA1[0]
elif s/(n*3)>0.3 and  s/(n*3)<0.5:
    GA=GA1[1]
elif s/(n*3)>=0.5 and  s/(n*3)<=0.6:
    GA=GA1[2]
elif s/(n*3)>0.6 and  s/(n*3)<=0.75:
    GA=GA1[3]    
else:
    GA=GA1[4] 
print('\nProbability of guessing right at first trial: '+str(prob_1))
print('Probability of guessing right before or during second trial: '+str(prob_1+prob_2))
print('Probability of guessing right: '+str(prob_1+prob_2+prob_3))
print('Probability of not guessing right: '+str(prob_0))
print('\nGame Assessment: Your guessing ability is ' + GA+ '.')
D['Points per round'].plot.bar(title='Bar chart of performance',ylabel='Points per round')     
D.plot.hist(alpha=1, title='Histogram of performance.')        
        



