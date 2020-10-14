import os
from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from datetime import datetime

app = Flask(__name__)

engine = create_engine("postgres://huvphgbrnoupis:7f122ceda4954d16d4bb928b2e026d4ba2bc8f01fe24bc28dacd89c69e563e89@ec2-54-160-120-28.compute-1.amazonaws.com:5432/da15nie4o0pfki")
db = scoped_session(sessionmaker(bind=engine))
s = db()
##
@app.route("/")
@app.route("/index.html")
def index():
    result = s.execute("SELECT * FROM events")
    listT = []
    for row in result:
        row_as_dict = dict(row)
        listT.append(row_as_dict)
    print(listT)
    return render_template("index.html", results=listT)

@app.route("/courses")
@app.route("/course.html")
def courses():
    result = s.execute("SELECT * FROM events LIMIT 4")
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