# 🧭 Sistema de Ubicación para Zonas Públicas WIFI

Este proyecto es una aplicación web desarrollada con **Python (Flask)** y **Bootstrap**, que permite a los usuarios **iniciar sesión de forma segura** mediante un proceso de validación por etapas (usuario → contraseña → captcha).
El sistema incluye un **captcha casero dinámico**, que genera una operación matemática aleatoria cada vez que se carga la página, garantizando una capa adicional de seguridad sin depender de servicios externos como Google reCAPTCHA.

---

## 🚀 Características principales

* ✅ **Interfaz moderna y responsive** gracias a **Bootstrap 5**.
* 🔐 **Login paso a paso:** primero valida el usuario, luego la contraseña y finalmente el captcha.
* 🔢 **Captcha matemático autogenerado**, que cambia al recargar la página.
* 💬 **Mensajes dinámicos** de validación con alertas visuales.
* 🧩 **Desarrollado completamente en Flask**, sin dependencias externas de JavaScript para la lógica principal.
* 🏠 **Página de bienvenida personalizada** (Dashboard) que saluda al usuario por su nombre.

---

## 🧰 Tecnologías utilizadas

* **Python 3.8+**
* **Flask**
* **HTML5**
* **Bootstrap 5**
* **Jinja2 (para plantillas dinámicas)**

---

## ⚙️ Instalación y configuración

Sigue estos pasos para ejecutar el proyecto en tu entorno local:

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/tuusuario/sistema-zonas-wifi.git
cd sistema-zonas-wifi
```

### 2️⃣ Crear un entorno virtual

```bash
python -m venv venv
```

### 3️⃣ Activar el entorno virtual

* **Windows:**

  ```bash
  venv\Scripts\activate
  ```
* **Linux/Mac:**

  ```bash
  source venv/bin/activate
  ```

### 4️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```


### 5️⃣ Ejecutar el servidor

```bash
python app.py
```

Luego abre tu navegador en:
👉 `http://127.0.0.1:5000`

---

## 👥 Flujo del sistema

1. El usuario accede al **login principal**.
2. Ingresa su **nombre de usuario**.

   * Si existe, se muestra el campo de **contraseña**.
3. Si la contraseña es correcta, aparece el **captcha matemático**.
4. Si el captcha se resuelve correctamente, el sistema redirige al **dashboard**, mostrando un mensaje de bienvenida personalizado.

---

## 🧩 Estructura del proyecto

```
📁 TicNet
│
├── 📄 app.py              # Lógica principal de Flask
├── 📄 requirements.txt    # Dependencias del proyecto
│
├── 📁 views/          
   ├── index.html
   ├── login.html
   └── dashboard.html

```

---

## 🧑‍💻 Autor

**Luis Alejandro Londoño Valle**
Desarrollador de software especializado en **C#, .NET, y Flask (Python)**
📍 Medellín, Colombia
🔗 [GitHub](https://github.com/AlejandroLondonoValle) · [LinkedIn](www.linkedin.com/in/luís-alejandro-londoño-valle)

---

## 💡 Notas adicionales

* Asegúrate de **mantener tu `secret_key` segura** dentro del archivo `app.py`.
* Este proyecto puede servir como base para sistemas más grandes (por ejemplo, **portales gubernamentales**, **sistemas de autenticación por etapas**, o **plataformas educativas seguras**).

---
