window.sendQuery = async function () {

    const input = document.getElementById("userInput");
    const chatContainer = document.querySelector(".chat-box");

    const query = input.value.trim();

    if (!query) return;

    // =========================
    // USER MESSAGE
    // =========================

    const userMessage = document.createElement("div");

    userMessage.className = "message user-message";

    userMessage.innerHTML = `
        <p>${query}</p>
    `;

    chatContainer.appendChild(userMessage);

    // Auto scroll
    chatContainer.scrollTop = chatContainer.scrollHeight;

    input.value = "";

    try {
        // Loading message

const loadingMessage = document.createElement("div");

loadingMessage.className = "message bot-message loading";

loadingMessage.innerHTML = `
    <div class="typing">
        <span></span>
        <span></span>
        <span></span>
    </div>
`;

chatContainer.appendChild(loadingMessage);

chatContainer.scrollTop = chatContainer.scrollHeight;

        const response = await fetch("http://127.0.0.1:8001/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                query: query
            })

        });

        const data = await response.json();
        console.log(data);
        // Remove loading animation

loadingMessage.remove();

        // =========================
// BOT MESSAGE
// =========================

const botMessage = document.createElement("div");

botMessage.className = "message bot-message";

// FORMAT RESPONSE
const formattedResponse = data.response
    .replace(/\d+\./g, "<br><br>$&")
    .replace(/- /g, "<br>• ");

// BOT HTML
botMessage.innerHTML = `

    <div class="bot-card">

        <p>
            <strong>Status:</strong> 
            ${data.status.toUpperCase()}
        </p>

        <p>
            <strong>Priority:</strong> 
            ${data.priority.toUpperCase()}
        </p>

        <br>

        <p class="response-text">
            ${formattedResponse}
        </p>

    </div>

`;

chatContainer.appendChild(botMessage);

        // Auto scroll
        chatContainer.scrollTop = chatContainer.scrollHeight;

    } catch (error) {

        console.error(error);

        const errorMessage = document.createElement("div");

        errorMessage.className = "message bot-message";

        errorMessage.innerHTML = `
            <div class="bot-card error-card">
                <p>⚠️ Server Error. Please try again.</p>
            </div>
        `;

        chatContainer.appendChild(errorMessage);

        // Auto scroll
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }
};