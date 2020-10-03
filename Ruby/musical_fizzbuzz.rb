# A musical fizzbuzz using sonicpi https://sonic-pi.net/
# Play an G5 along with each fizz
# Play an D#5 along with each buzz
# Play a  D# chord along with each fizzbuzz
# Otherwise kick the drums
# Sometimes snare randomly

define :fizz_buzz_player do |n|
  1.upto(n) do |i|
    print i
    if i % 15 == 0
      play 72
      play 75
      play 79
      print "FizzBuzz"
    elsif i % 5 == 0
      play 75
      print "Buzz"
    elsif i % 3 == 0
      play 79
      print "Fizz"
    else
      play sample :drum_heavy_kick
    end
    
    sample :drum_snare_hard if one_in(4)
    sleep(1)
  end
end


fizz_buzz_player 100
