--author: @nchiarappa

msg = ""

if (1 - 3) % 3 == 0 then

    msg = "Fizz"

else

    if (1 - 5) % 5 == 0 then

        msg = "Buzz"

    else

        msg = 1

    end

end

msg = msg .. "\
"

for i = 2, 100 do

    if (i - 3) % 3 == 0 then

        msg = msg .. "Fizz"

    else

        if (i - 5) % 5 == 0 then

            msg = msg .. "Buzz"

        else

            msg = msg .. i

        end

    end

    if (i - 3) % 3 == 0 then

        if (i - 5) % 5 == 0 then

            msg = msg .. "Buzz"

        else

            msg = msg

        end

    end


    msg = msg .. "\
"

end

print(msg)