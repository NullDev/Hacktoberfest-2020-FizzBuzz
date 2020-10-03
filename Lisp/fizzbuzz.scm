(define (multiple? x y)
  (= 0 (modulo x y)))

(define (fizzbuzz-iter n i)
  (cond ((and (multiple? i 5) (multiple? i 3)) (display "FizzBuzz"))
        ((multiple? i 3) (display "Fizz"))
        ((multiple? i 5) (display "Buzz"))
        (else (display i)))
  (newline)
  (if (> n i)
      (fizzbuzz-iter n (+ i 1))))

(define (fizzbuzz n)
  (fizzbuzz-iter n 1))

(newline)
(fizzbuzz 100)
