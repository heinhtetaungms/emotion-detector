let RunSentimentAnalysis = () => {
    textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("system_response").innerHTML = xhttp.responseText;
        }
        if (this.readyState == 4 && this.status == 400) {
            document.getElementById("system_response").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("POST", "emotionDetector", true);  // Remove the query parameter
    xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");  // Set content type
    xhttp.send(JSON.stringify({ text: textToAnalyze }));  // Send JSON data
}
