#python program that deals with real diode analysis
#iterative model
#linear model
#constant voltage model

#iterative model
#parameters used : EMF,voltageDrop-diode,currentOne-diode,currentTwo-diode
#the model is a more accurate way of determing the voltage drop across a real diode
#It can also be used to determine the current flowing

#formula V2=v1+2.3*n*Vt*log(I2/I1);

"""
The matplot library was used to analyse the ouputs in the console
graphically. It was observed that the area which is more dense 
is where the voltage across the diode remains nearly the same .

The iteration stops if the parameters provided detects a negative
current across the diode. This implies that the diode is open or in a 
reverse-bias mode.
"""
import math
import matplotlib.pyplot as plt 


current = [] #keeps the current value of each iteration
voltage = [] #keeps the voltage across the diode for each iteration

#displays information about the model to the screen
def information():
    print("Diode Analysis using Iterative Model\n")
    print("All parameters are in their standard unit")
    print(".....................................\n")
    print("Voltage=V, current =A, Resistance= ohms")
    print("------------------------------------\n")
    print("NOTE: More iteration count implies high accuracy\n")

def request_for_parameters():
    emf = float(input("Enter the emf of the closed circuit>>"))
    diode_voltagedrop = float(input("Enter the initial diode voltage>>"))
    diode_current =float(input("Enter initial diode current>>"))
    ex_resistance = float(input("Enter value of total external resistance>>"))
    n = float(input("Enter the n value of the material the diode was made of>>"))
    thermal_voltage =float(input("Enter the value of the thermal voltage at room temperature>>"))
    #iteration_count = int(input("How many times do you want to iterate (should iteration>1)>>"))
    iterative_model(emf,diode_voltagedrop,diode_current,ex_resistance,n,thermal_voltage)

def iterative_model(emf,diode_voltagedrop,diode_current,ex_resistance
                    ,n,thermal_voltage):
    
    const_term = 2.3*n*thermal_voltage

    iteration_count = 0
    prev_iteration_voltage = diode_voltagedrop
    next_iteration_voltage = 0

    #prev_next_voltage_difference = abs(prev_iteration_voltage - next_iteration_voltage)
    while(True):
        temp_voltage = diode_voltagedrop
        if round(prev_iteration_voltage,4) == round(next_iteration_voltage,4):
            break
        else:
           # voltage_drop_record = 0
        # get the current flowing through the circuit 
            new_current = (emf-diode_voltagedrop)/ex_resistance
            print("iteration {0}=> current flowing through diode {1}A\n".format(iteration_count+1,new_current))
            current.append(new_current)

        #calculates the new voltage drop across the diode
            diode_voltagedrop = diode_voltagedrop + const_term * math.log10(new_current/diode_current)

            print("iteration {0} => voltage drop across diode : {1}V\n".format(iteration_count+1,diode_voltagedrop))
            voltage.append(diode_voltagedrop)
            print("------------------------------------------------------------------\n\n")
            diode_current=new_current
            next_iteration_voltage = diode_voltagedrop
            prev_iteration_voltage = temp_voltage

        iteration_count+=1
    print("Program finished\n")


information() 


try:
    request_for_parameters()
    plt.scatter(current,voltage)
    plt.xlabel("Current")
    plt.ylabel("voltage")
    plt.show()
except ValueError:
    print("The iteration could not continue because log of a negative number is invalid\n")
    print("You may have entered a string or a letter as part of the parameters!")
except ZeroDivisionError:
    print("The total external resistance cannot be zero!")



    
#iterative_model(5,0.7,0.001,5000,2,2,-1)