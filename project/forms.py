from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, IntegerField
from wtforms.validators import InputRequired, NumberRange, DataRequired

class WalkForm(FlaskForm):
    direct = SelectField("Куда идем: ",
                         coerce = int,
                         choices=[
                             (0,'Север'),
                             (1,'Юг'),
                             (2,'Восток'),
                             (3,'Запад'),
                         ],
                         render_kw={
                             'class':'form-control'
                         },
                         )
    step = IntegerField(
        'На сколько клеток?',
        validators=[NumberRange(min=1), DataRequired()],
        default=1,
        render_kw={
            'class': 'form-control'
        },
    )
    '''
    escape = SelectField("В какой клетке выход?",
                         coerce=int,
                         choices=[],
                         render_kw={
                             'class': 'form-control'
                         },
                         )
                         '''
    submit = SubmitField("Принять")

class CreateForm(FlaskForm):
    height = IntegerField(
        'Высота поля',
        validators=[NumberRange(min=1), DataRequired()],

        render_kw={
            'class':'form-control'
        },
    )
    width = IntegerField(
        'Ширина поля',
        validators=[NumberRange(min=1), DataRequired()],

        render_kw={
            'class': 'form-control'
        },
    )


    submit = SubmitField("Создать")
