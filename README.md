# Delta State Election Results Web Application

This is a simple Flask web application designed to display and manage election results for polling units in Delta State. The application allows users to view individual polling unit results, calculate and display the total results for any local government, and store results for new polling units.

## Features

1. **View Individual Polling Unit Results**:
   - Users can select a specific polling unit and view the election results for each party.
   - Data is retrieved from the `announced_pu_results` table in the database.

2. **Display Total Results for a Local Government**:
   - Users can select a local government from a dropdown menu and see the total election results for all polling units in that local government.
   - The total results are calculated by aggregating the data from the `announced_pu_results` table.

3. **Store Results for New Polling Units**:
   - There is a dedicated page for storing election results for new polling units.
   - Users can input the results for all parties, and the data is stored in the database.

## Prerequisites

- Python 3.x
- Flask
- SQLAlchemy (for the provided database)
- Web browser

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/delta-election-results.git
   cd delta-election-results
   ```

2. Run the Flask application:

   ```bash
   ./main.py
   ```

4. Open a web browser and go to `http://localhost:5000` to access the application.

## Usage

- Use the web application to view individual polling unit results, calculate total results for local governments, and store results for new polling units.
- The application provides a user-friendly interface with dropdowns and forms for easy interaction.

## Database

- The provided [SQLAlchemy database](https://drive.google.com/file/d/0B77xAtHK1hd4Ukx6SHpqTkd6TWM/view) is named `bincom_test.db` and contains tables for polling units, wards, LGAs, and election results.

## Author

- Vivian Dagbue
- Contact: vdagbue@gmail.com

