for 1..100 -> $iter {
  print "Fizz" if $iter % 3 == 0;
  print "Buzz" if $iter % 5 == 0;
  print $iter unless $iter % 5 == 0 or $iter % 3 == 0;
  print "\n";
}
