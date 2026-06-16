import { useState } from "react";
import axios from "axios";

import Sidebar from "../layout/Sidebar";
import MainContent from "../layout/MainContent";
import InsightsPanel from "../layout/InsightsPanel";

function Home() {

  const [showChat, setShowChat] = useState(false);

  const [message, setMessage] = useState("");

  const [messages, setMessages] = useState([
    {
      role: "assistant",
      content: "Hello Thanmai 👋"
    }
  ]);

  const startChat = () => {
    setShowChat(true);
  };

  const sendMessage = async () => {

    if (!message.trim()) return;

    const userMessage = {
      role: "user",
      content: message
    };

    setMessages(prev => [
      ...prev,
      userMessage
    ]);

    const currentMessage = message;

    setMessage("");

    try {

      const response = await axios.post(
        "http://127.0.0.1:8000/chat",
        {
          message: currentMessage
        }
      );

      const aiMessage = {
        role: "assistant",
        content: response.data.reply
      };

      setMessages(prev => [
        ...prev,
        aiMessage
      ]);

    } catch (error) {

      setMessages(prev => [
        ...prev,
        {
          role: "assistant",
          content: "Something went wrong."
        }
      ]);

    }
  };

  return (
    <div className="app-layout">

      <Sidebar />

      <MainContent
        showChat={showChat}
        startChat={startChat}
        messages={messages}
        message={message}
        setMessage={setMessage}
        sendMessage={sendMessage}
      />

      <InsightsPanel />

    </div>
  );
}

export default Home;