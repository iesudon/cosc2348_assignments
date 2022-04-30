MAX=20

for (( i=0; i<$MAX; i++ )) 
do
arr[$i]=$RANDOM
done
echo "Original Array: "
echo ${arr[*]}

# Performing Bubble sort 
for ((i = 0; i<$MAX; i++))
do
    
    for((j = 0; j<$MAX-$i-1; j++))
    do
    
        if [ ${arr[j]} -gt ${arr[$((j+1))]} ]
        then
            # swap
            temp=${arr[j]}
            arr[$j]=${arr[$((j+1))]}  
            arr[$((j+1))]=$temp
        fi
    done
done

echo "Sorted Array:"
echo ${arr[*]}
