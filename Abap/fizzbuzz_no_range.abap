*&---------------------------------------------------------------------*
*& Report FIZZBUZZ_HACKTOBERFEST_NO_RANGE
*&---------------------------------------------------------------------*
*&
*&---------------------------------------------------------------------*
report fizzbuzz_hacktoberfest_no_range.

parameters: fizzbuzz type i.
data count type i value 1.
data is_multiple_by_three type i.
data is_multiple_by_five type i.

do fizzbuzz times.
is_multiple_by_three = sy-index mod 3.
is_multiple_by_five = sy-index mod 5.

if is_multiple_by_three = 0 and is_multiple_by_five = 0.
    write / 'fizzbuzz'.
    continue.
elseif is_multiple_by_three = 0.
    write / 'fizz'.
elseif is_multiple_by_five = 0.
    write / 'buzz'.
    continue.
else.
    write / sy-index.
endif.
enddo.