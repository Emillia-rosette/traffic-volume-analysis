


## Data Dictionary

#### Data Dictionary: Count Points


| **Column Name**               | **Description**                                                | **Data Type** |
|-------------------------------|----------------------------------------------------------------|---------------|
| **count_point_id**             | A unique identifier for the count point.                       | int64         |
| **region_id**                  | Identifier for the region where the count point is located.    | int64         |
| **region_name**                | Name of the region where the count point is located.           | object        |
| **local_authority_id**         | Identifier for the local authority where the count point is located. | int64         |
| **local_authority_name**       | Name of the local authority where the count point is located.  | object        |
| **road_name**                  | Name of the road where the count point is located.             | object        |
| **road_type**                  | Type of the road (e.g., major, minor).                         | object        |
| **start_junction_road_name**   | Name of the road at the start junction of the link.            | object        |
| **end_junction_road_name**     | Name of the road at the end junction of the link.              | object        |
| **easting**                    | Easting coordinate of the count point location.                | int64         |
| **northing**                   | Northing coordinate of the count point location.               | int64         |
| **latitude**                   | Latitude of the count point location.                          | float64       |
| **longitude**                  | Longitude of the count point location.                         | float64       |
| **link_length_km**             | Length of the road link in kilometers.                         | float64       |
| **link_length_miles**          | Length of the road link in miles.                              | float64       |

#### Data Dictionary: Raw Count

| **Variable Name**                 | **Description**                                                                                       | **Data Type** |
|-----------------------------------|-------------------------------------------------------------------------------------------------------|---------------|
| **Count_point_id**                | A unique reference identifier for the road link associated with the count data.                        | Integer       |
| **Direction_of_travel**           | Direction of travel for the vehicles being counted (e.g., Northbound, Southbound).                     | String        |
| **Year**                          | The year in which the count was recorded.                                                              | Integer       |
| **Count_date**                    | The date on which the actual count took place.                                                         | Date          |
| **Hour**                          | The hour during which the count took place. `7` represents 7am-8am, and `17` represents 5pm-6pm.       | Integer       |
| **Region_id**                     | Website region identifier.                                                                             | Integer       |
| **Region_name**                   | The name of the region where the count point (CP) is located.                                          | String        |
| **Region_ons_code**               | The Office for National Statistics (ONS) code identifier for the region.                               | String        |
| **Local_authority_id**            | Website local authority identifier.                                                                    | Integer       |
| **Local_authority_name**          | The name of the local authority where the CP is located.                                               | String        |
| **Local_authority_code**          | The ONS code identifier for the local authority.                                                       | String        |
| **Road_name**                     | The name of the road where the count took place (e.g., M25, A3).                                       | String        |
| **Road_category**                 | The classification of the road type (e.g., Motorway, A Road, B Road).                                  | String        |
| **Road_type**                     | Indicates whether the road is classified as a 'major' or 'minor' road.                                 | String        |
| **Start_junction_road_name**      | The road name of the start junction of the link.                                                       | String        |
| **End_junction_road_name**        | The road name of the end junction of the link.                                                         | String        |
| **Easting**                       | The easting coordinate of the CP location.                                                             | Float         |
| **Northing**                      | The northing coordinate of the CP location.                                                            | Float         |
| **Latitude**                      | The latitude of the CP location.                                                                       | Float         |
| **Longitude**                     | The longitude of the CP location.                                                                      | Float         |
| **Link_length_km**                | The total length of the network road link for that CP (in kilometers).                                 | Float         |
| **Link_length_miles**             | The total length of the network road link for that CP (in miles).                                      | Float         |
| **Pedal_cycles**                  | The count of pedal cycles.                                                                             | Integer       |
| **Two_wheeled_motor_vehicles**    | The count of two-wheeled motor vehicles.                                                               | Integer       |
| **Cars_and_taxis**                | The count of cars and taxis.                                                                           | Integer       |
| **Buses_and_coaches**             | The count of buses and coaches.                                                                        | Integer       |
| **LGVs**                          | The count of Light Goods Vehicles (LGVs).                                                              | Integer       |
| **HGVs_2_rigid_axle**             | The count of Heavy Goods Vehicles (HGVs) with 2 rigid axles.                                           | Integer       |
| **HGVs_3_rigid_axle**             | The count of HGVs with 3 rigid axles.                                                                  | Integer       |
| **HGVs_4_or_more_rigid_axle**     | The count of HGVs with 4 or more rigid axles.                                                          | Integer       |
| **HGVs_3_or_4_articulated_axle**  | The count of HGVs with 3 or 4 articulated axles.                                                       | Integer       |
| **HGVs_5_articulated_axle**       | The count of HGVs with 5 articulated axles.     
