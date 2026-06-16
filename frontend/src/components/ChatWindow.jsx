import MessageBubble from "./MessageBubble";

function ChatWindow({ messages }) {
  return (
    <div
      className={`chat-window ${
        messages.length < 4
          ? "chat-center"
          : ""
      }`}
    >
      {messages.map((msg, index) => (
        <MessageBubble
          key={index}
          role={msg.role}
          content={msg.content}
        />
      ))}
    </div>
  );
}

export default ChatWindow;