#!/bin/bash

find_prime_numbers (){
primesum=0
echo "1"
echo "2"
for((i=3;i<=$1;))
do
    for((j=i-1;j>=2;))
    do
        if [[ $(($i%$j))  -ne 0 ]]
        then
            prime_1=1
        else
            prime_1=0
            break
        fi
    j=`expr $j - 1`
    done
    if [[ $prime_1 -eq 1 ]]
    then
        echo $i
        primesum=$(($primesum+$i))
    fi
    i=$(($i+1))
done
return $primesum
}
sum_prime_numbers ()
{
    find_prime_numbers $1
    primesum=$?
    return $primesum
}

sum_prime_numbers 50
echo $?
