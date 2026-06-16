Backend

--> if we need to go to the Virtual Environment please go to backend and Run this Command: 
venv\Scripts\activate

--> To get the Packages we need this command :
pip install fastapi uvicorn google-generativeai python-dotenv


--> To Run the Application use this command : 
uvicorn main:app --reload

--> after Running the Application Run Command use this one to verify  :
http://127.0.0.1:8000/

-->  after Running the Application Run Command use this one to verify  :
http://127.0.0.1:8000/docs#/

Frontend

cd frontend
npm create vite@latest . -- --template react
npm install
npm install axios

To add the Icons :
npm install react-icons


To run the Application in the frontend
npm run dev