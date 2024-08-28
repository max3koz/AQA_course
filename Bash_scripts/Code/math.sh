#!/usr/bin/env bash

a=5
b=2

echo $a
echo $b

city="New York"

echo $city

let sum=$a+$b 
let subtrac=$a-$b
let miltiplic=$a\*$b
let division=$a/$b

echo $sum
echo $subtrac
echo $miltiplic
echo $division

echo "22 / $sum" | bc -l
echo "4.2 * 9.15" | bc -l
echo "(6.5 / ($b / 4)) + (6 * 2.2)" | bc -l

files_lines=$(cat math.sh | wc -l)

echo ""
echo "The lines in the math.sh file:" $files_lines

echo ""
echo $(cat math.sh | wc -l)

echo ""
echo $(ls -la)

echo ""
echo "Script arguments: $@"
echo "First arg: $1. Second arg: $2."
echo "Number of arguments: $#"

echo "========================================================="
echo "Type in a string and then press Enter:"
read response
echo "You entered: $response"

echo "========================================================="
echo "Enter first argument:"
read num_1
echo "Enter second argument:"
read num_2
let res=(num_1+num_2)/2
echo "Result is "$res

echo "========================================================="
echo "Enter noun:"
read noun
echo "Enter verb:"
read verb
echo "Enter adjective:"
read adjective
echo "$verb $adjective $noun"

