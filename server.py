import wtforms
from flask import Flask, request, render_template
from wtforms import validators

from main import solve_square_equation

app = Flask(__name__)
template = "main.html"


class EquationForm(wtforms.Form):
    a = wtforms.FloatField('A', validators=[validators.DataRequired()])
    b = wtforms.FloatField('B', validators=[validators.DataRequired()])
    c = wtforms.FloatField('C', validators=[validators.DataRequired()])


@app.route('/', methods=['GET', 'POST'])
def solve_equation():
    form = EquationForm(request.form)
    if request.method == "POST":
        a = form.a.data
        b = form.b.data
        c = form.c.data
        result = solve_square_equation(a, b, c)
        return render_template(template, form=form, result=result)
    return render_template(template, form=form)


if __name__ == '__main__':
    app.run()
