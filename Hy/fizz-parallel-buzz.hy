;; Type annotated, parallel implementation of the fizzbuzz problem.
;; Author: @atgmello

(import [concurrent.futures [ProcessPoolExecutor]])
(import [os [cpu-count]])

(defn fizzbuzz? [^int n] (zero? (+ (% n 3) (% n 5))))
(defn fizz? [^int n] (zero? (% n 3)))
(defn buzz? [^int n] (zero? (% n 5)))

(defn check-which [^int n] (cond [(fizzbuzz? n) "FizzBuzz"]
                                 [(fizz? n) "Fizz"]
                                 [(buzz? n) "Buzz"]
                                 [True n]))

(defn fizzbuzz [^int n]
  (setv ^ProcessPoolExecutor executor
        (ProcessPoolExecutor :max-workers (cpu-count)))
  (setv ^list res (.map executor check-which (range 1 (+ n 1))))
  (.shutdown executor)
  (for [r res] (print r)))

(fizzbuzz 100)
