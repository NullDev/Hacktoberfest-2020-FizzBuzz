;Iterative fizzbuzz
;Author: Emblazion

(defn fizzbuzz []
  (doseq [x (range 1 101)]
    (cond
      (and (= (mod x 3) 0) (= (mod x 5) 0)) (println "FizzBuzz")
      (= (mod x 3) 0) (println "Fizz")
      (= (mod x 5) 0) (println "Buzz")
      :else (println x))))

(fizzbuzz)