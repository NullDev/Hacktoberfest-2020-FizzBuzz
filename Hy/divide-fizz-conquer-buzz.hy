;; The only way to tackle such a complex problem: Divide and Conquer (sort of).
;; You can call fizzbuzz with dbug = True if it helps you grasp the solution.
;; Author: @atgmello

(require [hy.contrib.walk [let]])
(import [math [floor]])

(defn fizz-buzz [until &optional [debug False]]
  (setv result (list (range 0 until)))
  (defn devide-fizz-conquer-buzz [ini end]
    (if (= ini end)
        (let [res (list)]
          (do
            (if debug
                (print (.format "Leaf reached.\nValue: {}\n" ini)))
            (if (zero? (% ini 3))
                (.append res "Fizz"))
            (if (zero? (% ini 5))
                (.append res "Buzz"))
            (if (zero? (len res))
                (.append res (str ini)))
            (setv (get result (- ini 1)) (str.join "" res))
            (if debug
                (print (.format "Results so far:\n{}\n" result)))))
        (let [pivot (floor (/ (+ ini end) 2))]
           (do
             (if debug (print
                         (.format
                           "Dividing:\nIni: {} Pivot: {} End: {}\n"
                           ini pivot end)))
             (if debug (print
                         (.format
                           "First recursion:\nIni: {}. End: {}\n"
                           ini pivot end)))
             (devide-fizz-conquer-buzz ini pivot)
             (if debug (print
                         (.format
                           "Second recursion:\nIni: {}. End: {}\n"
                           (+ pivot 1) end)))
             (devide-fizz-conquer-buzz (+ pivot 1) end))))
    (return result))
  (for [n (devide-fizz-conquer-buzz  1 until)] (print n)))

(fizz-buzz 100)
