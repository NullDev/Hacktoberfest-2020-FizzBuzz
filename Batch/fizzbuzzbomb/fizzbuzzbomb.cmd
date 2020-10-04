@echo off
setlocal enableDelayedExpansion
for /l %%N in (1 1 100) do (
  set /a "fizzbuzz=%%N%%15, buzz=%%N%%5, fizz=%%N%%3"
  if !fizzbuzz! == 0 (
    start FizzBuzz.cmd
  ) else if !buzz! == 0 (
    start Buzz.cmd
  ) else if !fizz! == 0 (
    start Fizz.cmd
  ) else echo %%N
)
REM This is pretty much the generic implementation, except for the vaguely fork-bomby behavior
