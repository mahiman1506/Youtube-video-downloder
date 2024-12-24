document.getElementById('download-btn').addEventListener('click', () => {
  const url = document.getElementById('video-url').value;
  if (url) {
    document.getElementById('status').innerText = 'Processing...';

    // Send the URL to the Python backend (via a server or local API)
    fetch('http://127.0.0.1:5000/download', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ url }),
    })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        document.getElementById('status').innerText = 'Download started!';
      } else {
        document.getElementById('status').innerText = 'Failed to download video.';
      }
    })
    .catch(error => {
      document.getElementById('status').innerText = 'Error: ' + error.message;
    });
  } else {
    document.getElementById('status').innerText = 'Please enter a URL.';
  }
});
  