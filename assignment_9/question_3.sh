MAX=50
for (( i=1; i<=$MAX; i++ )) 
do
arr[$i]=$i
done
echo ${arr[@]}
