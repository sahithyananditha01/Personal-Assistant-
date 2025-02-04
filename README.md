# Personal-Assistant- Nitu


Nitu is a Python-based personal assistant that leverages voice commands to perform various tasks,

	1.Asking date and time
	2.Taking notes
	3.Capturing screenshots
	4.Opening web browsers
	5.Playing music via Spotify
	6.Providing weather updates

Features

	•	Voice Recognition: Utilizes the speech_recognition library to process voice commands.
	•	Text-to-Speech Response: Employs gTTS for generating spoken responses.
	•	Spotify Integration: Controls music playback through the Spotify Web API using spotipy.
	•	Weather Updates: Fetches current weather information for Newark using the OpenWeatherMap API.
	•	Task Management: Allows users to add and list tasks through voice commands.
	•	Screenshot Capture: Takes screenshots using pyautogui.
	•	Web Browsing: Opens Google Chrome via voice command.

Installation

1.	Clone the Repository:

		git clone https://github.com/YourUsername/Nitu-Assistant.git
		cd Nitu-Assistant


2.	Set Up a Virtual Environment (Optional but recommended):

		python3 -m venv venv
		source venv/bin/activate  # On Windows, use venv\Scripts\activate


3.	Install Dependencies:
   
   		pip install -r requirements.txt


5.	API Credentials:
   
	•	Spotify:
	•	Create a Spotify Developer account and set up an application to obtain your CLIENT_ID, CLIENT_SECRET, and REDIRECT_URI.
	•	Ensure your redirect URI matches the one registered in your Spotify Developer Dashboard.
	•	OpenWeatherMap:
	•	Sign up at OpenWeatherMap to get your API key.
	•	Configuration:
	•	Replace the placeholder values in the script with your actual API credentials.

Usage
1.	Run the Application:

		python.py


2.	Interact with Nitu:

	•	Say “candy” followed by your command. For example:
	•	“Candy, play music.”
	•	“Candy, what’s the weather?”
	•	“Candy, take a screenshot.”

Dependencies

	•	speech_recognition
	•	gtts
	•	requests
	•	pyautogui
	•	webbrowser
	•	spotipy

Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements or bug fixes.
