import json

with open('individual_assignment_jan2020/Afghanistan.json', encoding = 'utf8') as file:
    data = json.load(file)  # a list of dictionaries
# "date_start" and "date_end" to make the graph
# "best", "high" and "low" for deaths


Afghanistan_list = []
for event in data:
    Afghanistan_list.append(f"{event['date_start']},{event['date_end']},{event['deaths_a']},{event['deaths_b']},{event['deaths_civilians']},{event['best']},{event['high']},{event['low']}")
print(Afghanistan_list)

# csv layout has a header as first line
# intention: make every element in Afghanistan_list its own row
with open('Afghanistan.csv', 'w') as file:
    file.writelines('date_start,date_end,deaths_a,deaths_b,deaths_civilians,best,high,low\n')
    for element in Afghanistan_list:
        file.writelines(f'{element}\n')