# ProjectKeyLogger

## Overview
ProjectKeyLogger is a comprehensive key logging solution that captures keyboard input, encrypts the data, and provides both client and server-side components for data management. The system includes a key logger service, encryption module, data management tools, and a web interface for viewing the collected data.

## Project Structure
```
ProjectKeyLogger/
├── ProjectKeyLogger/
│   ├── encryption/
│   │   ├── encryption_interface.py
│   │   └── shaul_encryption.py
│   ├── key_logger_service/
│   │   ├── i_key_logger_service.py
│   │   └── key_Logger_service.py
│   ├── manager/
│   │   └── key_logger_manager.py
│   ├── writer/
│   │   ├── json_writer.py
│   │   ├── network_writer.py
│   │   └── yaml_writer.py
│   ├── decrypt_script.py
│   └── main.py
├── server_side/
│   ├── fastapi_server/
│   │   ├── base_models/
│   │   │   └── data_insert_model.py
│   │   ├── database/
│   │   │   ├── db_connect.py
│   │   │   ├── logs.py
│   │   │   └── users.py
│   │   └── routers/
│   │       ├── data.py
│   │       └── utils.py
│   ├── flask_server/
│   │   ├── templates/
│   │   │   ├── dashboard.html
│   │   │   ├── home-page.html
│   │   │   └── login.html
│   │   └── app.py
│   └── requirements.txt
└── README.md
```

## Features

### Client Side
- **Key Logger Service**: Captures keystrokes from user input
- **Window Tracking**: Records which application window was active during keystroke capture
- **Encryption**: Secures captured data with custom encryption algorithms
- **Multiple Output Formats**: Supports JSON, YAML, and network data transmission

### Server Side
- **FastAPI REST API**: Receives and stores encrypted keystroke data
- **MongoDB Integration**: Stores data in a structured format
- **Flask Web Interface**: Provides a user-friendly dashboard to view and analyze collected data
- **Authentication**: Secures access to the dashboard with password protection

## Installation

### Prerequisites
- Python 3.8+
- MongoDB
- Virtual environment tool (recommended)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ProjectKeyLogger.git
cd ProjectKeyLogger
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r server_side/requirements.txt
```

4. Configure environment variables:
```bash
export API_URL="http://localhost:8000"  # For the client side
```

## Usage

### Running the Key Logger Client

1. Start the key logger service:
```bash
cd ProjectKeyLogger
python main.py
```

2. The logger will begin capturing keystrokes and either save them locally or transmit them to the server based on the configured writer.

### Running the Server Components

1. Start the FastAPI server:
```bash
cd server_side/fastapi_server
uvicorn main:app --reload --port 8000
```

2. Start the Flask web interface:
```bash
cd server_side/flask_server
flask run --port 5000
```

3. Access the web dashboard at http://localhost:5000

4. Login with the password: `KLPpassword`

## Security Considerations

This project is intended for educational purposes and authorized monitoring only. Unauthorized use to record keystrokes without consent may violate privacy laws and regulations.

Recommended security practices:
- Always obtain proper authorization before deploying
- Use strong encryption keys
- Change default passwords
- Implement proper access controls

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- [pynput](https://pypi.org/project/pynput/) for keyboard input capture
- [FastAPI](https://fastapi.tiangolo.com/) for the API server
- [Flask](https://flask.palletsprojects.com/) for the web interface
- [MongoDB](https://www.mongodb.com/) for data storage

Similar code found with 2 license types] for keyboard input capture
- FastAPI for the API server
- Flask for the web interface
- MongoDB for data storage
