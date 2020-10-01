(defun fizzbuzz (num)
       (cond
         ((= num 101) (format t ""))
         ((and (= 0 (mod num 3)) (= 0 (mod num 5))) (or (format t "FizzBuzz~%") (fizzbuzz (1+ num))) )
         ((= 0 (mod num 3))   (or (format t "Fizz~%") (fizzbuzz (1+ num))))
         ((= 0 (mod num 5))  (or (format t "Buzz~%") (fizzbuzz (1+ num))))
         (t  (or (format t "~d~%" num) (fizzbuzz (1+ num))))))

(fizzbuzz 1)