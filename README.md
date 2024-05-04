# Traffic Data warehouse

This repository contains code and configurations for building an Extract-Load-Transform (ELT) pipeline using Apache Airflow and dbt. The ELT pipeline aims to facilitate the transformation and loading of vehicle trajectory data collected from swarm UAVs (drones) into a scalable data warehouse for further analysis.

## Business Need
Our startup, specializing in AI and data intelligence solutions, has partnered with a city traffic department to analyze traffic data using swarm UAVs. The goal is to improve traffic flow and support various city projects by collecting, transforming, and analyzing vehicle trajectory data.

## Repository structure

```
.
├── airflow                 <--- Airflow related code.
│  ├── dags                 <--- DAGs executed by airflow.
│  └── docker-compose.yml   <--- Docker compose file to run the airflow
├── dbt_traffic             <--- Data built tools.
│  |── models               <--- Various models to transform the data
│  └── tests                <--- Great expectation test
├── extract                 <--- Python scripts that extract data from csv.
│  |── data_source          <--- Various locations to fetch the data
│  └── extract.py           <--- Various utilities for extracting the data from csv
├── load        
│  └── load_data.py         <--- Various utilities for loading the data to database
├── README.md               <--- This file
├── Redash                  <--- Redash related codes
├── requirements.txt        <--- Dependencies
├── screenshots             <--- Screenshot outputs
├── tests                   <--- Unit tests for python code.
└── utils                   <--- Various Python scripts
   ├── data_utils.py        <--- Data extraction utils.
   └── db_utils.py          <--- DatabaseManager class
```

## Key Components

### Airflow DAGs

Airflow DAGs orchestrate the ELT pipeline's execution. Two main DAGs are defined:

- dbt_transformations: Executes dbt commands for data transformation, including running transformations and generating documentation.
- create_db_and_load_data: Manages the creation of a database and loading of data from CSV files into multiple tables using Python operators.

### dbt Transformations

dbt is leveraged for data modeling and transformations. The transformation SQL scripts are organized into separate models, each performing specific aggregations and calculations on the vehicle trajectory data.

### Data Loading

Data loading tasks are executed within the Airflow DAGs. Python operators are utilized to create a database, create tables, and load data from CSV files into the database tables. SQLAlchemy is used for database interaction, ensuring efficient data loading processes.

## Setup Instructions

1. Clone this repository to your local environment.
2. Install Apache Airflow and dbt following the respective documentation.
3. Configure the traffic_db_profile in dbt for connecting to your database.
4. Update the connection string and file paths in the Airflow DAGs as per your environment.
5. Deploy the DAGs to your Airflow instance and ensure they are scheduled to run at the desired intervals.

## Usage

Once the setup is complete, the Airflow DAGs will automatically execute the defined tasks according to the specified schedule. Monitor the Airflow UI for task status and logs, and use dbt documentation to explore transformed data models.

## Contributors

- [@abyt101](https://github.com/AbYT101) - Abraham Teka

## Tech Stacks
|       |  | | | | | | |
| ----------- | ----------- | -------- | ---------| -----------| -------| -----------| -------|
| <img height="80" src="https://user-images.githubusercontent.com/25181517/117208740-bfb78400-adf5-11eb-97bb-09072b6bedfc.png">   |*postgreSQLs*| | <img height="80" src="https://www.docker.com/wp-content/uploads/2022/03/vertical-logo-monochromatic.png">   |*docker*| | <img height="80" src="https://avatars.githubusercontent.com/u/10746780?s=280&v=4">   |*redash*|
| <img height="80" src="https://static-00.iconduck.com/assets.00/airflow-icon-512x512-tpr318yf.png">   |*airflow*| | <img height="80" src="https://seeklogo.com/images/D/dbt-logo-500AB0BAA7-seeklogo.com.png">   |*dbt*|

<br>

## Challenge by

![10 Academy](https://static.wixstatic.com/media/081e5b_5553803fdeec4cbb817ed4e85e1899b2~mv2.png/v1/fill/w_246,h_106,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/10%20Academy%20FA-02%20-%20transparent%20background%20-%20cropped.png)
