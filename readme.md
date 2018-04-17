# TICK - Udemy #
Welcome to the source code repository of the udemy course: **Master timeseries by using the TICK stack example by example**

> Slides: https://docs.google.com/presentation/d/1b87uuah-T-EiXKHqXlrmAFR1-rBHTLTMPvERBi3RM50/edit?usp=sharing

[Install](#install)

[Run python script](#run-python) 

[Influxdb project 1: Write and read temperatures using the influxdb REST api](01_write_and_read_temperature/readme.md)

 
## <a name="install"> </a> Install ##
1. Install docker-compose: https://docs.docker.com/compose/install/
2. Install python 3.6.2 and virtualenv https://www.python.org/downloads/release/python-362/
3. Create virtualenv:
    ```bash
    bash setup_python.sh 
    ```

## <a name="run-python"> </a> Run python script ##
 Make sure you have started influxdb
 ```bash
    source python_tick_udemy/bin/activate
    cd 01_write_and_read_temperature
    python create_db.py
```


