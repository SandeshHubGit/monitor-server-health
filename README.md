# Monitor Server Health

## Project Description

  This Python script monitors server CPU usage in real-time and alerts when it exceeds a predefined threshold.

## Table of Contents

  1. Prerequisites
  2. Installation Instructions
  3. Usage Instructions
  4. Configuration
  5. Security Best Practices
  6. Troubleshooting
  7. Contribution Guidelines

## Prerequisites

  1. Python 3.x installed on your system.
  2. psutil library installed (pip install psutil).

## Installation Instructions

  1. Clone this repository:
     ``` git clone https://github.com/yourusername/monitor-server-health.git ```
  2. Navigate to the project directory:
     ``` cd monitor-server-health ```
  3. Install required dependencies:
     ``` pip install psutil ```

## Usage Instructions
  Run the script to monitor CPU usage:
  ``` python monitor_server_health.py ```

  The script:
  1. Monitors CPU usage every second.
  2. Prints current CPU usage.
  3. Raises an alert if CPU usage exceeds the set threshold (default: 80%).

## Configuration
  Modify the threshold value in monitor_server_health.py:
  ``` CPU_THRESHOLD = 80%  # Change this to your desired threshold ```

## Security Best Practices
  1. Run the script in a restricted environment to avoid unwanted modifications.
  2. Ensure Python and dependencies are up to date.
  3. Use logging instead of print statements for better monitoring.

## Troubleshooting
  1. Error: ModuleNotFoundError: No module named 'psutil'
   Install psutil using:
    ``` pip install psutil ```

  2. CPU usage not updating?
    Ensure the system has sufficient CPU activity.

## Contribution
  Contributions are welcome! Feel free to fork the repository and submit pull requests with improvements or bug fixes.

## Output
  For example, We set CPU_THRESHOLD = 20%

![image](https://github.com/user-attachments/assets/cdade9c6-27f4-432c-956f-39254a9c86f7)
