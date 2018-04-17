# Influxdb project 1: Write and read temperatures using the influxdb REST api #

[Back to main readme](../readme.md)

Scenario: Create and store temperatures for a sensor located in a greenhouse, and graph the temperatures of the last day

## Setup ##
1. Start influxdb
    ```bash
    cd ../00_config/influx-only
    docker-compose up
    ```
2. Run python script
     ```bash
        source ../python_tick_udemy/bin/activate
        python create_db.py
    ```

## Javascript ##
[Fiddle](https://jsfiddle.net/fettleif/2aa8v2q3/)

