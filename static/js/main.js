function sendQuestion() {
    const question = document.getElementById("question").value;
    fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: question })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("response").textContent = data.answer;
    });
}