# json2es.awk
# Converts the JSON input into a bulk insert file for Elastic Search
# delimiter needs to be set to double quote i.e. awk -F\" json2es.awk
{
	print "{ \"index\" : { \"_index\" : \"exerciselog\", \"_type\" : \"dailylog\", \"_id\" : \"" $4" \"} }"
	print $0
}
