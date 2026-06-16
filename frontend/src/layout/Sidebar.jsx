import { FaRobot } from "react-icons/fa";

function Sidebar() {
  return (
    <div className="sidebar">

      <div className="sidebar-logo">
        <FaRobot />
        <span>Thanmai AI</span>
      </div>

    <button
      className="new-chat-btn"
      onClick={() => window.location.reload()}
    >
      + New Chat
    </button>

      <div className="sidebar-section">

        <h4>Recent Chats</h4>

        <div className="chat-item">
          React Project
        </div>

        <div className="chat-item">
          Python Notes
        </div>

        <div className="chat-item">
          AI Agent
        </div>

      </div>

      <div className="sidebar-footer">
        Settings
      </div>

    </div>
  );
}

export default Sidebar;