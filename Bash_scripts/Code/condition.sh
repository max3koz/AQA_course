#! usr/bin/env bash

[[ 4 -gt 3 ]] && echo t || echo f
[[ 3 -gt 4 ]] && echo t || echo f
echo $?

cd ~/Code
[[ -e maths.sh ]] && echo t || echo f

number=7
[[ $number -gt 3 ]] && echo t || echo f
[[ $number -gt 10 ]] && echo t || echo f
[[ -e $number ]] && echo t || echo f

[[ $number -lt 3 ]] && echo t || echo f
[[ $number -lt 10 ]] && echo t || echo f

[[ $number -eq 3 ]] && echo "true" || echo "false"
[[ $number -eq 7 ]] && echo "true" || echo "false"


[[ rhythms =~ [aeiou] ]] && echo t || echo f

my_name=maksym
[[ $my_name =~ ^ma.+m$ ]] && echo t || echo f
