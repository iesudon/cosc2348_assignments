#!/bin/bash
# bash scripting can't handle decimals
home_rent_allowance=0
home_rent_allowance_percent=0
gross_salary=0
salary=${1}
if [ -z $salary ]
then
echo "Please enter a number as an argument"
elif [ $salary -lt 10000 ]
then
home_rent_allowance_percent="20/100"
dearness_allowance_percent="80/100"
elif [[ $salary -ge 10001 && $salary -lt 20000 ]]
then
home_rent_allowance_percent="25/100"
dearness_allowance_percent="90/100"
elif [ $salary -ge 20001 ]
then
home_rent_allowance_percent="30/100"
dearness_allowance_percent="95/100"
else
echo "Something went wrong"
fi
home_rent_allowance=$((home_rent_allowance_percent * salary))
dearness_allowance=$((dearness_allowance_percent * salary))
gross_salary=$((home_rent_allowance + dearness_allowance + salary))
echo $salary
echo $dearness_allowance
echo $home_rent_allowance
echo $gross_salary
