// A neat JavaScript one-liner to solve FizzBuzz 
// (from my gist: https://gist.github.com/NLDev/d620a1808fc445afe79875690db78da3)
// Author: @NLDev

Array.apply([], Array(100)).map((e, i) => [["fizz"][i % 3], ["buzz"][i % 5]].join("") || i).forEach(i => console.log(i));
