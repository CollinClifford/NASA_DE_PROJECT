#### Updated 02/028/2024 Current version: 2

# NASA_DE_PROJECT: A data factoy using NASA Open API Web Services 
![Nasa Astronomy Picture of the Day Example](./media/apod.jpg)

The NASA_DE_PROJECT takes public information provided through a network of NASA's Open APIs and populates a local database that owners can use to perform data analysis, create visualizations, or practice data goverance/administrative exercises on.\
As this is largely a learning opportunity for the construction of Data Warehouses, historical data only spans back through 2024.  After this project is complete, historical data will be considered.

This project consists of the following components.
- Extraction (WIP)\
*used to make API calls and store raw data in Data Lake*
- Data Pipeline/Factory (WIP)\
*used to perfrom ETL process before loading to data warehouse*
- Data Warehouse (WIP)\
*stores relational tables/views in postgresql local server*
- Stored Procedures (WIP)\
*used to create processes for data maintainance and governance*

##### Summary

Currently, the program works in the following order:
1. Cycles through NASA Open API Web Services, updating JSON with missing data
2. Runs Data Pipeline to perform ETL processes
    - Drops dependent tables
    - Drops new tables in database
    - Drops schemas
    - Creates schemas
    - Creats new tables
    - Inserts raw data
    - Creates dependent tables

![NASA_proj workflow diagram](./media/NASA_proj_wf.jpg)  

## Components

- `./data_factory`
    - `./data_warehouse_init`
        - `./functions`
        - `./sql_commands`
- `./data_lake_storage`
- `./extraction_scripts`
    - `./functions`
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
    - Create Data Pipeline/Factory for above APIs.
- **Version 2**
    - Connect other APIS.
    - Create Data Pipeline/Factory for new APIs.
    
## Installation and Execution
*Note:*\
The user should have [python3](https://pypi.org/project/pip/) installed\
as well as have a clear understanding of [pip](https://pypi.org/project/pip/)\
and [postgresql](https://pypi.org/project/pip/).
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

please contact collinclifford@ymail.com for any inquiries about this program.

## Additional API Details (all information from the [NASA OPEN API](https://analytics.usa.gov/) website):
### APOD
One of the most popular websites at NASA is the [Astronomy Picture of the Day](http://apod.nasa.gov/apod/astropix.html). In fact, this website is one of the [most popular websites](https://analytics.usa.gov/) across all federal agencies. It has the popular appeal of a Justin Bieber video. This endpoint structures the APOD imagery and associated metadata so that it can be repurposed for other applications. In addition, if the `concept_tags` parameter is set to True, then keywords derived from the image explanation are returned. These keywords could be used as auto-generated hashtags for twitter or instagram feeds; but generally help with discoverability of relevant imagery.

The full documentation for this API can be found in the [APOD API Github repository](https://github.com/nasa/apod-api).
### Asteroids - NeoWs
NeoWs (Near Earth Object Web Service) is a RESTful web service for near earth Asteroid information. With NeoWs a user can: search for Asteroids based on their closest approach date to Earth, lookup a specific Asteroid with its NASA JPL small body id, as well as browse the overall data-set.

Data-set: All the data is from the NASA JPL Asteroid team (http://neo.jpl.nasa.gov/).

This API is maintained by [SpaceRocks Team: David Greenfield, Arezu Sarvestani, Jason English and Peter Baunach](https://github.com/SpaceRocks/).
### DONKI
The [Space Weather Database Of Notifications, Knowledge, Information (DONKI)](https://ccmc.gsfc.nasa.gov/tools/DONKI/) is a comprehensive on-line tool for space weather forecasters, scientists, and the general space science community. DONKI chronicles the daily interpretations of space weather observations, analysis, models, forecasts, and notifications provided by the Space Weather Research Center (SWRC), comprehensive knowledge-base search functionality to support anomaly resolution and space science research, intelligent linkages, relationships, cause-and-effects between space weather activities and comprehensive webservice API access to information stored in DONKI.

This API consists of the following component services:
### EARTH
Landsat imagery is provided to the public as a joint project between NASA and USGS. A recent industry [report](http://www.fgdc.gov/ngac/meetings/december-2014/ngac-landsat-economic-value-paper-2014-update.pdf) on landsat satellite imagery data estimates that total annual value to the economy of $2.19 billion, far exceeding the multi-year total cost of building, launching, and managing Landsat satellites and sensors. The value is derived from consumers use of the data. The objective of this endpoint is to give you an easy to use taste of what Landsat imagery data can provide. There are more complicated APIs available if you want to build models on top of satellite imagery, apply machine-learning, or minimize clouds in your image. NASA's Earth Science Devision has a variety of Earth imagery APIs for developers, which you can find out about in the [Earthdata Developer Portal](https://earthdata.nasa.gov/collaborate/open-data-services-and-software/api). Specifically, the GIBS (Global Imagery Browse Services) API may be of interest. The [Google Earth Engine API](https://earthengine.google.com/) is another powerful option. This API is powered by Google Earth Engine API, and currently only supports pan-sharpened Landsat 8 imagery.