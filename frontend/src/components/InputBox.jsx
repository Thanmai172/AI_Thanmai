import { IoSend } from "react-icons/io5";

function InputBox({
  message,
  setMessage,
  sendMessage
}) {
  return (
    <div className="input-container">

      <input
        type="text"
        placeholder="Ask Thanmai anything..."
        value={message}
        onChange={(e) =>
          setMessage(e.target.value)
        }
      />

      <button onClick={sendMessage}>
        <IoSend />
      </button>

    </div>
  );
}

export default InputBox;