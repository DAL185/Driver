"""
1. clarify / assumptions
(1) task: generate a report containing each driver with total miles and avg speed, sort the output by most miles
to least
(2) input: file with some lines  -> output: list of report for each driver's total miles and speed
(3) assumptions: each line is not None or empty string,  no drive past midnight, start time always before the end time, data could be handled in memory
(4) corner case: discard the trips that avg a speed of < 5 mph or > 100 mph -> not in range[5, 100]

2. result
(1) demo examples
input:
Driver Dan
Driver Lauren
Driver Kumi
Trip Dan 07:15 07:45 17.3
Trip Dan 06:12 06:32 21.8
Trip Lauren 12:01 13:16 42.0

output:
Lauren: 42 miles @ 34 mph
Dan: 39 miles @ 47 mph
Kumi: 0 miles


(2) solution summary(high-level):
process the input file, build a dictionary to record each driver's total time and total miles, and calculate the avg speed,
finally build the sorted reports

(3) solution details:
a. init: process the input file, build a list(called lines) of string to record each line
         build a dictionary in format: {driver: [time, miles])}, initially time = 0, miles = 0
         build another dict miles_report in format: miles_report[(total_miles, driver): report]
            for sort the report based on the total miles from most to least
b. traverse lines, for each line:
   case1: command is driver, init the dictionary[driver] = [0, 0]
   case2: command is trip, calculate the time and miles, update the dictionary[driver] with plus the new miles and time
c. for each driver in the dictionary, get the total miles and avg speed, filter the extreme speed that not in range[5, 100],
   build the cur report, and update the miles_report
d. sort keys(total_miles, driver) in miles report in by most miles to least, if miles are same, sort keys in lexi order of
   driver's name
d. traverse sorted keys in miles_report, add each cur report into the final report

(4) coding

3. testing: unit testing
based on each part of the solution details(a-d), test if each part could get the correct result
"""
class ReadSource():
    def __init__(self):
        self.file = open("/Users/lvda/Desktop/2020-2021秋招/OA/Root/driver.txt", encoding= "UTF-8")

    def process_input(self):
        lines = []

        while True:
            cur_line = self.file.readline()
            if cur_line:
                lines.append(cur_line.strip('\n').split(" "))
            else:
                break
        self.file.close()
        return lines

from datetime import datetime
import copy
class DriverReport():
    def report(self):
        # init: read the input file
        dictionary = {}
        self.miles_report = {}
        lines = ReadSource().process_input()
        #print(lines)

        # traverse each line check the command's case, build dictionary
        for line in lines:
            # case1
            if line[0] == "Driver":
                dictionary[line[1]] = [0, 0]
            # case2
            else:
                driver, miles = line[1], line[4]
                start_time, end_time = line[2], line[3]
                time_diff = self.get_time_diff(start_time, end_time)
                dictionary[driver][0] += time_diff
                dictionary[driver][1] += float(miles)

        # traverse each driver at dictionary, build the report output
        report = self.build_report(dictionary)
        return report

    def get_time_diff(self, start_time, end_time):
        time_1_struct = datetime.strptime(start_time, "%H:%M")
        time_2_struct = datetime.strptime(end_time, "%H:%M")
        seconds = (time_2_struct - time_1_struct).seconds / 3600
        return seconds

    def build_report(self, dictionary):
        # init
        report = []

        # traverse each driver
        for driver, time_miles in dictionary.items():
            # init
            cur_report = []
            # add driver
            cur_report.append(driver + ':')


            # check if the total miles is 0
            if time_miles[1] == 0:
                cur_report.append('0 miles')
                self.miles_report[(0, driver)] = " ".join(copy.deepcopy(cur_report))

            else:
                speed = int(round(time_miles[1] / time_miles[0]))

                # filter the extreme speed
                if speed not in range(5, 101):
                    #print("Driver with extremie speed: " + str((driver, speed)))
                    continue

                total_miles = int(round(time_miles[1]))
                cur_report.append(str(total_miles) + " miles @")
                cur_report.append(str(speed) + " mph")
                self.miles_report[(total_miles, driver)] = " ".join(copy.deepcopy(cur_report))

        # sort the report based on the miles from most to least
        # print(self.miles_report)
        sorted_keys = sorted(self.miles_report, reverse=True)
        for key in sorted_keys:
            report.append(self.miles_report[key])
        #print(report)
        return report


if __name__ == '__main__':

    reports = DriverReport().report()
    for re in reports:
        print(re)

