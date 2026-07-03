let mediaRecorder;

let recordedChunks = [];
let recordingQuestionNumber = 0;

function startRecording() {

    recordedChunks = [];

    recordingQuestionNumber = interview.current + 1;

    mediaRecorder = new MediaRecorder(window.mediaStream);

    mediaRecorder.ondataavailable = (event) => {

        if (event.data.size > 0) {

            recordedChunks.push(event.data);

        }

    };

    mediaRecorder.onstop = saveRecording;

    mediaRecorder.start();

    console.log("Recording Started");

}

function stopRecording() {

    if (
        mediaRecorder &&
        mediaRecorder.state !== "inactive"
    ) {

        mediaRecorder.stop();

    }

}

async function saveRecording() {

    const blob = new Blob(
        recordedChunks,
        {
            type: "video/webm"
        }
    );

    const formData = new FormData();

    formData.append(
        "video",
        blob,
        `question_${recordingQuestionNumber}.webm`
    );

    formData.append(
        "interview_id",
        interview.id
    );

    formData.append(
        "question_number",
        recordingQuestionNumber
    );

    try {

        const response = await fetch(
            "/api/upload-answer",
            {
                method: "POST",
                body: formData
            }
        );

        const result = await response.json();

        console.log(result);

    }
    catch (error) {

        console.error(error);

    }

}