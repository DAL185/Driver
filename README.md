## Overview
* A project to process the data based on driver's information

## Analysis Process

### 1. Clarification / Assumptions 
* (1) Task: generate a report containing each driver with total miles and avg speed, sort the output by most miles
to least
* (2) Input: file with each driver's information -> output: list of report for each driver's total miles and speed 
* (3) Assumptions: each line is not None or empty string, no drive past midnight, start time always before the end time, data could be handled in memory
* (4) Corner Case: discard the trips that avg a speed of < 5 mph or > 100 mph -> not in range[5, 100]

### 2. Result
#### (1) Demo Examples
```
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
```

#### (2) Solution Summary(High-Level)
* process the input file, build a dictionary to record each driver's total time and total miles, and calculate the avg speed, finally build the sorted reports

#### (3) solution details
* a. Init: process the input file, build a list(called lines) of string to record each line
         build a dictionary in format: {driver: [time, miles])}, initially time = 0, miles = 0
         build another dict miles_report in format: miles_report[(total_miles, driver): report]
            for sort the report based on the total miles from most to least
* b. Traverse lines, for each line:
   case1: command is driver, init the dictionary[driver] = [0, 0]
   case2: command is trip, calculate the time and miles, update the dictionary[driver] with plus the new miles and time
* c. For each driver in the dictionary, get the total miles and avg speed, filter the extreme speed that not in range[5, 100],
   build the cur report, and update the miles_report
* d. Sort keys(total_miles, driver) in miles report in by most miles to least, if miles are same, sort keys in lexi order of
   driver's name
* d. Traverse sorted keys in miles_report, add each cur report into the final report

#### (4) coding(please check the DriverReport.py)

### 3. Testing
* I decided to use unit testing based on the demo example data to check each part of the solution details(a-d), as well as some corner case test such as extreme speed not in range[5, 100]

#### 3.1 Unit testing for each solution details part 
* a. Because initally two dictionary would be empty, so first step we just test if we have sucessfully read the input file and built the list 

![a](https://github.com/DAL185/Driver/blob/master/Testing/a.%20test%20input%20file%20read.png)

* b. The second test is to check if the dictionary which in format{driver:[total_time(in hours), total_miles]} has been built sucessfully 
![b](https://github.com/DAL185/Driver/blob/master/Testing/b.%20test%20the%20dictionary.png)

* c. The thrid test is to check if the other dict called miles_report, which is in format {(total_miles, driver): driver's report} and used for sort the report firstly by most total_miles to least, and secondly by Driver name's lexicographical order  
![c](https://github.com/DAL185/Driver/blob/master/Testing/c.%20test%20the%20miles_%20report.png)

* d. The fourth test is to check if the dict miles_report has been sorted sucessfully based on the rule in step c
![d](https://github.com/DAL185/Driver/blob/master/Testing/d.%20test%20sorted%20miles_report.png)

* e. The fifth test is to check the final report 
![e](https://github.com/DAL185/Driver/blob/master/Testing/e.test%20final%20report.png)


#### 3.2 Test corner cases 
* At this part, we test some corner cases with extreme speed that not in range[5, 100], we print those extreme speed with driver's name, and find that they are not in the final report, so the corner case's process is successful
![corner case](https://github.com/DAL185/Driver/blob/master/Testing/corner%20case%20with%20extreme%20speed.png)

