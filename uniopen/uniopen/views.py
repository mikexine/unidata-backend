# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import render_template, session, request, flash, redirect, url_for
from .app import app, db
from .models import User, University, Studyroom
from .forms import RegisterForm, LoginForm, AddUniversityForm, AddStudyRoomForm
from .utils import flash_errors, login_required
from sqlalchemy.exc import IntegrityError


@app.route("/", methods=["GET", "POST"])
def home():
    form = LoginForm(request.form)
    if request.method == 'POST':
        u = User.query.filter_by(username=request.form['username'],
                                password=request.form['password']).first()
        if u is None:
            error = 'Invalid username or password.'
            flash(error, 'warning')
        else:
            session['logged_in'] = True
            session['username'] = u.username
            flash("You are logged in.", 'success')
            return redirect(url_for("members"))
    return render_template("home.html", form=form)


@app.route("/members/", methods=['GET', 'POST'])
@login_required
def members():
    unilist = University.query.all()
    # print unilist[0].shortname
    return render_template("members.html", unilist=unilist)


@app.route("/studyrooms/<unid>/", methods=['GET', 'POST'])
@login_required
def studyrooms(unid):
    studylist = db.session.query(Studyroom).filter_by(university_id=unid).all()
    return render_template("studyrooms.html", studylist=studylist, unid=unid)


@app.route("/studyrooms/<unid>/addstudyroom/", methods=['GET', 'POST'])
@login_required
def addstudyroom(unid):
    form = AddStudyRoomForm(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        new_sr = Studyroom(form.shortname.data, form.fullname.data, form.seats.data, form.address.data, form.texthours.data, form.phone.data)
        currentuni = University.query.get(unid)
        currentuni.studyrooms.append(new_sr)
        try:
            db.session.add(new_sr)
            db.session.commit()
            flash("Thank you for adding a new study room", 'success')
            return redirect("/studyrooms/%s/" % unid)
        except IntegrityError as err:
            print(err)
            flash("That study room already exists. Try again.", 'error')
    else:
        flash_errors(form)
    return render_template("addstudyroom.html", form=form)


@app.route("/studyrooms/<unid>/editstudyroom/<unisr>/", methods=['GET', 'POST'])
@login_required
def editstudyroom(unid, unisr):
    currentsr = Studyroom.query.get(unisr)
    form = AddStudyRoomForm(request.form, obj=currentsr, csrf_enabled=False)
    if form.validate_on_submit():
        form.populate_obj(currentsr)
        new_sr = Studyroom(form.shortname.data, form.fullname.data, form.seats.data, form.address.data, form.texthours.data, form.phone.data)
        try:
            db.session.commit()
            flash("Thank you for fixing the data!", 'success')
            return redirect("/studyrooms/%s/" % unid)
        except IntegrityError as err:
            print(err)
            flash("That study room already exists. Try again.", 'error')
    else:
        flash_errors(form)
    return render_template("addstudyroom.html", form=form)


@app.route("/adduniversity/", methods=['GET', 'POST'])
@login_required
def adduniversity():
    form = AddUniversityForm(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        new_uni = University(form.shortname.data, form.fullname.data, form.address.data)
        try:
            db.session.add(new_uni)
            db.session.commit()
            flash("Thank you for adding a new uni", 'success')
            return redirect(url_for('members'))
        except IntegrityError as err:
            print(err)
            flash("That uni already exists. Try again.", 'error')
    else:
        flash_errors(form)
    return render_template("adduniversity.html", form=form)


@app.route("/edituniversity/<unid>/", methods=['GET', 'POST'])
@login_required
def edituniversity(unid):
    currentuni = University.query.get(unid)
    form = AddUniversityForm(request.form, obj=currentuni, csrf_enabled=False)
    if form.validate_on_submit():
        form.populate_obj(currentuni)
        new_uni = University(form.shortname.data, form.fullname.data, form.address.data)
        try:
            db.session.commit()
            flash("Thank you for fixing the data!", 'success')
            return redirect(url_for('members'))
        except IntegrityError as err:
            print(err)
            flash("That uni already exists. Try again.", 'error')
    else:
        flash_errors(form)
    return render_template("adduniversity.html", form=form)


@app.route('/logout/')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    flash('You are logged out.', 'info')
    return redirect(url_for('home'))

@app.route("/register/", methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        new_user = User(form.username.data, form.email.data, form.password.data)
        try:
            db.session.add(new_user)
            db.session.commit()
            flash("Thank you for registering. You can now log in.", 'success')
            return redirect(url_for('home'))
        except IntegrityError as err:
            print(err)
            flash("That username and/or email already exists. Try again.", 'error')
    else:
        flash_errors(form)
    return render_template('register.html', form=form)


@app.route("/docs/")
def docs():
    form = LoginForm(request.form)
    return render_template("docs.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
