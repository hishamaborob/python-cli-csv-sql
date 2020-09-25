## CSV SQL CLI Tool

#### Overview

- An interactive CLI tool that runs SQL queries against csv files.
- A simple Python 3.8 based CLI tool that uses no external libraries.
- Unit and integration tested using Python's unittest.
- Some important documentation/comments is provided at the header of almost all files.
- Some test data (csv files) is provided under ./test/data
- The tool starts by executing the special bootstrap file and provide a directory as parameter.
- The bootstrap will build the main context and inject dependencies.

#### How to Use

Run the test:


```
$ python3 -m unittest discover test/
```


Run the tool:


    $ python3 cli_csv_sql.py /path/to/directory/where/csv/files

Quit the tool:


    $ q

Example:


    xx@xx:~/cli_csv_sql$ python3 cli_csv_sql.py /home/xx/Downloads
    2 Tables:
    techcrunch
    techcrunch-test-data
    /home/xx/Downloads=#select company,numEmps from techcrunch where numEmps=14;
    5 records returned: 
    company        numEmps        
    Scribd         14             
    Scribd         14             
    Scribd         14             
    SayNow         14             
    DailyStrength  14             
    /home/xx/Downloads=# q
    xx@xx:~/cli_csv_sql$

