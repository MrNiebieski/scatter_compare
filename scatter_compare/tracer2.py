import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from scipy.interpolate import interp1d

def isbetween(left,right,test):
	return (left-test)*(test-right)>=0

def interpolate(x1,y1,x2,y2,x,y):
	#print x1,x,x2
	#print y1,y,y2
	return (x*(y2-y1)+(x2*y1-x1*y2)-y*(x2-x1))/(x2-x1)

with open('step2_input1.txt') as f:
	t1_list = []
	r1_list = []
	for line in f.readlines():
		t=float(line.strip().split('\t')[0])
		r=float(line.strip().split('\t')[1])
		t1_list.append(t)
		r1_list.append(r)

with open('step2_input2.txt') as f:
	t2_list = []
	r2_list = []
	for line in f.readlines():
		t=float(line.strip().split('\t')[0])
		r=float(line.strip().split('\t')[1])
		t2_list.append(t)
		r2_list.append(r)

print len(t1_list);
print len(t2_list);

x_list = []
d_list = []
#interpolate.interp1d
# f1 = interp1d(t1_list, r1_list, "cubic")
# f2 = interp1d(t2_list, r2_list, "cubic")
f1 = interp1d(t1_list, r1_list, "linear")
f2 = interp1d(t2_list, r2_list, "linear")
for x in np.arange(-1.5, 1, 0.02):
	x_list.append(x)
	d_list.append(f1(x)-f2(x))




with open('trace2.txt', 'w+') as f:
	for i in range(len(x_list)):
		f.write('%f\t%f\n'%(x_list[i],d_list[i]))

# plt.plot(x_list,d_list,'o')
# plt.show()
