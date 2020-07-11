console.log('Welcome to my sample javascript program!');

// Let's checkout some funny issues in JS!

[] == ![]; // -> true

false == []; // -> true
false == ![]; // -> true

console.log("b" + "a" + +"a" + "a"); // -> baNaNa

NaN === NaN; // -> false

(![] + [])[+[]] +
  (![] + [])[+!+[]] +
  ([![]] + [][[]])[+!+[] + [+[]]] +
  (![] + [])[!+[] + !+[]];
// -> 'fail'

document.all instanceof Object; // -> true
typeof document.all; // -> 'undefined'

Number.MIN_VALUE > 0; // -> true

[1, 2, 3] + [4, 5, 6]; // -> '1,2,34,5,6'

console.log('View more: https://github.com/denysdovhan/wtfjs');
