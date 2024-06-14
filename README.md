# Route Map App

Route Map App is a desktop application built with Python and PyQt5, featuring an embedded Leaflet web map. Users can add and save route points by clicking on the map.

This project was developed as a part of another application.

## Features

- Interactive map by Leaflet, displayed inside a QWebEngineView.
- Add markers by clicking on the map; coordinates are sent to a Flask server.
- Sidebar list displays added points with their index and coordinates.

## Installation and running

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/RouteMapApp.git
   cd RouteMapApp
   ```

2. Create and activate virtual environment (Optional)

    ```bash
    virtualenv <venv_name>
    source <venv_name>/bin/activate # Linux
    <venv_name>\Scripts\activate.bat # Windows
    ```

3. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

4. Run the app

    Start the server (default at http://127.0.0.1:5000):
    ```bash
    python server.py 
    ```

    Start the Qt app:
    ```bash
    python main.py 
    ```