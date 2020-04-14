import csv
import pdb

def k():

    processed_data = {}
    with open('../data/pollution-data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        i = 0
        for row in reader:

            if row['date'] == 'NA':
                i += 1
                print(i)
            else:
                # process time
                year, month, date = row['date'].split("-")

                pruned_data = {
                    'year': year,
                    'month': month,
                    'date': date,
                    'so2': row['so2'],
                    'no2': row['no2'],
                    'rspm': row['rspm'],
                    'spm': row['spm'],
                    'pm2_5': row['pm2_5']
                }


                # map keys based on location
                state = row['state']
                city = row['location']
                region = row['type']
                # pdb.set_trace()
                if state not in processed_data:
                    processed_data[state] = {}
                    processed_data[state][city] = pruned_data
                else:
                    if city not in processed_data:
                        processed_data[state][city] = pruned_data
                    else:
                        processed_data[state][city] = pruned_data

    pdb.set_trace()
    return 0

if __name__=='__main__':
    print(k())