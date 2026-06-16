import MessageBubble from "./MessageBubble";

function ChatWindow({ messages }) {
  return (
    <div className="chat-window">

      {messages.map((msg, index) => (
        <div
          key={index}
          className={
            msg.role === "user"
              ? "message user-message"
              : "message ai-message"
          }
        >
          {msg.content}
        </div>
      ))}

    </div>
  );
}

export default ChatWindow;