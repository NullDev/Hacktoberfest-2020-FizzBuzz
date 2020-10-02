(def fizz?#(zero?(mod % 3)))
(def buzz?#(zero?(mod % 5)))
(def fizzbuzz?#(and(fizz? %)(buzz?%)))


(defn fizzbuzz
    #(cond
    (fizzbuzz? %) "FizzBuzz"
    (fizz? %) "Fizz"
    (buzz? %) "Buzz"
    :elese %))

(map fizzbuzz (range 1 101))
