function startReadingTimer() {

    let seconds = 5;

    readingTimer.innerHTML = seconds;

    const readingCountdown = setInterval(() => {

        seconds--;

        readingTimer.innerHTML = seconds;

        if (seconds <= 0) {

            clearInterval(readingCountdown);

            beginCountdown();

        }

    }, 1000);

}

function beginCountdown() {

    finishButton.disabled = false;

    skipButton.disabled = false;

    startRecording();

    let seconds = questions[interview.current].time;

    const timer = document.getElementById("timer");

    function updateTimer() {

        const minutes = Math.floor(seconds / 60);

        const remaining = seconds % 60;

        timer.innerHTML =
            String(minutes).padStart(2, "0")
            + ":"
            + String(remaining).padStart(2, "0");

        if (seconds <= 0) {

            stopRecording();

            clearInterval(window.answerCountdown);

            if (interview.current + 1 < interview.total) {

                showQuestion(interview.current + 1);

            } else {

                interviewContent.innerHTML = `

                    <div class="text-center mt-5">

                        <h2>🎉 Interview Finished</h2>

                        <p>Generating AI Report...</p>

                    </div>

                `;

            }

        }

        seconds--;

    }

    updateTimer();

    window.answerCountdown = setInterval(updateTimer, 1000);

}