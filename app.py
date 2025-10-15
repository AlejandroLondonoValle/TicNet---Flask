from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import random

app = Flask(__name__, template_folder='views')
app.secret_key = ''  # cambia esto en producción

# Usuarios y contraseñas
usuarios_validos = {
    '3229207': '7029223',
    'admin': '1234',
    'alejandro': '1234',
    'nataly': '1234',
    'juan': '1234',
    'alexander' : '1234',
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

# Funcion para validar el usuario
@app.route('/check_user', methods=['POST'])
def check_user():
    data = request.get_json() # Recibe JSON { usuario: 'valor' }
    usuario = data.get('usuario') # Extrae el usuario y lo convierte a un dato mas manejable para python
    if usuario in usuarios_validos:
        return jsonify({'exists': True})
    else:
        return jsonify({'exists': False})
    

# Funcion para validar la contraseña
@app.route('/check_password', methods=['POST'])
def check_password():
    data = request.get_json()
    usuario = data.get('usuario')
    contraseña = data.get('contraseña')

    if usuarios_validos.get(usuario) == contraseña:
        return jsonify({'valid': True})
    else:
        return jsonify({'valid': False})


# Captcha que genera una operación aleatoria y guarda la respuesta en session
@app.route('/generate_captcha', methods=['GET'])
def generate_captcha():
    # Elige un tipo de operación 'compleja' pero que a la vez sea sencilla de calcular
    tipos = ['(a*b)+c', 'a+b-c', 'a*b-c', '(a+b)*c']
    tipo = random.choice(tipos)

    # Generar valores aleatorios para a, b, c según el tipo de operación
    if tipo == '(a*b)+c' or tipo == 'a*b-c':
        a = random.randint(2, 12)
        b = random.randint(2, 12)
        c = random.randint(1, 20)
    else:
        a = random.randint(1, 40)
        b = random.randint(1, 30)
        c = random.randint(1, 10)

    # Construir la pregunta y calcular la respuesta sin usar eval inseguro
    if tipo == '(a*b)+c':
        question = f"¿Cuánto es ({a} × {b}) + {c} ?"
        answer = (a * b) + c
    elif tipo == 'a+b-c':
        question = f"¿Cuánto es {a} + {b} - {c} ?"
        answer = a + b - c
    elif tipo == 'a*b-c':
        question = f"¿Cuánto es {a} × {b} - {c} ?"
        answer = (a * b) - c
    else:  # '(a+b)*c'
        question = f"¿Cuánto es ({a} + {b}) × {c} ?"
        answer = (a + b) * c

    # Guardar la respuesta en la sesión (como string para comparar fácilmente)
    session['captcha_answer'] = str(answer)

    # Retornar la pregunta al cliente
    return jsonify({'question': question})

# Validar el captcha y completar login (form POST)
@app.route('/login_complete', methods=['POST'])
def login_complete():
    usuario = request.form.get('usuario')
    captcha_input = request.form.get('captcha_input', '').strip()

    # Comprobar que tenemos algo guardado en sesión
    expected = session.get('captcha_answer')
    if not expected:
        # No hay captcha generado (posible recarga o expiración de sesión)
        return render_template('login.html', error='No se encontró un CAPTCHA activo. Refresca e intenta de nuevo.')

    # Comparación segura: ambos como string (evita int cast errors) ademas si se equivoca lo saca al inicio otra vez
    if captcha_input != expected:
        return render_template('Index.html', error='Respuesta de CAPTCHA incorrecta. Intenta de nuevo.')

    # Una vez consumido, eliminar la respuesta para que no se vuelva a usar
    session.pop('captcha_answer', None)
    # Login exitoso, guardar usuario en sesión para despues pintarlo en el dashboard
    session['usuario'] = usuario
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', usuario=session['usuario'])

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    # también eliminar captcha si existe
    session.pop('captcha_answer', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
