val_1=100
val_2=10
val_3=67
val_4=70
val_5=19

out_1=$((val_1+val_2))
echo $out_1
out_1=$((val_1-val_3))
echo $out_1
out_1=$((val_3*val_2))
echo $out_1
out_1=$((val_4/val_5))
echo $out_1
out_1=$((val_3%val_2))
echo $out_1
out_1=$((val_5**val_1))
echo $((--val_5))
echo $((val_1++))
