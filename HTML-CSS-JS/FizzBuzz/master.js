const box = document.querySelector('.box');

for (let i = 1; i <= 100; i++) {
    setTimeout(function timer() {

        if (i % 3 === 0 && i % 5 === 0) {
            document.getElementsByClassName('boomer')[0].style.display = 'block';
            document.querySelector('.boomer-title').innerHTML = 'FizzBuzz';
        }
        else if (i % 3 === 0) {
            document.getElementsByClassName('boomer')[0].style.display = 'block';
            document.querySelector('.boomer-title').innerHTML = 'Fizz';
        }
        else if (i % 5 === 0) {
            document.getElementsByClassName('boomer')[0].style.display = 'block';
            document.querySelector('.boomer-title').innerHTML = 'Buzz';
        }
        else {
            document.getElementsByClassName('boomer')[0].style.display = 'none';
            var j = String(i)
            var num = j.split("")

            if (num.length == 1) {
                box.innerHTML = '';

                var img = document.createElement("img");
                img.src = "./svg/" + 0 + ".svg";
                box.appendChild(img);

                var img = document.createElement("img");
                img.src = "./svg/" + 0 + ".svg";
                box.appendChild(img);

                var img = document.createElement("img");
                var id = parseInt(num[0])
                img.src = "./svg/" + id + ".svg";
                box.appendChild(img);
            }
            else if (num.length == 2) {
                box.innerHTML = '';

                var id1 = parseInt(num[0])
                var id2 = parseInt(num[1])

                var img = document.createElement("img");
                img.src = "./svg/" + 0 + ".svg";
                box.appendChild(img);

                var img = document.createElement("img");
                img.src = "./svg/" + id1 + ".svg";
                box.appendChild(img);

                var img = document.createElement("img");
                img.src = "./svg/" + id2 + ".svg";
                box.appendChild(img);
            }
            else {
                box.innerHTML = '';

                var img = document.createElement("img");
                img.src = "./svg/" + 1 + ".svg";
                box.appendChild(img);

                var img = document.createElement("img");
                img.src = "./svg/" + 0 + ".svg";
                box.appendChild(img);

                var img = document.createElement("img");
                img.src = "./svg/" + 0 + ".svg";
                box.appendChild(img);
            }
        }
    }, i * 500);
}