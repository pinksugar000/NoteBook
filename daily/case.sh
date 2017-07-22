#!/bin/bash
dozen=abc
number=123
echo please enter string :
read str
case $str in 
	$dozen ) 
		echo is abc
		;;
	$number )
		echo is 123
		;;
	* )
		echo please enter again
		;;
esac
