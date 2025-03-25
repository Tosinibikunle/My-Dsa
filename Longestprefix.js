// Write a function to find the longest common prefix string amongst an array of strings.
// If there is no common prefix, return an empty string



var longestCommonPrefix = function(strs) {
    if(!strs.length)
        return ''
    let prefix =''
    const firstElement = strs[0]
    for(let i = 0; i < firstElement.length;i++){
        let pfx = !prefix ? firstElement[i] : prefix + firstElement[i] 
        for(let j = 1; j < strs.length; j++){
            if(!strs[j].startsWith(pfx)){
                return prefix;
            }
        }
        prefix = pfx;
    }
    
    return prefix;
};