# Fill in this file with the code from parsing YAML exercise
import json
import yaml

with open('myfile.yaml','r') as yaml_file:
    ouryaml = yaml.safe_load(yaml_file)

print (ouryaml)

print ("The acces token is {}".format(ouryaml['access_token']))
print ("The token expires in {} seconds.".format(ouryaml['expires_in']))
