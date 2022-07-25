# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 13:21:27 2021
@author: Innocent Chukwuma Obasi
Purpose: A smart variable coefficient differential equation calculator that evaluates the general 
        and particular solutions to the differential equation below:
                        y" + Axy' - nAy = 0
        where n represents an integer while A represents any number(including negative numbers).
        The methodology used for this calculator was developed by Innocent Chukwuma Obasi in his 
        publication 'New solutions to variable coefficients differential equation (2021, ongoing review)'. This
        method proves to be better than other contemporary methods.
        This calculator is able to detect invalid inputs for correction, and also ensure
        a readable and understandable output.    
"""
import math
import cmath
import numpy as np
from scipy.special import erf
import matplotlib.pyplot as plt
print('\nTo solve the differential equation: \n\t\t\t\t\t\ty" + Axy\' - nAy = 0 \nwhere n represents an integer while A represents any number(including negative numbers)')
"""
Input values of A and n for the solution of the equation. Verify the inputs if it forms the 
intended equation.
"""
intended='no'
while intended=='no':
    A1=''
    while A1.isdigit()==False:
        try:
            A=float(input('Enter the value of A : '))
            if A==0:
                print('\t\t\t\t\tError! input must be either a number (except zero) or a decimal')
                A1=''
            else:
                A=A
                break
        except:
            print('\t\t\t\t\tError! input must be either a number (except zero) or a decimal')
            A1=''
    n1=''
    while n1.isnumeric()==False:
        try:
            nn=int(input('Enter the value of n : '))
            if nn<0:
                print('\t\t\t\t\tError! input must be an integer other than zero (e.g. 1,2,3...)')
                n1=''
            elif nn==0:
                print('\t\t\t\t\tError! input must be an integer other than zero (e.g. 1,2,3...)')
                n1=''
            else:
                n=nn
                break
        except:
            print('\t\t\t\t\tError! input must be an integer other than zero (e.g. 1,2,3...)')
            n1=''
# to display the inputed equation for verification
    A11=str(A)
    n11=str(n*A)
    n2=n11[0:len(n11)-2]
    if A11[-1]=='0':
        A2=str(int(float(A11)))
    else:
        A2=A11 
    if n11[-1]=='0':
        n2=str(int(float(n11)))
    else:
        n2=n11
    if A2=='1':
        A2=''
    elif A2=='-1':
        A2='-'
    if n2=='1': 
        n2=''
    elif n2=='-1':
        n2='-'
    try:
        if A2[0]=='-':
            sign1='+'
            sign2='-'
            A2=A2[1:]
            n2=n2[1:]
        else:
            sign1='-'
            sign2='+'
            A2=A2
            n2=n2
    except:
        A2=''
        sign1='-'
        sign2='+'
    print('\nInputed equation:\n\t\t\t\ty" '+sign2+' '+A2+'xy\' '+sign1+' '+n2+'y = 0')
    if n%2==1:
        N=(n-1)/2
    else:
        N=n/2
    N=int(N)
    if n%2==1:
        N1=(n-1)/2
    else:
        N1=(n-2)/2
    N1=int(N1)
    s=''
    while s=='':
        Q1=input('Is the above equation the intended equation you had in mind to be solved? (yes/no): ')
        if Q1.lower()=='yes':
            intended='yes'
            s=0
            def the1(i):
                try:
                    t=(math.factorial(n))/((2**i)*math.factorial(i)*math.factorial(n-2*i)*(A)**i)
                except:
                    print('\nThe value of n is too large')
                tt=n-2*i
                m=str(t)
                if m=='1.0'and n==2 and i==0:
                    m=''
                elif m=='1.0'and n==2 and i==1:
                    m='1'
                elif m=='-1.0'and n==2 and i==1:
                    m='-1'
                elif m=='1.0'and n!=2:
                    m='' 
                if m!='':
                    if str(format(float(m),'.4f'))[-4]=='0'and str(format(float(m),'.4f'))[-3]=='0' and str(format(float(m),'.4f'))[-1]=='0' and str(format(float(m),'.4f'))[-2]=='0':
                        m=str(int(float(m)))
                    else:
                        m=str(format(float(m),'.4f'))
                return m+'x^'+str(tt)
            def the2(i):
                t1=0
                for j in range(i):
                    t1+=(2**j*math.factorial(n-1-j))/math.factorial(i-j)
                t=(math.factorial(n-1-i)/math.factorial(n-1-2*i)+t1/(2**i*math.factorial(n-1-2*i)))*(1/A)**(i+1)
                tt=n-1-2*i
                m=str(t)
                if m=='1.0':
                    m=''
                elif m=='-1.0':
                    m='-'
                if m!='' and m!='-':
                    if str(format(float(m),'.4f'))[-4]=='0'and str(format(float(m),'.4f'))[-3]=='0' and str(format(float(m),'.4f'))[-1]=='0' and str(format(float(m),'.4f'))[-2]=='0':
                        m=str(int(float(m)))
                    else:
                        m=str(format(float(m),'.4f'))
                return m+'x^'+str(tt)
            w=''
            v=''
            if N==0:
                w='   '+the1(0)
            else:
                for i in range(N+1):
                    if the1(i)[0]=='-':
                        w+=' - '+the1(i)[1:]
                    else:
                        w+=' + '+the1(i)
            if n%2==0:
                w1='['+w[3:len(w)-3]+']'
            else:
                w1='['+w[3:len(w)-2]+']'
            if w1[-3]=='+':
                w1=w1[:-2]+' 1'
            elif w1[-3]=='-':
                w1=w1[:-2]+' 1'
            if N==0:
                v='   '+the2(0)
            else:
                for i in range(N1+1):
                    if the2(i)[0]=='-':
                        v+=' - '+the2(i)[1:]
                    else:
                        v+=' + '+the2(i)
            if n%2==0:
                if v[1]=='-':
                    v='-'+v[3:len(v)-2]
                else:
                    v=v[3:len(v)-2]
                v1='['+v+']'
            else:
                if v[1]=='-':
                    v='-'+v[3:len(v)-3]
                else:
                    v=v[3:len(v)-3]
                v1='['+v+']'
            if v1[-3]=='+':
                v1=v1[:-2]+' 1]'
            elif v1[-3]=='-':
                v1=v1[:-2]+' 1]'
            u=(math.pi/(2*A))**0.5
            u=str(format(u,'.4f'))
            u1=(0.5*A)**0.5
            u1=str(format(u1,'.4f'))
            q=str(-0.5*A)
            if v1=='[]':
                GS='\nThe general solution:\ny = C1'+w1+' + C2('+u+')'+w1+'erf('+u1+'x)+ '+'C2'+'exp('+q+'x^2)'
            elif v1=='[-]':
                GS='\nThe general solution:\ny = C1'+w1+' + C2('+u+')'+w1+'erf('+u1+'x)+ '+'-C2'+'exp('+q+'x^2)'
            else:
                GS='\nThe general solution:\ny = C1'+w1+' + C2('+u+')'+w1+'erf('+u1+'x) + '+'C2'+v1+'exp('+q+'x^2)'
            print(GS)
        elif Q1.lower()=='no':
            s=0
            print('\nThen you will have to input again.')
            intended='no'
        else:
            print('\t\t\t\t\tError! you are only allowed to select either yes or no.')
            s=''
""" To determine the particular solution. Accepting inputs of either yes or
no to determine whether the user wants the particular solution of the differential
equation
"""
PS=''
while PS=='':
    Q2=input('Do you wish to obtain the particular solution for a given set of boundary conditions? (yes/no): ')
    if Q2.lower()=='yes':
        x11=''
        while x11.isdigit()==False:
            try:
                x1=float(input('Enter the initial boundary condition for x : '))
                break
            except:
                print('\t\t\t\t\tError! input must be either a number or a decimal')
                x11=''
        y11=''
        while y11.isdigit()==False:
            try:
                y1=float(input('Enter the corresponding value of y at x = '+str(x1)+' : '))
                break
            except:
                print('\t\t\t\t\tError! input must be either a number or a decimal')
                y11=''
        x21=''
        while x21.isdigit()==False:
            try:
                x2=float(input('Enter the final boundary condition for x : '))
                break
            except:
                print('\t\t\t\t\tError! input must be either a number or a decimal')
                x21=''
        y21=''
        while y21.isdigit()==False:
            try:
                y2=float(input('Enter the corresponding value of y\' at x = '+str(x2)+' : '))
                break
            except:
                print('\t\t\t\t\tError! input must be either a number or a decimal')
                y21=''
        def thet1(x):
            theta1=0   
            for i in range(N+1):
                theta1+=(x**(n-2*i))*((math.factorial(n))/((2**i)*math.factorial(i)*math.factorial(n-2*i)*(A)**i))
            return theta1
        def thet2(x):
            t=0
            t1=0
            for i in range(N1+1):
                for j in range(i):
                    t1+=(2**j*math.factorial(n-1-j))/math.factorial(i-j)
                t+=((x**(n-1-2*i))/A)*math.exp((-A/2)*x**2)*(math.factorial(n-1-i)/math.factorial(n-1-2*i)+t1/(2**i*math.factorial(n-1-2*i)))*(1/A)**i
            try:
                h=math.sqrt(math.pi/(2*A))*thet1(x)*math.erf(math.sqrt(A/2)*x)+t
            except:
                h=cmath.sqrt(math.pi/(2*A))*thet1(x)*erf(cmath.sqrt(A/2)*x)+t
            return h
        def thet_1(x):
            theta_1=0   
            for i in range(N+1):
                try:
                    t=(n-2*i)*(x**(n-2*i-1))*((math.factorial(n))/((2**i)*math.factorial(i)*math.factorial(n-2*i)*(A)**i))
                    theta_1=theta_1+t
                except:
                    t=0
                    theta_1=theta_1+t
            return theta_1
        def thet_2(x):
            t=0
            t1=0
            for i in range(N1+1):
                for j in range(i):
                    t1+=(2**j*math.factorial(n-1-j))/math.factorial(i-j)
                try:
                    t2=(((n-1-2*i)/A)-x**2)*(x**(n-1-2*i))*math.exp((-A/2)*x**2)*(math.factorial(n-1-i)/math.factorial(n-1-2*i)+t1/(2**i*math.factorial(n-1-2*i)))*(1/A)**i
                    t=t+t2
                except:
                    t2=0
                    t=t+t2
            try:
                h=math.sqrt(math.pi/(2*A))*thet_1(x)*math.erf(math.sqrt(A/2)*x)+t+thet1(x)*math.exp((-A/2)*x**2)
            except:
                h=cmath.sqrt(math.pi/(2*A))*thet_1(x)*erf(cmath.sqrt(A/2)*x)+t+thet1(x)*math.exp((-A/2)*x**2)
            return h
        T1=thet1(x1)
        T2=thet2(x1)
        T3=thet_1(x2)
        T4=thet_2(x2)
        P=np.array([[T1,T2],[T3,T4]])
        Q=np.array([y1,y2])
        try:
            C=np.linalg.solve(P,Q)    
            C1=str(format(C[0],'.4f'))
            C2=str(format(C[1],'.4f'))
            if A11[0]=='-':
                C1='('+C1+')'
                C2='('+C2+')'
            if C2[0]=='-':
                C2='('+C2+')'
            if v1=='[]':
                PS='\nThe particular solution:\ny = '+C1+w1 +' + '+ C2+'('+u+')'+w1+'erf('+u1+'x) + '+C2+'exp('+q+'x^2)'
            elif v1=='[-]':
                PS='\nThe particular solution:\ny = '+C1+w1+' + '+C2+'('+u+')'+w1+'erf('+u1+'x) + '+'-'+C2+'exp('+q+'x^2)'
            else:
                PS='\nThe particular solution:\ny = '+C1+w1 +' + '+ C2+'('+u+')'+w1+'erf('+u1+'x) + '+C2+v1+'exp('+q+'x^2)'
            print(PS)
            x=np.linspace(x1,10+x1*10,1000)
            def thet3(g):
                F=np.zeros(1000)
                for i in range (1000):
                    F[i]=thet2(g[i])
                return F    
            try:
                y=float(format(C[0],'.4f'))*thet1(x)+float(format(C[1],'.4f'))*thet3(x)
                plt.plot(x,y)
                plt.xlabel('x - axis')
                plt.ylabel('y - axis')
                plt.title('Graph of y against x\n')
                plt.show()
                print('\nSuccessful operation! Graph is available in the plot section')
            except:
                print('\n\t\t\t\t\tNo graphical analysis available, solutions deals with complex numbers.')
        except:
            print('\n\t\t\t\t\tParticular solution could not be obtained.')
    elif Q2.lower()=='no':
        PS=GS
    else:
        print('\t\t\t\t\tError! you are only allowed to select either yes or no.')
        PS=''
        
    