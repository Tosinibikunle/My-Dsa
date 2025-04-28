function getAllMatches(str, regex) {
      return [...str.matchAll(regex)];
      }

      // Example:
      const myString = 'cat bat mat';
      const myRegex = /\b\w{3}\b/g;

      const matches = getAllMatches(myString, myRegex);
      console.log(matches.map(m => m[0])); // ['cat', 'bat', 'mat']
