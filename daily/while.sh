a=1
while [ $a -le 10 ] 
do 
	echo -n $a
	((a=$a+1))
done
