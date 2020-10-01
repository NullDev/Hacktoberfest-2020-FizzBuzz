<?php
// A simple fizzbuzz script written in PHP using a class
// Author: @tony133
declare(strict_types=1);

class FizzBuzz
{
    public function process($collection): array
    {
        $result = array_map(function ($item) {

            $response = '';

            if ($item % 3 === 0) {
                $response .= 'Fizz';
            }

            if ($item % 5 === 0) {
                $response .= 'Buzz';
            }

            if ($response === '') {
                $response = $item;
            }

            return $response;

        }, $collection);

        return $result;
    }
}
