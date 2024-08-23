#! / usr/bin/env bash

true && echo "Programm 1 was executed."
false && echo "Programm 2 was executed."


true && echo "Program 1 was executed."
false && echo "Program 2 was executed."

## Program 1 was executed.



false && true && echo Hello
echo 1 && false && echo 3
echo Athos && echo Porthos && echo Aramis

## 1
## Athos
## Porthos
## Aramis



true || echo "Program 1 was executed."
false || echo "Program 2 was executed."

## Program 2 was executed.



false || echo 1 || echo 2
echo 3 || false || echo 4
echo Athos || echo Porthos || echo Aramis

## 1
## 3
## Athos



echo Athos || echo Porthos && echo Aramis
echo Gaspar && echo Balthasar || echo Melchior
## Athos
## Aramis
## Gaspar
## Balthasar
