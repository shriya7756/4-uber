import sys
import csv
def mapper():
    for line in sys.stdin:
        line = line.strip()
        data = list(csv.reader([line]))[0]
        if len(data) < 4:
            continue
        if data[0].lower() == 'date/time':
            continue
        date_time = data[0]
        date = date_time.split(' ')[0] 
        print(f"{date}\t1")
if __name__ == "__main__":
    mapper()

