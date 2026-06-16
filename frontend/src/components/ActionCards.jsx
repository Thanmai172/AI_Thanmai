function ActionCards({ startChat }) {
  return (
    <div className="action-cards">

      <div
        className="action-card"
        onClick={startChat}
      >
        💬 Chat With AI
      </div>

      <div className="action-card">
        🚀 Create React App
      </div>

      <div className="action-card">
        🐍 Learn Python
      </div>

      <div className="action-card">
        🤖 Build AI Agent
      </div>

      <div className="action-card">
        🛠 Debug My Code
      </div>

    </div>
  );
}

export default ActionCards;
