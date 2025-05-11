function buildSuffixArray(str) {
      const n = str.length;
        const suffixes = [];

          for (let i = 0; i < n; i++) {
              suffixes.push({ index: i, suffix: str.substring(i) });
                }

                  suffixes.sort((a, b) => a.suffix.localeCompare(b.suffix));

                    // Extract and return just the starting indices
                      return suffixes.map(s => s.index);
                      }
}