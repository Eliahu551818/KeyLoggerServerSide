# ProjectKeyLogger

## Overview
ProjectKeyLogger is a comprehensive key logging service that captures and logs keystrokes, encrypts the data, and provides a server-side API to manage and retrieve the logged data. The project is divided into several components, including the key logger service, encryption, data management, and server-side API.

## Project Structure

ProjectKeyLogger/
├── server_side/
│   ├── fastapi_server/
│   │   ├── routers/
│   │   │   ├── users.py
│   │   │   ├── data.py
│   │   │   ├── utils.py
│   │   ├── database/
│   │   │   ├── db_connect.py
│   │   │   ├── logs.py
│   │   │   ├── users.py
│   │   ├── base_models/
│   │   │   ├── data_insert_model.py
│   │   ├── main.py
│   ├── decrypt_script.py
│   ├── main.py
│   ├── README.md

## Key Components

### Key Logger Service
The key logger service captures keystrokes and stores them in memory. It includes methods to start and stop the logging service and retrieve the logged data.

- [`KeyLoggerService`](ProjectKeyLogger/key_logger_service/key_logger_service.py)
- [`IKeyLoggerService`](ProjectKeyLogger/key_logger_service/i_key_logger_service.py)

### Encryption
The encryption module provides functionality to encrypt and decrypt the logged data.

- [`Encryption`](ProjectKeyLogger/encryption/shaul_encryption.py)
- [`IEncryptor`](ProjectKeyLogger/encryption/encryption_interface.py)

### Data Management
The manager module handles the orchestration of the key logger service, including starting, stopping, and managing the logged data.

- [`KeyLoggerManager`](ProjectKeyLogger/manager/key_logger_manager.py)

### Writers
The writer module provides different implementations to write the logged data to various formats such as JSON, YAML, and network.

- [`JsonWriter`](ProjectKeyLogger/writer/json_writer.py)
- [`YamlWriter`](ProjectKeyLogger/writer/yaml_writer.py)
- [`NetworkWriter`](ProjectKeyLogger/writer/network_writer.py)

### Server-Side API
The server-side API is built using FastAPI and provides endpoints to manage and retrieve the logged data.

- [`main.py`](server_side/fastapi_server/main.py)
- [`users.py`](server_side/fastapi_server/routers/users.py)
- [`data.py`](server_side/fastapi_server/routers/data.py)
- [`utils.py`](server_side/fastapi_server/routers/utils.py)
- [`db_connect.py`](server_side/fastapi_server/database/db_connect.py)
- [`logs.py`](server_side/fastapi_server/database/logs.py)
- [`users.py`](server_side/fastapi_server/database/users.py)

## Getting Started

### Prerequisites
- Python 3.8+
- MongoDB

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/ProjectKeyLogger.git
    cd ProjectKeyLogger
    ```

2. Install the required dependencies:
    ```sh
    pip install -r server_side/requirements.txt
    ```

3. Set up the environment variables:
    ```sh
    cp server_side/fastapi_server/.env.example server_side/fastapi_server/.env
    ```

4. Update the `.env` file with your MongoDB URI.

### Running the Key Logger Service
