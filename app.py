from flask import *
from model import *

db.connect()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Ceci est un décorateur qui permet d'ajouter une «logique» à différentes
# fonctions sans les modifier directement (sera vu à la fin du cours Python)
def login_required(f):
    def decorated_function(*args, **kwargs):
        # Si l'utilisateur n'est pas loggué => login
        user_id = session.get('user_id')
        if not user_id:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@login_required
@app.route('/')
def index():
    user_id = session.get('user_id')
    if user_id:
        user = User.get(User.id == user_id)
        documents = Document.select()
        return render_template('index.html', user=user, documents=documents)
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        # Soit l'utilisateur existe déjà, soit on le crée dans la foulée
        try:
            user = User.get(User.name == name)
        except:
            user = User.create(name=name)
        session['user_id'] = user.id
        return redirect(url_for('index'))
    else:
        return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

@login_required
@app.route('/add/<int:document_id>', methods=['GET', 'POST'])
def add_document(document_id):
    user_id = session.get('user_id')
    user = User.get(User.id == user_id)
    document = Document.get(Document.id == document_id)
    try:
        ud = UserDocument.get(UserDocument.user_id == user_id, UserDocument.document_id == document_id)
    except:
        UserDocument.create(user=user, document=document)
    return redirect(url_for('index'))

@login_required
@app.route('/remove/<int:document_id>', methods=['GET', 'POST'])
def remove_document(document_id):
    user_id = session.get('user_id')
    user = User.get(User.id == user_id)
    ud = UserDocument.get(UserDocument.user_id == user_id, UserDocument.document_id == document_id)
    ud.delete_instance()
    return redirect(url_for('index'))

@login_required
@app.post('/comment')
def comment_document():
    user_id = session.get('user_id')
    ud_id = request.form.get('ud_id')
    comment = request.form.get('comment')
    ud = UserDocument.get(UserDocument.id == ud_id)
    ud.comment = comment
    ud.save()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
