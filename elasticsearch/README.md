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
Concatenate the output from Spark into a single file and generate data to be inserted into Elastic Search.

```bash
cat data/json/sample/* > data/json/sample.json
awk -F\" -f elasticsearch/json2es.awk data/json/sample.json > data/elastic/sample.es
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
Create the Elastic Search index and upload data into it (replace the IP address with the one for ElasticSearch from the previous step)

_TBD_

```bash
cd data/elastic
curl -s -XPOST http://172.19.0.2:9200/exerciselog/dailylog/_bulk --data-binary @sample.es
cd -
```

Step 5:
Kibana stuff.

_TBD_
