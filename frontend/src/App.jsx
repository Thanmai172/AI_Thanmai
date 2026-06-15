import { useState } from "react";
import axios from "axios";

function App() {
  const [message, setMessage] = useState("");
  const [reply, setReply] = useState("");

  const sendMessage = async () => {
    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/chat",
        {
          message: message
        }
      );

      setReply(response.data.reply);
    } catch (error) {

       if (error.response) {
         setReply(error.response.data.detail);
  }    else {
          setReply("Unable to connect to server");
  }

  console.error(error);
}
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Thanmai AI Assistant</h1>

      <input
        type="text"
        placeholder="Ask anything..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        style={{
          width: "300px",
          padding: "10px"
        }}
      />

      <button
        onClick={sendMessage}
        style={{
          marginLeft: "10px",
          padding: "10px"
        }}
      >
        Ask AI
      </button>

      <hr />

      <h3>Response</h3>

      <p>{reply}</p>
    </div>
  );
}

export default App;