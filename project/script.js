function talkToAssistant() {
  const input = document.getElementById("user-input").value;
  const output = document.getElementById("assistant-output");

  if (input.toLowerCase().includes("hello")) {
    output.innerText = "Hey there! Looking for trending news?";
  } else if (input.toLowerCase().includes("trending")) {
    output.innerText = "Latest trend: AI Politics, Tech Stocks rising!";
  } else {
    output.innerText = "Let me check that for you...";
  }
}
document.getElementById('file').addEventListener('change', function(e) {
  const file = e.target.files[0];
const previewArea = document.getElementById('previewArea');
  const filename = document.getElementById('filename');
  previewArea.innerHTML = '';
  filename.textContent = '';

  if (!file) return;

  filename.textContent = `Selected file: ${file.name}`;

  if (file.type.startsWith('image/')) {
    const img = document.createElement('img');
    img.src = URL.createObjectURL(file);
    previewArea.appendChild(img);
  } else if (file.type.startsWith('video/')) {
    const video = document.createElement('video');
    video.src = URL.createObjectURL(file);
    video.controls = true;
    previewArea.appendChild(video);
  } else {
    previewArea.innerHTML = '<p>Preview not available for this file type.</p>';
  }
});
</script>
```
