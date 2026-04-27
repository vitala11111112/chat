const socket = io("localhost:8081", {transports: ['websocket']});
const input = document.getElementById("input");
const sendButton = document.getElementById("send");
const messagesContainer = document.querySelector(".messages");

function sendMessages() {
    const text = input.value.trim();

    if (text !== "") {
        socket.emit("chat_message", text);
        input.value = "";
        console.log("123")
    }
}

sendButton.addEventListener("click", sendMessages);

socket.on("chat_message", function (msg) {
    const messageDiv = document.createElement("div");
    messageDiv.textContent = msg;
    messagesContainer.appendChild(messageDiv);
});