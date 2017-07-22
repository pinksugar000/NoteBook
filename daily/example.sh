#!/bin/bash

echo please enter your num
read num
if [ $num > 0 ] 
then  expr $num \* $num 
else if [ $num < 0 ]
then echo $num
else echo zero
fi
fi



































