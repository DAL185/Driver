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
* a. init: process the input file, build a list(called lines) of string to record each line
         build a dictionary in format: {driver: [time, miles])}, initially time = 0, miles = 0
         build another dict miles_report in format: miles_report[(total_miles, driver): report]
            for sort the report based on the total miles from most to least
* b. traverse lines, for each line:
   case1: command is driver, init the dictionary[driver] = [0, 0]
   case2: command is trip, calculate the time and miles, update the dictionary[driver] with plus the new miles and time
* c. for each driver in the dictionary, get the total miles and avg speed, filter the extreme speed that not in range[5, 100],
   build the cur report, and update the miles_report
* d. sort keys(total_miles, driver) in miles report in by most miles to least, if miles are same, sort keys in lexi order of
   driver's name
* d. traverse sorted keys in miles_report, add each cur report into the final report

#### (4) coding(please check the DriverReport.py)

### 3. Testing
* I decided to use unit testing based on the demo example data to check each part of the solution details(a-d), as well as some corner case test such as extreme speed not in range[5, 100]

#### 3.1 Unit testing for each solution details part 
* a. because initally two dictionary would be empty, so first step we just test if we have sucessfully read the input file and built the list 

![a](a. test input file read.png)


