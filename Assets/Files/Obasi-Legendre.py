# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 21:59:29 2022

@author: Innocent Chukwuma Obasi
Purpose: A smart variable coefficient differential equation calculator that evaluates the general 
        solution to the differential equation below:
                        (1-x^2)y" - 2xy' + n(n+1)y = 0
        where n represents an non-negative integer.
        The methodology used for this calculator was developed by Innocent Chukwuma Obasi in his 
        research work 'The Best Ever Solution to Legendre Differential Equation (2022, ongoing review)'. This
        method proves to be far better than other contemporary methods including the usage of Legendre
        polynomials. This calculator is able to detect invalid inputs for correction, and also ensure
        a readable and understandable output.    
"""
import math
from fractions import Fraction
print("""\nTo solve the differential equation: 
      \n\t\t\t\t\t\t(1-x^2)y" - 2xy\' + n(n+1)y = 0 \nwhere,
      n must be a non-negative integer""")
"""
Input the values of n for the solution of the equation. Verify the inputs if it forms the 
intended equation.
"""
intended='no'
while intended=='no':
    n1=''
    while n1.isnumeric()==False:
        try:
            nn=int(input('Enter the value of n : '))
            if nn<0:
                print('\t\t\t\t\tError! input must be a non-negative integer (e.g. 0,1,2,3...)')
                n1=''
            else:
                n=nn
                break
        except:
            print('\t\t\t\t\tError! input must be a non-negative integer (e.g. 0,1,2,3...)')
            n1=''
# to display the inputed equation for verification
    n2=str(n*(n+1))
    print('\nInputed equation:\n\t\t\t\t(1-x^2)y" - 2xy\' + '+n2+'y = 0')
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
    st=''
    while st=='':
        Q1=input('Is the above equation the intended equation you had in mind to be solved? (yes/no): ')
        if Q1.lower()=='yes':
            intended='yes'
            st=0
            def L1(n):
                s=''
                if n==0:
                    s='1'
                elif n==1:
                    s='x'
                else:
                    for r in range(N+1):
                        s1=((-1)**r*math.factorial(2*n-1-2*r))/(math.factorial(n-1-r)*math.factorial(n-2*r)*math.factorial(r))
                        tt=n-2*r
                        if tt==0:
                            s1='('+str(Fraction(s1))+')'
                        elif tt==1:
                            s1='('+str(Fraction(s1))+')x'
                        else:
                            s1='('+str(Fraction(s1))+')x^'+str(tt)
                        s+=' + '+s1
                    s=s[3:]
                return s
            def L2(n):
                s='('+L1(n)+').atanh(x)'
                if n==0:
                    s=s
                else:
                    s0=Fraction(-math.factorial(2*n-1)/(math.factorial(n)*math.factorial(n-1)))
                    tt=n-1
                    if tt==0:
                        s1='('+str(s0)+')'
                    elif tt==1:
                        s1='('+str(s0)+')x'
                    else:
                        s1='('+str(s0)+')x^'+str(tt)
                    s=s+' + '+s1
                    for r in range(N1):
                        tt=n-3-2*r
                        A=Fraction(((-1)**r*math.factorial(2*n-3-2*r)))/Fraction((math.factorial(n-1-r)*math.factorial(n-3-2*r)*math.factorial(r+1)))
                        s00=Fraction(((n-1-2*r)*(n-2-2*r)*s0))/Fraction((2*(n-1-r)))
                        s0=-(Fraction(1)/Fraction(2*r+3))*(s00-A)
                        if tt==0:
                            s1='('+str(s0)+')'
                        elif tt==1:
                            s1='('+str(s0)+')x'
                        else:
                            s1='('+str(s0)+')x^'+str(tt)
                        s+=' + '+s1
                return s
            GS='\nThe general solution:\ny = C1['+L1(n)+'] + C2['+L2(n)+']'
            print('L1_'+str(n)+'(x) = '+L1(n))
            print('\nL2_'+str(n)+'(x) = '+L2(n))
            print(GS)
        elif Q1.lower()=='no':
            st=0
            print('\nThen you will have to input again.')
            intended='no'
        else:
            print('\t\t\t\t\tError! you are only allowed to select either yes or no.')
            st=''
