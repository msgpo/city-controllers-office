from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

import csv
import datetime

from flask_rq import get_queue

from app import db
from app.models import ProfServ, Profit_Status, Exempt_Status

contract = Blueprint('ProfServ', __name__)

def readCSV(filename):

    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        next(csvReader)
        i = 1;
        for row in csvReader:
            #if int(row[12]) == 102:
            #    exstat = Exempt_Status.EXEMPT
            #    advext = Exempt_Status.EXEMPT
            #else:
            #    exstat = Exempt_Status.ADVERTISED
            #    advext = Exempt_Status.ADVERTISED
            if row[14] == 'For Profit':
                profstat = Profit_Status.For_Profit
            else:
                profstat = Profit_Status.Non_Profit
            contract = ProfServ(
                id = i,
                original_contract_id = row[0],
                current_item_id = row[1],
                department_name = row[2],
                vendor = row[3],
                contract_structure_type = row[4],
                short_desc = row[5],
                start_dt = datetime.datetime.strptime(row[6], '%m/%d/%Y').date(),
                end_dt = datetime.datetime.strptime(row[7], '%m/%d/%Y').date(),
                days_remaining = int(row[8]),
                amt = float(row[9]),
                tot_payments = float(row[10]),
                orig_vendor = row[11],
                exempt_status = row[12],
                adv_or_exempt = row[13],
                profit_status = profstat
            )
            db.session.add(contract)
            db.session.commit()
            i += 1;
