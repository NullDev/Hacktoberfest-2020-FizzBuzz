-- ==============================================================================
--   File . . . . . . oracle.sql
--   Author . . . . . CreepSore
--   Last Edit. . . . 2020-10-01 08:25
--   Description. . . Selects the FizzBuzz-Sequence as a table
--                    See: https://github.com/NLDev/Hacktoberfest-2020-FizzBuzz
-- ==============================================================================

 select nvl(decode(mod(level, 3), 0, 'Fizz', '') || decode(mod(level, 5), 0, 'Buzz', ''), level)
   from dual
connect by level <= 100;