function createAbortableFetch(url) {
  const controller = new AbortController();
  const signal = controller.signal;
  const fetchPromise = fetch(url, { signal });

  return { fetchPromise, abort: () => controller.abort() };
}


const { fetchPromise, abort } = createAbortableFetch('https://example.com');

fetchPromise.catch(e => console.log('Fetch aborted or failed', e));
abort(); 
