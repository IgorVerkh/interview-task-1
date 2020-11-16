from json import load, dumps


config = 'source_file_2.json'

managers = {}
watchers = {}

with open(config, encoding='utf-8') as f:
    config = load(f)

# sort by priority
config = sorted(config, key=lambda k: k['priority'])

for proj in config:

    for mng in proj['managers']:
        if mng not in managers:
            managers[mng] = []
        managers[mng].append(proj['name'])

    for wtch in proj['watchers']:
        if wtch not in watchers:
            watchers[wtch] = []
        watchers[wtch].append(proj['name'])

json_object = dumps(managers, indent = 4)
with open('managers.json', 'w') as outfile:
    outfile.write(json_object)

json_object = dumps(watchers, indent = 4)
with open('watchers.json', 'w') as outfile:
    outfile.write(json_object)
