function copyToClipboard(text) {
  return navigator.clipboard.writeText(text);
}


copyToClipboard('Hello World!')
  .then(() => console.log('Copied!'))
  .catch(err => console.error('Failed to copy:', err));
