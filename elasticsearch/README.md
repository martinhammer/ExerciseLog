Elastic Search
==============

Prequisites
- Linux
- Spark with pyspark working correctly (tested with Spark 1.5)
- Elastic Search and Kibana - in my setup running inside Docker


Step 0:
All of the steps below assume that you are running them from the root directory of the repository, i.e. "ExerciseLog"

Step 1:
Prepare data by taking the markdown exercise log and converting it to JSON.
Note: in the future this step will become redundant and instead the pyspark program will write directly to Elastic Search.

```bash
spark-submit elasticsearch/generatejson.py
```

Step 2:
Concatenate the output from Spark into a single file

```bash
cat data/json/sample/* > data/json/sample.json
```
Step 3:
Start Elastic Search and Kibana

```bash
docker network create exerciselog
docker run -d --name elasticsearch --net exerciselog elasticsearch
docker run -d -p 5601:5601 --name kibana --net exerciselog kibana
```
Note down the IP addresses of ES and Kibana
Note: in the future this step will not be needed
```bash
docker inspect elasticsearch
docker inspect kibana
```

Step 4:
Upload the data into Elastic. 

_TBD_

Step 5:
Kibana stuff.

_TBD_
