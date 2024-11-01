# AI-Interactive-Dashboard

## Project Overview

The AI-Interactive-Dashboard is a powerful and engaging web application that leverages AI and interactive visualizations to provide users with real-time data insights. The dashboard includes features such as user authentication, role-based access control, and real-time data updates using Flask-SocketIO.

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/akaday/AI-Interactive-Dashboard.git
   cd AI-Interactive-Dashboard
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python app.py
   ```

## Usage

### User Authentication and Registration

The dashboard includes user authentication and registration functionality. Users can register with their email and password, and then log in to access the dashboard. The application uses Flask-Login to manage user sessions.

### User Preferences and Role-Based Access Control

Users can customize their dashboard experience by setting preferences such as theme (light or dark). The application also implements role-based access control to restrict certain features to specific user groups.

### Real-Time Data Updates

The dashboard uses Flask-SocketIO to provide real-time data updates. Users can receive live data feeds and notifications for significant data changes.

### Interactive Visualizations

The dashboard integrates Plotly to create dynamic and interactive charts and graphs. Users can filter, sort, zoom, and pan on the charts for better data exploration.

## Contributing

We welcome contributions to enhance the AI-Interactive-Dashboard. Please fork the repository and submit pull requests for any improvements or new features.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
