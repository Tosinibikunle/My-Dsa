
var mySqrt = function(x) {
    if (x < 0) { return null; }
    if (x < 2) { return x; }
    let guess = x;
    while (Math.abs(guess * guess - x) > 0.5) {
        guess = (guess + x / guess) / 2;
    }
    return parseInt(guess, 10);    
};