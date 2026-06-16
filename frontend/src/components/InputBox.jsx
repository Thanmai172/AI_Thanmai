import { IoSend } from "react-icons/io5";

function InputBox({
  message,
  setMessage,
  sendMessage
}) {
  return (
    <div className="input-box">

      <input
        type="text"
        placeholder="Type your message..."
        value={message}
        onChange={(e) =>
          setMessage(e.target.value)
        }
      />

     <button onClick={sendMessage}>
        <IoSend size={22} />
    </button>

    </div>
  );
}

export default InputBox;