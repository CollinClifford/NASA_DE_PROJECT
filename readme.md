#### Updated 02/08/2024 Current version: 1.2

# NASA_DE_PROJECT: A data factoy using NASA Open API Web Services 
![Nasa Astronomy Picture of the Day Example](./media/apod.jpg)

This project consists of several components.
- Data Lake (WIP)\
*raw data files are stored*
- Extraction Scripts (WIP)\
*used to make API calls and store raw data in Data Lake*
- Data Pipeline/Factory (WIP)\
*used to perfrom ETL process before loading to data warehouse*
- Data Warehouse (WIP)\
*stores relational tables in postgresql local server*
- Stored Procedures (WIP)\
*will be used to create processes for data maintainance and governance*

##### Summary

This program is stored on a Raspbery Pi server and runs at midnight daily.  It runs in the following order.
1. Cycles through NASA Open API Web Services updating JSON with missing data
2. Runs Data Pipeline to perform ETL processes
    - Drops/Creates new tables in database
    - Inserts raw data

![NASA_proj workflow diagram](./media/NASA_proj_wf.jpg)

As this is largely a learning opportunity for the construction of Data Warehouses, historical data only spans back through 2024.  After this project is complete, historical data will be considered.  

## Components

- `./data_factory`
- `./data_lake_storage`
- `./extraction_scripts`
- `./logs`
- `./media`
- `.env`
- `.gitignore`
- `./main.py`
- `./readme.md`
- `./requirements.txt`

## Packages Used
- requests
- psycopg2-binary
- python-dotenv

## Release Plan
- **Version 1.1**
    - Create first draft.
    - Connect to APOD, NeoWS, DONKI APIs.
    - Create Data Pipeline/Factory for APOD, NeoWs.
- **Version 1.2**
    - Connected to EARTH, EPIC, Mars_Rover_Photos APIs.
    - Create Data Pipeline/Factory for DONKI

## Installation and Execution
*Note:* This project uses python3.
1. **Clone Repository:**
    ```bash
    git clone https://github.com/CollinClifford/NASA_DE_PROJECT
    cd NASA_DE_PROJECT
2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
3. **Configure Environment Variables:**
    Create a `.env` file in the project root with the necessary environment variables with the following as a template.
    ```bash
    # API Key

    API_KEY=

    # Database connections
    DB_HOST=
    DB_NAME=
    DB_USER=
    DB_PASSWORD=
    DB_PORT=
    SSL_MODE=disable
4. **Set up logs folder**\
    Create this folder path:
    ```bash
    mkdir logs
    cd logs
    touch main.log
5. **Run the Program:**\
    Execute the bash script:
    ```bash
    python3 ./main.py
