async function sendMessage() {
    let input = document.getElementById("user-input");
    let message = input.value.trim();

    if (message === "") return;

    let chatBox = document.getElementById("chat-box");

    // 👤 User message
    chatBox.innerHTML += `
        <div class="user">
            🧑 ${message}
        </div>
    `;

    input.value = "";
    chatBox.scrollTop = chatBox.scrollHeight;

    try {
        let response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: message })
        });

        let data = await response.json();

        // 🤖 Assistant response
        chatBox.innerHTML += `
            <div class="bot">
                🤖 ${data.response}
            </div>
        `;

    } catch (error) {
        chatBox.innerHTML += `
            <div class="bot">
                ⚠️ Error connecting to server
            </div>
        `;
    }

    chatBox.scrollTop = chatBox.scrollHeight;
}


// 🎯 Enter key support
function handleKeyPress(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        sendMessage();
    }
}



// 🎤 Voice input
function startVoice() {
    let recognition = new webkitSpeechRecognition();
    recognition.lang = "en-US";
    recognition.start();

    recognition.onresult = function(event) {
        let text = event.results[0][0].transcript;
        document.getElementById("user-input").value = text;
        sendMessage();
    };

    recognition.onerror = function() {
        alert("Voice recognition error");
    };
}