<#
.SYNOPSIS
    Hacktoberfest 2020 submission for the Fizz Buzz challenge!

.NOTES
    FizzBuzz is a program that prints the numbers from 1 to 100. 
    But for multiples of three it prints “Fizz” instead of the number and for the multiples of five, it prints “Buzz”. 
    For numbers which are multiples of both three and five it prints “FizzBuzz”.

.LINK
    https://www.tomdalling.com/blog/software-design/fizzbuzz-in-too-much-detail/
#>

function Start-FizzBuzzing {
    #CmdletBinding()
    param(
        [Parameter(Mandatory=$true)]$range
    )

    function Test-Divisible {
        #CmdletBinding()
        param(
            [Parameter(Mandatory=$true)]$dividend,
            [Parameter(Mandatory=$true)]$divisor
        )

        Write-Verbose "Dividing $dividend By $divisor"

        if ($dividend % $divisor -eq 0){
            return $true
        }
        else{
            return $false
        }
    }

    foreach ($num in $range){
        if ((Test-Divisible -dividend $num -divisor 3) -and (Test-Divisible -dividend $num -divisor 5)){
            "FizzBuzz"
        }
        elseif(Test-Divisible -dividend $num -divisor 3){
            "Fizz"
        }
        elseif(Test-Divisible -dividend $num -divisor 5){
            "Buzz"
        }
        else{
            $num
        }
    }
}

# Call Out Function :)
Start-FizzBuzzing -range (1..100)