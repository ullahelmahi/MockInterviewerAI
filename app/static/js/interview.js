const interviewData = document.getElementById("interview-data");

window.interview = {
    id: interviewData.dataset.interviewId,
    total: Number(interviewData.dataset.total),
    current: 0
};

const startButton = document.getElementById("start-btn");
const startScreen = document.getElementById("start-screen");
const countdownScreen = document.getElementById("countdown-screen");
const countdownNumber = document.getElementById("countdown-number");
const interviewContent = document.getElementById("interview-content");

const questionNumber = document.getElementById("question-number");
const questionCategory = document.getElementById("question-category");
const questionText = document.getElementById("question-text");
const progressBar = document.getElementById("progress-bar");
const readingTimer = document.getElementById("reading-timer");

const finishButton =
    document.getElementById("finish-btn");

const skipButton =
    document.getElementById("skip-btn");

function showQuestion(index) {

    interview.current = index;

    const q = questions[index];

    questionNumber.innerHTML =
        `Question ${q.number} of ${interview.total}`;

    questionCategory.innerHTML =
        q.category;

    questionText.innerHTML =
        q.text;

    progressBar.style.width =
        `${((index + 1) / interview.total) * 100}%`;

    finishButton.disabled = true;

    skipButton.disabled = true;

    startReadingTimer();

}

startButton.onclick = () => {

    startCamera();

    startScreen.style.display = "none";

    countdownScreen.style.display = "block";

    let count = 3;

    countdownNumber.innerHTML = count;

    const countdown = setInterval(() => {

        count--;

        if (count > 0) {

            countdownNumber.innerHTML = count;

        } else {

            clearInterval(countdown);

            countdownScreen.style.display = "none";

            interviewContent.style.display = "block";

            showQuestion(0);

        }

    }, 1000);

};

finishButton.onclick = () => {

    stopRecording();

    clearInterval(window.answerCountdown);

    if (interview.current + 1 < interview.total) {

        showQuestion(interview.current + 1);

    }
    else {

        interviewContent.innerHTML = `

            <div class="text-center mt-5">

                <h2>🎉 Interview Finished</h2>

                <p>Generating AI Report...</p>

            </div>

        `;
        setTimeout(() => {
            window.location.href = `/report/generate/${interview.id}`;
        }, 1500);

    }

};

skipButton.onclick = () => {
    
    stopRecording();

    clearInterval(window.answerCountdown);

    if (interview.current + 1 < interview.total) {

        showQuestion(interview.current + 1);

    }
    else {

        interviewContent.innerHTML = `

            <div class="text-center mt-5">

                <h2>🎉 Interview Finished</h2>

                <p>Generating AI Report...</p>

            </div>

        `;
        setTimeout(() => {
            window.location.href = `/report/generate/${interview.id}`;
        }, 1500);

    }

};