const socket = io("localhosy:8080",{transports: ["websocket"]});
socket.on('connect', ()=> {
    console.log("connected")
    socket.emit("char_message", "test")
})
socket.on("chat_response", (data) => {
    console.log(data)
})