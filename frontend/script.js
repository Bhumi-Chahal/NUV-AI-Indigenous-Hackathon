document.getElementById("fetchBtn").addEventListener("click", () => {
  const output = document.getElementById("output");
  output.innerHTML = "Fetching data...";

  fetch("http://127.0.0.1:8000/test") // 🔥 change to your backend URL
    .then(response => response.json())
    .then(data => {
      output.innerHTML = JSON.stringify(data, null, 2);
    })
    .catch(error => {
      output.innerHTML = "Error: " + error;
    });
});
