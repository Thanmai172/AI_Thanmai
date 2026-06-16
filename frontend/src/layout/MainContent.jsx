import WelcomeScreen from "../components/WelcomeScreen";
import ActionCards from "../components/ActionCards";
import ChatWindow from "../components/ChatWindow";
import InputBox from "../components/InputBox";

function MainContent({
  showChat,
  startChat,
  messages,
  message,
  setMessage,
  sendMessage
}) {

  if (showChat) {
    return (
      <div className="main-content">

        <ChatWindow
          messages={messages}
        />

        <InputBox
          message={message}
          setMessage={setMessage}
          sendMessage={sendMessage}
        />

      </div>
    );
  }

  return (
    <div className="main-content">

      <WelcomeScreen />

      <ActionCards
        startChat={startChat}
      />

    </div>
  );
}

export default MainContent;