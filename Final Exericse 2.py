# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 09:24:46 2019

@author: harry
"""
#Relevant import statements
import numpy as np
import math

import matplotlib.pyplot as plt



#List of all the constants that will be used in the program
m = 112
C_d = 1
A = 0.7
g = 9.81
t_0 = 0
h= 7640
p_0 = 1.2
k = (C_d*A*p_0)/2

   

#Start of the menu system
MyInput = '0'
while MyInput != 'q':
    
    #User is asked for the starting height and the initial speed
    Input_y_0 = input('Enter the height of the object in metres')
    y_0 = float(Input_y_0)
    
    Input_v_0 = input('Enter your Initial speed in metres per second')
    v_0 = float(Input_v_0)
    
    #Allows the user to choose which method they want to use
    MyInput = input('''Enter a method to simulate Free fall, "a" for the Analytical Method , 
                    "e" for Eulers Method, "c" if you want to compare the data or "q" to quit ''')
    print('You entered the choice: ',MyInput)
    if MyInput == 'a':
        print('Analytical Method')
        
        #For the code to work, the detail of the graph is chose by the user 
        Input_r = input('Enter the number of points for the graph to go over')
        r = int(Input_r)
        
        #This creates the range of t values that the y and v functions will use
        tmin = 0
        #This is simply the y equation set to zero and rearranged to find 
        #the value of t at 0
        tmax = np.arccosh(math.exp((k*y_0)/m))*(m/(k*g))**0.5
        t_data = np.linspace(tmin,tmax,r)
    
        #These create an array of values for each t value in t_data
        y_data = [y_0 - m/k * math.log(np.cosh(t/(m/(g*k))**0.5)) for t in t_data]
        

        v_data = [-((m*g)/k)**0.5 * np.tanh(t/(m/(g*k))**0.5) for t in t_data]
        
        #Simply asks he user for which data they want to graph
        Data_type = input('''Enter "y" for the vertical distance against time data or "v"
                    for the vertical speed against time data''')
        if Data_type == 'y':
               plt.plot(t_data,y_data)
               plt.xlabel('Time in (s)')
               plt.ylabel('Distance in (m)')
               plt.show()
               
     
            
        elif Data_type == 'v':
               plt.plot(t_data,v_data)
               plt.xlabel('Time in (s)')
               plt.ylabel('Velocity in ($ms^-1$)')
               plt.show()
        
            
        elif Data_type != 'y' or 'v' or 'b':
               print("Please select a valid option")
            
        

    elif MyInput == 'e':
        print('Eulers method')
        Input_delta_t = input('Enter the delta t value')
        delta_t = float(Input_delta_t)
        #Constants and inital values for the list
        t = 0
        y_data = [y_0]
        v_data = [v_0]
        t_data = [t] 
        #This while loop changes the values inputed to the next value according to  
        #Eulers method, then this value is added to the t,y,v data lists
        while y_0 > 0:
            
            k = C_d*A*math.exp(-y_0/h)/2
            
            
            v_0 = v_0 - delta_t * (g + (k/m) * (np.absolute(v_0)*v_0))
            v_data.append(v_0)
        
            y_0 = y_0 + delta_t * v_0
            y_data.append(y_0)
        
            t = t + delta_t
            t_data.append(t)
        #Same as for the analytical method for printing graphs
        Data_type = input('''Enter "y" for the vertical distance against time data or "v"
                    for the vertical speed against time data''')
        if Data_type == 'y':
            plt.plot(t_data,y_data)
            
            plt.xlabel('Time in (s)')
            plt.ylabel('Distance in (m)')
            plt.show()
    
        
            
        elif Data_type == 'v':
            plt.plot(t_data,v_data)
            plt.xlabel('Time in (s)')
            plt.ylabel('Velocity in ($ms^-1$)')
            plt.show()
            
            
        elif Data_type != 'y' or 'v':
            print("Please select a valid option")
            

        
            
            
            
                
            
            
        
            
    elif MyInput == 'c':
        y = y_0
        v = v_0
        t = 0
        p_0 = 1.2
        k = (C_d*A*p_0)/2
        #Combines both of the methods above but the variables for the Eulers method have been changed
        #get the correct values
        Input_r = input('Enter the number of points for the graph to go over')
        Input_delta_t = input('Enter the delta t value')
        delta_t = float(Input_delta_t)
        r = int(Input_r)
        tmin = 0
        #Analytical Part
        tmax = np.arccosh(math.exp((k*y_0)/m))*(m/(k*g))**0.5
        t_data = np.linspace(tmin,tmax,r)

        y_data = [y_0 - m/k * math.log(np.cosh(t/(m/(g*k))**0.5)) for t in t_data]
        

        v_data = [-((m*g)/k)**0.5 * np.tanh(t/(m/(g*k))**0.5) for t in t_data]
        #Eulers Method part    
        yE_data = [y]
        vE_data = [v]
        tE_data = [t]
        while y > 0:
            v = v - delta_t * (g + (k/m) * (np.absolute(v)*v))
            vE_data.append(v)
    
            y = y + delta_t * v
            yE_data.append(y)
        
            t = t + delta_t
            tE_data.append(t)
        
        plt.plot(t_data,y_data,color='blue')
        plt.plot(tE_data,yE_data,color='red',linestyle='--')
        plt.xlabel('Time in (s)')
        plt.ylabel('Distance in (m)')
        plt.show()

        
        plt.plot(t_data,v_data,color='blue')
        plt.plot(tE_data,vE_data,color='red',linestyle='--')
        plt.xlabel('Time in (s)')
        plt.ylabel('Velocity in ($ms^-1$)')
        plt.show()



            
            
            
            
    elif MyInput != 'q':
        print('This is not a valid choice')

print('You have chosen to finish - goodbye.')
