# Automatic File Backup 
_A Python-based tool to fetch and analyze live NBA team scores and season statistics using the NBA Data API. This project aims to help users gain real-time insights into current games and top-performing teams._

## Table of Contents
<pre>
-<a href="#overview">Overview</a>
-<a href="#problem">Problem</a>
-<a href="#tools">Tools</a>
-<a href="#project-structure">Project Structure</a>
-<a href="#key-things">Key Things</a>
-<a href="#how-to-run-this-program">How to run this program</a>
-<a href="#recommendations">Recommendations</a>
-<a href="#builder-contact">Builder Contact</a>
</pre>

<h2><a class="anchor" id="overview"></a>Overview</h2>
This Python program leverages the NBA's public data API to provide real-time analysis of team performance and ongoing matches. It includes functionality to:<br><br>

- View the current scoreboard (live games with team scores, time remaining, and period).<br>
- Get season statistics of NBA teams, sorted by points per game (PPG).<br>
- Filter out irrelevant or placeholder data to ensure clean output.<br>

<h2><a class="anchor" id="problem"></a>Problem</h2>
Building an NBA stats analyzer requires tackling several technical and data-handling challenges:<br><br>

- Parsing nested JSON responses from the NBA API.<br>
- Dynamically fetching the current scoreboard and stats endpoints.<br>
- Handling potential API structure changes (like renamed keys or new nesting).<br>
- Cleaning and validating data (e.g., filtering placeholder "Team" entries).<br>
- Sorting and displaying team stats in a user-friendly format.<br>

<h2><a class="anchor" id="tools"></a>Tools</h2>
The project uses basic but powerful Python libraries to achieve its functionality:<br>

- requests: To fetch JSON data from the NBA API.<br>
- pprint (PrettyPrinter): For clean, structured printing of JSON and dictionaries.<br>
- Lambda functions and sorting: To filter and rank team stats.<br>
- Standard Python I/O and control structures.<br>

No external libraries beyond the Python standard library are required.<br>

<h2><a class="anchor" id="projec-structure"></a>Project Structure</h2>
<pre>Mastermind/
│
├── main.py               # Main Python script to run the program
├── README.md             # Project documentation
</pre>

<h2><a class="anchor" id="key-things"></a>Key Things</h2>

### Real-Time Scoreboard**<br>

- Pulls data from the NBA’s live scoreboard endpoint.<br>
- Displays each game’s teams, scores, current period, and remaining time.<br>

### Season Stats<br>
- Fetches team stats for the regular season.<br>
- Filters out invalid team names (e.g., placeholder “Team” entries).<br>
- Ranks teams by average points per game (PPG), from highest to lowest.<br>

### Clean Data Handling<br>
- Uses JSON parsing and lambda-based filtering to ensure clean output.<br>
- Dynamically uses live API links provided by NBA's base endpoint.<br>
<br>
<h2><a class="anchor" id="how-to-run-this-program"></a>How to run this program</h2>

### Prerequisites<br>
- Install Python (preferably Python 3.x): https://www.python.org/downloads/<br>
- Ready right API from trusted sources for updated data and the APi should work properly.

### Clone or Download the Project<br>
- You can clone it using Git or simply download the .py file.<br>
- git clone https://github.com/yourusername/NBA-stats-analyzer-python.git<br>
- Change directory to where you cloned the file in local directory<br>

### Run the Program<br>
- Use your terminal or command prompt:<br>
- run the file<br>

### Output<br>
- You will see a list of currently active NBA games with live scores.<br>
- Followed by a ranked list of NBA teams sorted by points per game (PPG).<br>

<h2><a class="anchor" id="recommendations"></a>Recommendations</h2>
Here are some tips and ideas for improving or modifying the program:<br>

### For Future Enhancements:<br>

- Add player-level stats (top scorers, assists, rebounds).<br>
- GUI: Create a simple interface using tkinter or streamlit.<br>
- Scheduled Updates: Auto-refresh scoreboard every 30 seconds.<br>
- Export Options: Save stats to .csv or .json for further analysis.<br>
- Add Unit Tests: Ensure key functions work with mock JSON.<br>
- Error Handling: Gracefully handle connection issues or malformed data.<br>

<h2><a class="anchor" id="builder-contact"></a>Builder Contact</h2>

**Shreshth Adlakha**<br>
Python Developer<br>
shreshthaadlakha@gmail.com <br>
[LinkedIn](https://www.linkedin.com/in/shreshthadlakha/)
