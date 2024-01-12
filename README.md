# FAST Timetable Viewer

This Streamlit web application allows users to view and download the timetable for various subjects at FAST (Foundation for Advancement of Science and Technology). The timetable data is fetched from an external API with the base URL [https://universe-timetable.vercel.app/](https://universe-timetable.vercel.app/).

## Usage

1. **Subject Selection:**
   - Upon opening the app, you will see a title indicating "FAST Timetable Viewer."
   - A list of all available subjects is fetched from the API, and a multi-select widget is provided for users to choose specific subjects.

2. **Fetching Time Table:**
   - Click the "Fetch Time Table" button to retrieve and display the timetable for the selected subjects.
   - If no subjects are selected, a warning message will be displayed, prompting the user to select at least one subject.

3. **Time Table Display:**
   - Once the timetable data is fetched, it is presented in a DataFrame format with styled headers for better readability.
   - The displayed columns include "Subject," "Room," "Day," "Start-Time," and "End-Time."

4. **Download Time Table as CSV:**
   - Below the timetable display, a button labeled "Download Timetable as CSV" is provided.
   - Clicking this button will initiate the download of the timetable data in CSV format.

5. **Credits:**
   - The app includes a credits section at the bottom, acknowledging the contributors to the application: Hassan Rasool, Umar Waseem, and Talal Muzaffar.

## Setup

To run this Streamlit app locally, make sure you have Python installed. Install the required dependencies using:

```bash
pip install streamlit requests pandas
```

After installing the dependencies, run the app using:

```bash
streamlit run <filename>.py
```

Replace `<filename>` with the name of the file containing the provided code.

## Dependencies

- [Streamlit](https://www.streamlit.io/): A Python library for creating web applications with minimal effort.
- [Requests](https://docs.python-requests.org/en/latest/): A Python library for making HTTP requests.
- [Pandas](https://pandas.pydata.org/): A data manipulation and analysis library for Python.

## Note

This application relies on an external API hosted at [https://universe-timetable.vercel.app/](https://universe-timetable.vercel.app/). Ensure a stable internet connection to fetch timetable data successfully.

**Disclaimer:** The timetable data is dependent on the external API, and any issues in data retrieval may be due to API-related problems.

Feel free to explore the timetable and enjoy using the FAST Timetable Viewer!
