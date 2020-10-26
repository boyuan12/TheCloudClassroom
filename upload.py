import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from string import ascii_letters
import random

engine = create_engine("postgres://gbaddrwiegwvxu:bc0932e37cafe72985ad867afdc32e8b5b5b6aa01f5e750c418e91b47d6eb7e7@ec2-34-237-247-76.compute-1.amazonaws.com:5432/degnrhmmhp6q7a")
db = scoped_session(sessionmaker(bind=engine))
s = db()

def random_str(n=10):
    return "".join([random.choice(ascii_letters) for i in range(n)])

def parse_date(date):
    """ 29-Nov-20 """
    dm = {
        "Jun": "06",
        "Jul": "07",
        "Aug": "08",
        "Sep": "09",
        "Oct": "10",
        "Nov": "11"
    }
    date = date.split("-")
    try:
        month = dm[date[1]]
    except:
        return "2020-12-31"
    date = f"2020-{month}-{date[0]}"
    return date


with open('Copy of CC - Course List.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            if row[7] == "Complete":
                status = 2
            elif row[7] == "Active":
                status = 1
            elif row[7] == "Approved":
                status = 3
            s.execute("INSERT INTO events (slug, collection_id, created_on, updated_on, published_on, location, link, img, short_description, long_description, content, name, status, price, grade, start_date, end_date) VALUES (:slug, '12345', now(), now(), now(), 'Zoom', 'N/A', 'https://uploads-ssl.webflow.com/5f5bb5fb0054280aeb0e2b98/5f5bc42090115375ae621420_Screen%20Shot%202020-09-11%20at%2011.38.12%20AM-p-500.png', :desc, :desc, :desc, :name, :status, '0', :grade, :start, :end)", {"slug": random_str(), "desc": f'This is a course taught by {row[5]}', "name": row[1], "status": status, "grade": row[2], "start": parse_date(row[8]), "end": parse_date(row[9])})
            s.commit()
            print(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
            line_count += 1
    print(f'Added {line_count} courses.')