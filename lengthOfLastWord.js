var lengthOfLastWord = function(s) {
   s = s.trim();
   if(!s.match(/\s/)) {
       return s.length;
   }
    let lastWord = [];
    for(let i = s.length - 1; i >= 0; i--) {
        if(s[i] !== " ") {
            lastWord.push(s[i])
        } else if (s[i] === " " && lastWord.length >= 1) {
            return lastWord.length;
        }
    }
}