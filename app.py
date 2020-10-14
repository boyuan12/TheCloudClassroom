from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from datetime import datetime

app = Flask(__name__)

engine = create_engine("postgres://gbaddrwiegwvxu:bc0932e37cafe72985ad867afdc32e8b5b5b6aa01f5e750c418e91b47d6eb7e7@ec2-34-237-247-76.compute-1.amazonaws.com:5432/degnrhmmhp6q7a")
db = scoped_session(sessionmaker(bind=engine))
s = db()

import sentry_sdk
# from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://dad50acd268449f99482f3bbf4bb96dd@o393097.ingest.sentry.io/5462790",
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0
)

@app.route("/")
@app.route("/index.html")
def index():
    result = s.execute("SELECT * FROM events WHERE status=1 LIMIT 4")
    listT = []
    for row in result:
        row_as_dict = dict(row)
        listT.append(row_as_dict)
    print(listT)
    return render_template("index.html", results=listT)

@app.route("/courses")
@app.route("/course.html")
def courses():
    result = s.execute("SELECT * FROM events")
    listT = []
    for row in result:
        row_as_dict = dict(row)
        listT.append(row_as_dict)
    print(listT)
    return render_template("courses.html", results=listT)


@app.route("/courses/<string:slug>")
def course_detail(slug):
    result = s.execute("SELECT * FROM events WHERE slug=:s", {"s": slug})
    course = []
    for row in result:
        row_as_dict = dict(row)
        course.append(row_as_dict)

    if len(course) == 0:
        return "404 NOT FOUND"

    course_ins = s.execute("SELECT * FROM events_instructor WHERE event_id=:id", {"id": course[0]["id"]})
    ins = []
    for row in course_ins:
        row_as_dict = dict(row)
        ins.append(row_as_dict)

    instructor_id = ins[0]["instructor_id"]

    result = s.execute("SELECT * FROM instructors WHERE id=:id", {"id": instructor_id})
    instructor_info = []
    for row in result:
        row_as_dict = dict(row)
        instructor_info.append(row_as_dict)

    print(instructor_info[0])

    return render_template("detail_product.html", data=course[0], ins=instructor_info[0]) ####


@app.route("/courses-all")
def courses_all():
    result = s.execute("SELECT * FROM events")
    info = []
    for row in result:
        row_as_dict = dict(row)
        if datetime(row_as_dict["end_date"].year, row_as_dict["end_date"].month, row_as_dict["end_date"].day) > datetime(datetime.now().year, datetime.now().month, datetime.now().day):
            row_as_dict["active"] = True
        else:
            row_as_dict["active"] = False
        info.append(row_as_dict)
    print(info)
    return render_template("courses-all.html", info=info)


@app.route("/<string:html>")
def other_file(html):
    try:
        return render_template(html)
    except:
        return render_template("404.html")

###