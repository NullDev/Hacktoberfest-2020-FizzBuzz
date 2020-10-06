% fizzbuzz in MATLAB

for i = 1:100

  if(mod(i,3) && mod(i,5))

    fprintf('%i\n', i);

  else

    if(~mod(i,3))

      fprintf('fizz');

    end

    if(~mod(i,5))

      fprintf('buzz');

    end

    fprintf('\n');

  end

end
