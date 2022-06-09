"""
Definitions to process data

By Erick F.
09/06/2022
"""
import argparse

def start_parser():
	'''Start parser set up txt input argument and return the file path'''

	parser = argparse.ArgumentParser()
	parser.add_argument("-t", "--txtinput", type=str, required=True, help='the txt data input that contains employees, days and hours of work')
	args = parser.parse_args()

	return args.txtinput

def cost_groups_by_time():
	'''There exists two groups of days to work in a week, G1: from monday to friday. and G2: from saturday to sunday.
	According to these groups and the time in a day (an interval) the employee has worked there must be an especific
	hour cost. In the following table groups, intervals and costs in USD are structured'''

	cgbt = {"G1":{"days":set(["MO","TU","WE","TH","FR"]),
				  "interval_1":{"limits":(0,9),"cost":25},
				  "interval_2":{"limits":(9,18),"cost":15},
				  "interval_3":{"limits":(18,24),"cost":20}}, 
			"G2":{"days":set(["SA","SU"]),
			      "interval_1":{"limits":(0,9),"cost":30},
				  "interval_2":{"limits":(9,18),"cost":20},
				  "interval_3":{"limits":(18,24),"cost":25}}} 
	return cgbt

def get_groups_and_intervals_of_belonging(bt, et):
	'''In order to stablish which interval the employment hours falls into'''

	intrvl = set()
	if bt <= cost_groups_by_time()["G1"]["interval_1"]["limits"][1]: 
		intrvl.add(1)
	elif bt > cost_groups_by_time()["G1"]["interval_2"]["limits"][0] and bt <= cost_groups_by_time()["G1"]["interval_2"]["limits"][1]: 
		intrvl.add(2)
	elif bt > cost_groups_by_time()["G1"]["interval_3"]["limits"][0] and bt <= cost_groups_by_time()["G1"]["interval_3"]["limits"][1]:
		intrvl.add(3)
	if et <= cost_groups_by_time()["G1"]["interval_1"]["limits"][1]:
		intrvl.add(1)
	elif et > cost_groups_by_time()["G1"]["interval_2"]["limits"][0] and et <= cost_groups_by_time()["G1"]["interval_2"]["limits"][1]:
		intrvl.add(2)
	elif et > cost_groups_by_time()["G1"]["interval_3"]["limits"][0] and et <= cost_groups_by_time()["G1"]["interval_3"]["limits"][1]:
		if 1 in intrvl: intrvl.add(2)
		intrvl.add(3)

	return intrvl

def calculate_hours_by_interval(bt, et, intrvl):
	'''Stablish how many hours exist in every interval of time the employee has worked on'''
	
	hours_by_interval = {}
	if len(intrvl) == 1: #just an interval
		hours_by_interval["interval_" + str([i for i in intrvl][0])] = et - bt
	else:
		if len(intrvl) == 2: #two intervals
			intrvl_list = [i for i in intrvl]
			if intrvl_list[0] == 1: #belongs to intervals 1 and 2
				hours_by_interval["interval_1"] = cost_groups_by_time()["G1"]["interval_1"]["limits"][0] + cost_groups_by_time()["G1"]["interval_1"]["limits"][1] - bt
				hours_by_interval["interval_2"] = et - cost_groups_by_time()["G1"]["interval_1"]["limits"][1] - 1
			else: #belongs to intervals 2 and 3
				hours_by_interval["interval_2"] = cost_groups_by_time()["G1"]["interval_2"]["limits"][0] + cost_groups_by_time()["G1"]["interval_2"]["limits"][1] - bt
				hours_by_interval["interval_3"] = et - cost_groups_by_time()["G1"]["interval_2"]["limits"][0] - 1
		else: #there is 3 intervals
			hours_by_interval["interval_1"] = cost_groups_by_time()["G1"]["interval_1"]["limits"][0] + cost_groups_by_time()["G1"]["interval_1"]["limits"][1] - bt
			hours_by_interval["interval_2"] = cost_groups_by_time()["G1"]["interval_2"]["limits"][1] - cost_groups_by_time()["G1"]["interval_2"]["limits"][0]
			hours_by_interval["interval_3"] = et - cost_groups_by_time()["G1"]["interval_3"]["limits"][0]
	return hours_by_interval

def calculate_payment_by_day(hours_by_interval, day):
	'''Calculate payment by day for employee'''
	
	pymnt = 0
	if day in cost_groups_by_time()["G1"]["days"]:
		#belongs to G1
		for interval in hours_by_interval:
			pymnt += hours_by_interval[interval] * cost_groups_by_time()["G1"][interval]["cost"]
	elif day in cost_groups_by_time()["G2"]["days"]:
		#belongs to G2
		for interval in hours_by_interval:
			pymnt += hours_by_interval[interval] * cost_groups_by_time()["G2"][interval]["cost"]
	else:
		pass

	return pymnt

def calculate_total_payment(payment_by_day):
	'''Summation of payments by day'''

	total_payment = 0
	for day in payment_by_day:
		total_payment += payment_by_day[day]
	return total_payment
