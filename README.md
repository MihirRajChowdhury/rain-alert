# Rain Alert System
![DALL·E 2025-03-02 11 32 07 - A minimalist and modern image with a smooth gradient sky background transitioning from clear blue ( 87CEEB) at the top to stormy gray ( 4B5E6D) at the](https://github.com/user-attachments/assets/d13f04c3-18eb-4611-8991-037eff188300)

## Overview
The Rain Alert System is a Python-based project that checks the weather forecast for the next 12 hours using the OpenWeatherMap API. If rain is predicted, it sends an SMS notification to predefined phone numbers, reminding the recipients to carry an umbrella. This project is deployed on PythonAnywhere and runs daily at 9 AM to provide timely weather updates.

## Features
Fetches real-time weather data using the OpenWeatherMap API.
Predicts rain within the next 12 hours for a specified location.
Sends SMS notifications to listed phone numbers if rain is expected.
Automated daily execution at 9 AM via PythonAnywhere.
## How It Works
The script queries the OpenWeatherMap API for the weather forecast of a predefined location.
It analyzes the forecast data for the next 12 hours to detect any chance of rain.
If rain is predicted, it uses an SMS service (e.g., Twilio or similar) to send a message like:
"Rain expected today! Don’t forget to carry an umbrella."
The script runs automatically every day at 9 AM on PythonAnywhere.
## Technologies Used
* Python: Core programming language for the script.
* OpenWeatherMap API: Provides weather forecast data.
* SMS Service: Sends text message notifications (e.g., Twilio, specify if applicable).
* PythonAnywhere: Hosts and schedules the script to run daily.
## Setup Instructions
### Prerequisites
* Python 3.x installed.
* An OpenWeatherMap API key (sign up at OpenWeatherMap to get one).
* An SMS service account (e.g., Twilio) with API credentials.
* A PythonAnywhere account for deployment (optional).
### Installation
1. Clone the repository:
```bash
git clone https://github.com/your-username/rain-alert-system.git
cd rain-alert-system
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Set up environment variables:
Create a .env file in the root directory.
Add the following:
```bash
OPENWEATHERMAP_API_KEY=your_openweathermap_api_key
SMS_API_KEY=your_sms_service_api_key
SMS_API_SECRET=your_sms_service_secret
PHONE_NUMBERS=comma_separated_list_of_numbers
LOCATION=your_city_name
```
4. Run the script locally to test:
```bash
python rain_alert.py
```
## Deployment on PythonAnywhere
1. Upload the project files to your PythonAnywhere account.
2. Set up the environment variables in the PythonAnywhere dashboard.
3. Schedule the script to run daily at 9 AM using the "Tasks" feature.
## Configuration
* Phone Numbers: Edit the PHONE_NUMBERS variable in the .env file to include the numbers you want to notify (e.g., +1234567890,+0987654321).
* Location: Update the LOCATION variable with your city name or coordinates.
* Message: Customize the SMS message in the script if needed.
## Usage
* Run the script manually to test: python rain_alert.py.
* Once deployed on PythonAnywhere, it will automatically check the weather and send notifications at 9 AM daily.
## Future Improvements
* Add support for multiple locations.
* Include more detailed weather information in the SMS.
* Allow users to subscribe/unsubscribe via text messages.
## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For questions or suggestions, feel free to open an issue or contact me at [rajmihir945@gmail.com].
