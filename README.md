## Traffic Trends Across UK Regions
=========================

### Executive Summary

Traffic congestion is a growing issue in urban areas, leading to longer travel times, increased fuel consumption, and higher environmental pollution. This project leverages a time series approach to analyze and forecast traffic patterns across UK regions, examining factors like road type, road condition, and road class. The project aims to provide a comprehensive analysis of traffic patterns and trends, enabling policymakers to make informed decisions regarding traffic management and infrastructure investments.

### Problem Statement

The project's goal is to accurately predict traffic volumes by analyzing vehicle counts collected at regular intervals (monthly). By identifying patterns in vehicle counts and traffic flow dynamics, we aim to help local authorities optimize traffic flow, reduce congestion, and improve infrastructure. The project addresses the challenge of predicting traffic volumes across different regions using time series modeling to inform better traffic management and infrastructure planning.


### Data science opportunity
This project presents a data opportunity to leverage historical traffic patterns for predictive modeling, enabling more informed decisions in traffic management, congestion reduction, and infrastructure optimization. By applying data science techniques, the project aims to build models that forecast future traffic volumes based on historical data, helping stakeholders identify trends and optimize resources.

### Key takeaways

**Key Models:**

- Naive Model: SMAPE of 82.37%
- Prophet: SMAPE of 99.07%
- XGBoost: SMAPE of 82.93% (best performance)

**Features Used:**
- Road types, Year averages, Lagged traffic volumes, and Date-based features like day of the week.

**Technologies:**
- Python (pandas, XGBoost, Prophet, matplotlib)

**Setup:**
- Clone repo: git clone https://github.com/brainstation-datascience/capstone-Emillia-rosette.git

**Results:**

- XGBoost performed much better than the other two models, especially with added features like road types and lagged traffic data.

**Future Work:**
- Add weather, real-time data.
- Explore deep learning models for more complex patterns (e.g., LSTM).


### Datasets Overview
This project uses a comprehensive traffic dataset collected from the UK Department for Transport. The dataset includes vehicle counts by road type, direction, and location. Below is a summary of key variables used:

## Datasets Overview
This project uses a comprehensive traffic dataset collected from the UK Department for Transport. The dataset includes vehicle counts by road type, direction, and location. Below is a summary of key variables used:

| **Variable Name**           | **Description**                                                                                                                                       |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| `count_point_id`            | A unique reference for the road link that links the AADFs to the road network.                                                                         |
| `direction_of_travel`       | Direction of travel (e.g., North, South, East, West).                                                                                                  |
| `year`                      | Counts are shown for each year from 2000 onwards.                                                                                                      |
| `count_date`                | The date when the actual count took place.                                                                                                             |
| `hour`                      | The time when the counts in questions took place where 7 represents between 7am and 8am, and 17 represents between 5pm and 6pm.                         |
| `region_id`                 | Website region identifier.                                                                                                                             |
| `region_name`               | The name of the Region that the Count Point (CP) sits within.                                                                                           |
| `region_ons_code`           | The Office for National Statistics code identifier for the region.                                                                                      |
| `local_authority_id`        | Website local authority identifier.                                                                                                                    |
| `local_authority_name`      | The local authority that the CP sits within.                                                                                                            |
| `local_authority_code`      | The Office for National Statistics code identifier for the local authority.                                                                             |
| `road_name`                 | This is the road name (for instance, M25 or A3).                                                                                                        |
| `road_category`             | The classification of the road type (e.g., Motorway, Class A, Minor road).                                                                              |
| `road_type`                 | Whether the road is a ‘major’ or ‘minor’ road.                                                                                                          |
| `start_junction_road_name`  | The road name of the start junction of the link.                                                                                                        |
| `end_junction_road_name`    | The road name of the end junction of the link.                                                                                                          |
| `easting`                   | Easting coordinates of the CP location.                                                                                                                 |
| `northing`                  | Northing coordinates of the CP location.                                                                                                                |
| `latitude`                  | Latitude of the CP location.                                                                                                                            |
| `longitude`                 | Longitude of the CP location.                                                                                                                           |
| `link_length_km`            | Total length of the network road link for that CP (in kilometres).                                                                                      |
| `link_length_miles`         | Total length of the network road link for that CP (in miles).                                                                                           |
| `pedal_cycles`              | Counts for pedal cycles.                                                                                                                                |
| `two_wheeled_motor_vehicles`| Counts for two-wheeled motor vehicles.                                                                                                                  |
| `cars_and_taxis`            | Counts for cars and taxis.                                                                                                                              |
| `buses_and_coaches`         | Counts for buses and coaches.                                                                                                                           |
| `LGVs`                      | Counts for Light Goods Vehicles (LGVs).                                                                                                                 |
| `HGVs_2_rigid_axle`         | Counts for two-rigid axle Heavy Goods Vehicles (HGVs).                                                                                                  |
| `HGVs_3_rigid_axle`         | Counts for three-rigid axle HGVs.                                                                                                                       |
| `HGVs_4_or_more_rigid_axle` | Counts for four or more rigid axle HGVs.                                                                                                                |
| `HGVs_3_or_4_articulated_axle`| Counts for three or four-articulated axle HGVs.                                                                                                      |
| `HGVs_5_articulated_axle`   | Counts for five-articulated axle HGVs.                                                                                                                  |
| `HGVs_6_articulated_axle`   | Counts for six-articulated axle HGVs.                                                                                                                   |
| `all_HGVs`                  | Counts for all HGVs.                                                                                                                                    |
| `all_motor_vehicles`        | Counts for all motor vehicles.                                                                                                                          |
| `Month`                     | The month when the traffic count was recorded.                                                                                                          |
| `Day_of_Week`               | The day of the week when the traffic count was recorded.                                                                                                |
| `Day`                       | The specific day of the month when the traffic count was recorded.                                                                                      |
<!-- 
#### Road Definitions
- **Major Roads**: Includes motorways and all class ‘A’ roads. These roads usually have high traffic flows and are often the main arteries to major destinations.
  - **Motorways**: Built under the enabling legislation of the Special Roads Act 1949, now consolidated in the Highways Acts of 1959 and 1980. These include major roads of regional and urban strategic importance, often used for long-distance travel.
  - **‘A’ Roads**: These can be trunk or principal roads, often described as the 'main' roads.
    - **Trunk Roads**: Designated by the Trunk Roads Acts 1936 and 1946. Most motorways and many long-distance rural ‘A’ roads are trunk roads.
    - **Principal Roads**: Maintained by local authorities, these are significant roads, including some motorways.

- **Minor Roads**: These include ‘B’ and ‘C’ classified roads and unclassified roads, all of which are maintained by local authorities.
  - **‘B’ Roads**: In urban areas, can have relatively high traffic flows but are not regarded as significant as 'A' roads.
  - **‘C’ Roads**: Regarded as of lesser importance than ‘B’ or ‘A’ roads, generally having only one carriageway of two lanes and carrying less traffic.
  - **Unclassified Roads**: Includes residential roads both in urban and rural situations, typically with low traffic flows. -->

<!-- #### Types of Vehicle
- **All_MV**: All Motor Vehicles
- **2WMV**: Two-wheeled motor vehicles (e.g., motorcycles)
- **Car**: Cars and Taxis
- **LGV**: Light Goods Vans
- **HGV**: Heavy Goods Vehicle total
  - **HGVR2**: 2-rigid axle Heavy Goods Vehicle
  - **HGVR3**: 3-rigid axle Heavy Goods Vehicle
  - **HGVR4**: 4 or more rigid axle Heavy Goods Vehicle
  - **HGVA3**: 3 and 4-articulated axle Heavy Goods Vehicle
  - **HGVA5**: 5-articulated axle Heavy Goods Vehicle
  - **HGVA6**: 6 or more articulated axle Heavy Goods Vehicle
- **PC**: Pedal Cycles
<!--  -->

#### Vehicle Type Definitions
- **All Motor Vehicles**: All vehicles except pedal cycles.
- **Cars and Taxis**: Includes passenger vehicles with nine or fewer seats, three-wheeled cars, and four-wheel-drive ‘sports utility vehicles’ (SUV).
- **Motorcycles etc**: Includes motorcycles, scooters, and mopeds.
- **Buses and Coaches**: Includes all public service vehicles and works buses over 3.5 tonnes.
- **Light Vans**: Goods vehicles not exceeding 3.5 tonnes gross vehicle weight.
- **Heavy Goods Vehicles (HGV)**: Includes all goods vehicles over 3.5 tonnes gross vehicle weight.
  - **Rigid Heavy Goods Vehicles**: Includes rigid HGVs with varying numbers of axles.
  - **Articulated Heavy Goods Vehicles**: Classified based on the number of axles on the road. -->


### Demo
<!-- 
... Show your work:
...     Data visualisations
...     Interactive demo (e.g., streamlet app)
...     Short video of users trying out the solution -->


### Methodology

<!-- ... High-level diagrams of entire process:
...     various data processing steps
...     various modelling directions
...     various prototyping directions -->

![Alt text](methodology.png)

### Project Structure
│
├── **.devcontainer/**            # Development container configuration
├── **.github/**                  # GitHub workflows and settings
├── **.ipynb_checkpoints/**       # Jupyter notebook checkpoints
├── **.vscode/**                  # VS Code workspace settings
├── **data/**                     # Contains datasets and processed data files
├── **docs/**                     # Documentation files for the project
├── **Emillia-rosette_Nlandu_Capstone Assets/** # Project assets like images and presentations
├── **model/**                    # Folder for storing trained models and artifacts
├── **notebooks/**                # Jupyter notebooks for data analysis and modeling
├── **references/**               # Research papers and additional references
├── **src/**                      # Source code for data processing and modeling
├── **.gitignore**                # Specifies files to be ignored by Git
├── **conda.yml**                 # Conda environment specification file
├── **Correlation.png**           # Correlation plot image
├── **data_dictionary.md**        # Data dictionary for the project
├── **essex_map.json**            # GeoJSON file for mapping
├── **final_presentation.pdf**    # Final project presentation (PDF)
├── **final_presentation.pptx**   # Final project presentation (PowerPoint)
├── **LICENSE**                   # License file for the project
├── **Makefile**                  # Makefile for project automation
├── **methodology.png**           # Methodology flowchart image
├── **notebooks.zip**             # Zipped folder of project notebooks
└── **README.md**                 # Project readme file


### Credits & References

- Department for Transport. (n.d.) All Traffic Data Metadata. Available at: https://storage.googleapis.com/dft-statistics/road-traffic/all-traffic-data-metadata.pdf (2024).
- Williams, D. (2023) 'Sadiq Khan says London's congestion problems are improving despite complaints of traffic jams', Daily Mail, 5 August. Available at: https://www.dailymail.co.uk/news/article-13566731/Sadiq-Khan-London-congestion-roads-traffic.html (Accessed: 4 August 2024)

------------------------------------------------------------------------------
#### Usage

This is a template repository for quickly setting up a data science project
It includes a simple folder structure and a conda environment for isolated dependency management.

1. Start a new repo using this template
2. Update your `LICENSE` file.
3. Update your `README.md` file. 
4. Set up and activate conda environment
    1. Rename your conda environment in the `./conda.yml` file.
    2. Add/change any dependencies and their versions in the `./conda.yml` file.
    3. Set up your conda environment and activate it by running:
        ```bash
        conda env create -f conda.yml
        conda activate <your-env-name>
        ```
5. Add your own scripts in `./src/`
6. Add your own notebooks in `./notebooks/`
7. Add your own data in `./data/`
    gitignore will ignore the data folder when you push to github
    save a copy of your raw and process data, 
    pickled models in a Google Drive folder
    and add the link in the gdrive-links.md file
8. Add your project documents, reports, presentation pdfs in the `./docs`
9. Add your references (tutorials, papers, books etc.) in `./references` 