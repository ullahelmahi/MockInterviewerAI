const video =
    document.getElementById("camera");

async function startCamera() {

    try {

        const stream =
            await navigator.mediaDevices.getUserMedia({

                video: true,

                audio: true

            });

        video.srcObject = stream;

        window.mediaStream = stream;

    }

    catch(error) {

        alert("Camera or microphone permission denied.");

        console.error(error);

    }

}