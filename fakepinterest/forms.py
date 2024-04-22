from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,FileField
from wtforms.validators import DataRequired,Email,EqualTo,Length,ValidationError
from fakepinterest.models import Usuario

class FormLogin(FlaskForm):
    email=StringField("E-mail",validators=[DataRequired(),Email()])
    senha=PasswordField("Senha",validators=[DataRequired()])
    botao_confirmaçao=SubmitField("Fazer Login")

class FormCriarConta(FlaskForm):
    email=StringField("E-mail",validators=[DataRequired(),Email()])
    username=StringField("Nome de usuário",validators=[DataRequired()])
    senha=PasswordField("Senha",validators=[DataRequired(),Length(8,20)])
    confirmaçao_senha=PasswordField("Confirmação de senha",validators=[DataRequired(),EqualTo("senha")])
    botao_confirmaçao=SubmitField("Criar conta")

    def validate_email(self,email):
        usuario=Usuario.query.filter_by(email=email.data).first()
        if usuario:
            return ValidationError("Já existe uma conta com esse email.Faça login novamente.")

class FormFoto(FlaskForm):
    foto = FileField("Foto", validators=[DataRequired()])
    botao_confirmaçao=SubmitField("Enviar")
