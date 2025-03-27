const isPalindrome = function(x) {
    if (x < 0) return false;
    
   return x.toString().split('').reverse().join('') === x.toString(); 
}