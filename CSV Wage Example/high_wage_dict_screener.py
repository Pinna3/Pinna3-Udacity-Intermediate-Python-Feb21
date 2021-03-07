import csv

high_wages = []
desired_wage = 40000

with open('wage_info.csv', 'r') as infile:
    reader = csv.DictReader(infile)
    for elem in reader:
        if int(elem['annual_wage']) < desired_wage:
            continue
        high_wages.append(elem)

with open('high-wages-with-headers.csv', 'w') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=high_wages[0].keys())
    writer.writeheader()
    for elem in high_wages:
        writer.writerow(elem)
