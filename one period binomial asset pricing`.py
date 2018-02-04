#one period binomial asset pricing

########### By Ignacio Anguita ############

#S0=stock initial price
#SH=Stock high price
#ST=Stock tails price
#K=strike price
#r=interest rate
from io import open

#function for the calculations and write of the results
def Calculations(Name,S0,SH,ST,K,r):
	VH=SH-K # max value option
	VT=0 #min value option
	# constants for the operations
	u=SH/S0
	d=ST/S0
	p=(1+r-d)/(u-d)
	q=(u-1-r)/(u-d)
	#final values
	V0=(p*VH+q*VT)/(1+r) #value of the derivate
	Delta=(VH-VT)/(SH-ST) #number of stocks
	B=(SH-VH*Delta)/(1+r) #number of bonds
	#Here we print the values
	Call_options_result_file=open("Call_options_result.txt","a")
	Call_options_result_file.write("\n" )
	Call_options_result_file.write(Name)
	Call_options_result_file.write("\n" )
	Call_options_result_file.write("Option Value: " )
	Call_options_result_file.write(str(V0))
	Call_options_result_file.write("  Number of stocks: " )
	Call_options_result_file.write(str(Delta))
	Call_options_result_file.write("  Number of bonds: " )
	Call_options_result_file.write(str(B))
	Call_options_result_file.write("\n" )
	Call_options_result_file.close()

#main
#extraction of the information about the call options
Call_options_info_file=open("Call_options_infoV0.txt","r")
text_lines=Call_options_info_file.readlines()

number_of_data=int(text_lines[0])*7
i=1
while i<= number_of_data: # we pass the data of the txt file to the programm to calculate the ratios and do the tests
	Name=str(text_lines[i])
	i=i+1
	S0=float(text_lines[i])
	i=i+1
	SH=float(text_lines[i])
	i=i+1
	ST=float(text_lines[i])
	i=i+1
	K=float(text_lines[i])
	i=i+1
	r=float(text_lines[i])
	i=i+2
	Calculations(Name,S0,SH,ST,K,r)

Call_options_info_file.close()