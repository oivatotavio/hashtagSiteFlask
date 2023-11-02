from fakepinterest import database, app
from fakepinterest.models import Usuario, Foto

with app.app_context():
    database.create_all()

# em 30/10/2023 eu tentei rodar esse arquivo e deu um erro porque uma atualização
# do flask quebrou o flask-login, a solução era instalar uma versão mais nova do
# flask-login do repositorio github, porque a versão do pypi estava desatualizada
# o comando era: pip install git+https://github.com/maxcountryman/flask-login.git


# as vezes as coisas quebram, são concertadas no github, mas o repositorio "oficial" não
# implementa as alterações rápido o bastante no pypi, e uma alternativa é buscar no github do projeto
# há de se considerar isso quando o erro surgir