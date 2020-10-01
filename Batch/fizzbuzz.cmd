@echo off
setlocal enableDelayedExpansion
for /l %%N in (1 1 100) do (
  set /a "fizzbuzz=%%N%%15, buzz=%%N%%5, fizz=%%N%%3"
  if !fizzbuzz! == 0 (
    echo FizzBuzz
  ) else if !buzz! == 0 (
    echo Buzz
  ) else if !fizz! == 0 (
    echo Fizz
  ) else echo %%N
)