# Chatbot 

JobSeekers is a chatbot designed to serve as a part-time shift booking system for aspiring students who want to earn and learn as they go.

## Repository Contents

1. `Chatbot.py`: Python script for the chatbot functionality.
2. `ChatbotDatabase.db`: SQLite database file for storing chatbot data.
3. `intents.json`: JSON file containing intents for the chatbot.
4. `JobSeekersDatabase.db`: SQLite database file for job seeker data.

## Prerequisites

To run the code in this repository, you'll need to have the following software/packages installed:

- Python version 3.11

Additionally, you'll need the following Python libraries:
- numpy
- pandas
- sqlite3
- json
- sklearn
- scipy

## Installation

1. Install the required Python packages using `pip`:

    ```bash
    pip install numpy pandas sqlite3 json sklearn scipy
    ```

## Getting Started

Follow these steps to set up the chatbot:

1. **Step 1:** In the `Chatbot.py` file, update the path of the `intents.json` file in line 19 according to the location where you have stored it.
2. **Step 2:** If any database error arises, please run the `JobSeekersDatabase.py` file.
3. **Step 3:** Ensure that `ChatbotDatabase.db` is present in your folder where you have stored all the chatbot files.
