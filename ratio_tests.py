import csv
import datetime
import matplotlib.pyplot as plt
import numpy as np

file = open('corona.csv')
data = []
reader = csv.reader(file)
iterator = iter(reader)
next(iterator)
errors = 0
in_progress = 0
data_test = {}
data_result = {}

def getTime(time):
	try:
		return datetime.datetime.strptime(time, "%Y-%m-%d").date()
	except:
		return None
		
for row in iterator:
	test_time = getTime(row[0])
	result_time = getTime(row[1])
	if test_time is None:
		test_time = result_time
	if result_time is None:
		result_time = test_time
	if (test_time is None) and (result_time is None):
		errors += 1
		print(row)
		continue
	if row[2] == 'בעבודה':
		in_progress +=1
		continue
	is_positive = True if row[2] == 'חיובי' else False
	if not test_time in data_test:
		data_test[test_time] = (0,0)
	if not result_time in data_result:
		data_result[result_time] = (0,0)
	data_test[test_time] = (data_test[test_time][0]+is_positive, data_test[test_time][1]+1)
	data_result[result_time] = (data_result[result_time][0]+is_positive, data_result[result_time][1]+1) 
	
print("errors: " + str(errors))
print("in_progress: " + str(in_progress))
# print(data)

ratios = {}
x_test = []
y_test = []
for time in sorted(data_test.keys()):
	x_test.append(time)
	y_test.append((data_test[time][0]*100.0)/(data_test[time][1]*1.0))

x_result = []
y_result = []
for time in sorted(data_result.keys()):
	x_result.append(time)
	y_result.append((data_result[time][0]*100.0)/(data_result[time][1]*1.0))


plt.plot(x_test, y_test, color='olive', label='by test date')
plt.plot(x_result, y_result, color='skyblue', label = 'by result date')
plt.show()
