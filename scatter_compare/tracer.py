
def isbetween(left,right,test):
	return (left-test)*(test-right)>=0

def interpolate(x1,y1,x2,y2,x,y):
	#print x1,x,x2
	#print y1,y,y2
	return (x*(y2-y1)+(x2*y1-x1*y2)-y*(x2-x1))/(x2-x1)

with open('step1_output1.txt') as f:
	t1_list = []
	r1_list = []
	for line in f.readlines():
		t=float(line.strip().split('\t')[0])
		r=float(line.strip().split('\t')[1])
		t1_list.append(t)
		r1_list.append(r)

with open('step1_output2.txt') as f:
	t2_list = []
	r2_list = []
	for line in f.readlines():
		t=float(line.strip().split('\t')[0])
		r=float(line.strip().split('\t')[1])
		t2_list.append(t)
		r2_list.append(r)

print len(t1_list);
print len(t2_list);

left1 = 0
right1 = 1
test2 = 0

#assert (len(t1_list) < len(t2_list))
assert isbetween(t1_list[left1],t1_list[right1],t2_list[test2]) 
t_list = []
d_list = []

# while True:
# 	if isbetween(t1_list[left1],t1_list[right1],t2_list[test2]):
# 		t_list.append(t2_list[test2])
# 		# interpolation
# 		x1 = t1_list[left1]
# 		x2 = t1_list[right1]
# 		y1 = r1_list[left1]
# 		y2 = t1_list[right1]
# 		x = t2_list[test2]
# 		d = interpolate(x1,y1,x2,y2,x)-r2_list[test2]
# 		break
for i in range(len(t1_list)-1):
	x1 = t1_list[i]
	x2 = t1_list[i+1]
	y1 = r1_list[i]
	y2 = r1_list[i+1]
	x = t2_list[i]
	y = r2_list[i]
	d = interpolate(x1,y1,x2,y2,x,y)
	t_list.append(x)
	d_list.append(d)

with open('trace.txt', 'w+') as f:
	for i in range(len(t_list)):
		f.write('%f\t%f\n'%(t_list[i],d_list[i]))

#print d
