from flask import Blueprint, render_template, redirect, url_for

from app.models import EditableHTML, Department, ContrType, ProfServ

from app.main.forms import ResultsForm

from datetime import datetime

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('main/index.html')


@main.route('/about')
def about():
    editable_html_obj = EditableHTML.get_editable_html('about')
    return render_template(
        'main/about.html', editable_html_obj=editable_html_obj)

# Route to search page, where users can search for city contracts
@main.route('/search', methods=['GET', 'POST'])
def search():
    form = ResultsForm()
    depts = Department.query.all()
    types = ContrType.query.all()
    format = '%m-%d-%Y'
    if form.validate():
        filtered = ProfServ.query.all()
        if form.vendor_name.data != "":
            filtered = ProfServ.query.filter_by(vendor=form.vendor_name.data)
        if form.contract_number.data != "":
            filtered = ProfServ.query.filter_by(original_contract_id=form.contract_number.data)
        if form.start_date.data != "":
            filtered = ProfServ.query.filter(ProfServ.start_dt >= datetime.strptime(form.start_date.data, format))
        if form.end_date.data != "":
            filtered = ProfServ.query.filter(ProfServ.end_dt <= datetime.strptime(form.end_date.data, format))
        return render_template('main/results.html', filtered = filtered) #may change to redirect url_for
    return render_template('main/search.html', depts = depts, types = types, form = form)


# Route to results page, where results of city contracts searching appear
@main.route('/results', methods=['GET', 'POST'])
def results():
    return render_template('main/results.html')

# Route to contact page, where users can contact City Controller's Office
@main.route('/contact')
def contact():
    return render_template('main/contact.html')

# Route to tips page, where users can find search tips
@main.route('/tips')
def tips():
    return render_template('main/tips.html')

# Route to report page, where users can report page
@main.route('/report')
def report():
    return render_template('main/report.html')
