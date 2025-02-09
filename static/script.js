// static/script.js

let timerDisplay = document.getElementById('timerDisplay');
let startButton = document.getElementById('startButton');
let stopButton = document.getElementById('stopButton');
let socket = new WebSocket("ws://localhost:8000/ws/timer");

startButton.onclick = function() {
    fetch('/start_timer/1') // Start 25-minute Pomodoro timer
        .then(response => response.json())
        .then(data => {
            startButton.disabled = true;
            stopButton.disabled = false;
        });
};

stopButton.onclick = function() {
    fetch('/stop_timer')
        .then(response => response.json())
        .then(data => {
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
