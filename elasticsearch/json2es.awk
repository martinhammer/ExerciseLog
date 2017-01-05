# json2es.awk
# Converts the JSON input into a bulk insert file for Elastic Search
{
	print "{ \"index\" : { \"_index\" : \"exerciselog\", \"_type\" : \"dailylog\", \"_id\" : \"" $4" \"} }"
	print $0
}
