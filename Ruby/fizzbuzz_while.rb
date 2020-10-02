puts "Type a number: "
num = gets.to_i
cont = 1

while cont <= num do
    if cont % 3 == 0 and cont % 5 == 0
        puts "fizzbuzz"
    elsif cont % 3 == 0
        puts "fizz"
    elsif cont % 5 == 0
        puts "buzz"
    else
        puts cont
    end
    cont += 1
end
