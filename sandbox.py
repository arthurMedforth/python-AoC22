from elasticsearch_dsl import Q

dict_of_fields = ["filename","match.label"]
must = []
for item in dict_of_fields:    
    must.append({'match': {'field_name': item}})

query = Q('bool', must=must)

print(type(query))