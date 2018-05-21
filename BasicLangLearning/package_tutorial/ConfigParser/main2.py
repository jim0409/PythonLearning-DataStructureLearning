import configparser

config = configparser.RawConfigParser()
# it's where i put my config
config.read(
    '/Users/jimweng/PythonLearning-DataStructureLearning/tbrain/src/config_par.conf')

configFile = config['ModelParameter']

# configFile.Raw
configs = {}

for i in config['ModelParameter'].keys():
    # convert default(lowercase) to uppercase
    configs[i.upper()] = config['ModelParameter'].get(i)

print(configs)
