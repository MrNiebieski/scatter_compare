import math
with open('input1.txt') as f:
	x_list = []
	y_list = []
	for line in f.readlines():
		x=float(line.strip().split('\t')[0])
		y=float(line.strip().split('\t')[1])
		x_list.append(x)
		y_list.append(y)
		#print x,y

x_mean=sum(x_list)/len(x_list)
y_mean=sum(y_list)/len(y_list)
theta_list = []
rho_list = []
for i in range(len(x_list)):
	if x == x_mean:
		theta = math.pi/2
	else:
		theta = math.atan((y_list[i]-y_mean)/(x_list[i]-x_mean))
	rho = math.sqrt((y_list[i]-y_mean)*(y_list[i]-y_mean) + (x_list[i]-x_mean)*(x_list[i]-x_mean))
	rho_list.append(rho)
	theta_list.append(theta)

#print rho_list
#print theta_list

with open('step1_output1.txt', 'w+') as f:
	for i in range(len(x_list)):
		f.write('%f\t%f\n'%(theta_list[i],rho_list[i]))