// static/script.js

let timerDisplay = document.getElementById('timerDisplay');
let startButton = document.getElementById('startButton');
let stopButton = document.getElementById('stopButton');
let socket = new WebSocket("ws://localhost:8000/ws/timer");

async function fetchAPIData() {
    const response = await fetch('http://localhost:8000/v1/focus_duration');
    const data = await response.json();
    console.log(data.value)
    document.getElementById('timerValue').textContent = data.value
}
fetchAPIData()

// const response = fetch("http:///localhost:8000/stop_timer")
// console.log(response)

startButton.onclick = function() {
    fetch('/start_timer') // Start Pomodoro timer
        .then(response => response.json())
        .then(data => {
            startButton.disabled = true;
            stopButton.disabled = false;
        });
};

stopButton.onclick = function() {
    fetch('/stop_timer')
        .then(response => response.json())
        .then(() => {
            startButton.disabled = false;
            stopButton.disabled = true;
            timerDisplay.innerText = "00:00";
        });
};

// Listen for WebSocket messages (timer updates)
socket.onmessage = function(event) {
    let time = event.data;
    timerDisplay.innerText = time;
    console.log(typeof(time));
    if(time == "00:00") {
        startButton.disabled = false;
        stopButton.disabled = true;
        // var audio = new Audio("C:\\triples360\\todo_proposals\\pomodoro\\resources\\avicii_levels.mp3");
        var audio = new Audio("v1/resources/finish_audio/user");
        audio.play()
        // document.getElementById("playButton").click();
    }

};
