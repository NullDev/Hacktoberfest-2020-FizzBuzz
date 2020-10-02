// Procedurally generates a word for every number (after 1), so that every number is made from the sum of its factors' words.
// Author: @tamirco2003

const onsets = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'];
const nuclei = ['a', 'e', 'i', 'o', 'u'];
const codas = ['f', 'l', 'm', 'n', 'r', 's', 't', 'v', 'z'];

function generateWord() {
  let onset = onsets[Math.floor(Math.random() * onsets.length)];
  let nucleus = nuclei[Math.floor(Math.random() * nuclei.length)];
  let coda = codas[Math.floor(Math.random() * codas.length)].repeat(2);

  return onset + nucleus + coda;
}

function generateFactorWords(upTo, fizzbuzz) {
  let words = new Set(); // Set to make sure there are no duplicates.

  while (words.size < upTo - 1) {
    words.add(generateWord());

    if (fizzbuzz) {
      if (words.size === 3 - 2) {
        if (words.has('Fizz')) words.remove('Fizz');
        else words.add('Fizz');
      } else if (words.size === 5 - 2) {
        if (words.has('Buzz')) words.remove('Buzz');
        else words.add('Buzz');
      }
    }
  }

  return [...words];
}

function findFactors(num) {
  const max = Math.sqrt(num);
  let factors = new Set();

  for (let i = 2; i <= max; i++) {
    if (num % i === 0) {
      factors.add(i);
      factors.add(num / i);
    }
  }

  factors.add(num);

  return [...factors];
}

function fizzBuzz(words) {
  console.log(1);

  for (let i = 2; i < words.length + 2; i++) {
    let factors = findFactors(i);
    let wordList = factors.map((value) => words[value - 2]);
    console.log(wordList.join(''));
  }
}

fizzBuzz(generateFactorWords(100, true));
