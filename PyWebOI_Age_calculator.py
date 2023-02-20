from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *
from pywebio import start_server
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

date_today = date.today().strftime("%d/%m/%Y")
date_today = date_today.split("/")
date_today = [int(i) for i in date_today]

def check_form(data):
    if data['date'] > 31 or data['date'] < 1:
        return ('date', 'Date is not valid')
    if data['month'] > 12 or data['month'] < 1:
        return ('month', 'Month is not valid')
    if data['year'] < 1920 or data['year'] > date_today[2]:
        return ('year', 'Year is not valid')

put_html("<h2 align=""left""><h4> AGE CALCULATOR</h4><//h2>")
data = input_group("Enter your date of birthday",[
    input('Date', placeholder="dd", type=NUMBER, name='date'),
    input('Month', placeholder="mm", type=NUMBER, name='month'),
    input('Year', placeholder="yyyy", type=NUMBER, name='year'),
], validate=check_form)

input_date = [data['year'], data['month'], data['date']]
date_today[0], date_today[2] = date_today[2], date_today[0]
popup("your age is ", [put_html("<h4>"f"{relativedelta(datetime.now(),input_date).years} Years</br> \
              {relativedelta(datetime.now(),input_date).months} Months</br>\
              {relativedelta(datetime.now(),input_date).days} Days""</h4>"), put_buttons(
                  ['Close'], onclick=lambda _: close_popup())], implicit_close=True)