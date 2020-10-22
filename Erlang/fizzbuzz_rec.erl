% FizzBuzz solve with recursion in erlang.
% Author : @verebecske

-module(fizzbuzz_rec).
-export([start/0]).

start() -> fizzbuzz(100).
fizzbuzz(1) -> io:fwrite("1\n");
fizzbuzz(N) ->
    fizzbuzz(N-1),
    case N of
        N when (N rem 15) == 0 -> io:fwrite("fizzbuzz\n");
        N when (N rem 5) == 0 -> io:fwrite("buzz\n");
        N when (N rem 3) == 0 -> io:fwrite("fizz\n");
        N -> io:fwrite("~p\n",[N])
    end.
                                  