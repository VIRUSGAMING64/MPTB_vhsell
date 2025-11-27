# 🤖 MPTB_vshell

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue?style=for-the-badge&logo=python)
![Telegram Bot API](https://img.shields.io/badge/Telegram-Bot%20API-blue?style=for-the-badge&logo=telegram)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/status-Active-success?style=for-the-badge)

**MPTB_vshell** es una versión avanzada y modular de un bot de Telegram desarrollado en Python. Su arquitectura está diseñada para ser **extensible**, **eficiente** y **fácil de mantener**, utilizando un sistema robusto de colas y procesamiento asíncrono para manejar múltiples tareas simultáneamente.

---

## ✨ Características Principales

*   **🧩 Arquitectura Modular**: El código está desacoplado en módulos independientes (`brain`, `core`, `entity`, etc.), lo que facilita la escalabilidad y el mantenimiento.
*   **⚡ Alta Concurrencia**: Implementa `MessageQueue` y `Pool` junto con hilos (`threading`) para procesar mensajes, descargas y subidas sin bloquear el hilo principal del bot.
*   **🧠 Integración con IA**: Soporte nativo para modelos de lenguaje (como ChatGPT/OpenAI) para respuestas inteligentes y contextuales.
*   **📂 Sistema de Archivos Virtual**: Comandos estilo shell (`ls`, `mkdir`, `rm`) para gestionar archivos y directorios dentro del entorno del bot.
*   **💾 Persistencia de Datos**: Sistema de base de datos personalizado y gestión de estados de usuario persistentes.
*   **🛡️ Gestión de Usuarios**: Sistema de administración con capacidades de baneo, promoción a admin y gestión de estados (`su_state`).

---

## 📋 Requisitos Previos

*   **Python 3.8** o superior.
*   Una cuenta de **Telegram** y un **Bot Token** (consíguelo en [@BotFather](https://t.me/BotFather)).
*   (Opcional) **API Key de OpenAI** para las funciones de IA.

---

## 🛠️ Instalación y Configuración

Sigue estos pasos para poner en marcha tu propio bot:

### 1. Clonar el Repositorio
```bash
git clone https://github.com/VIRUSGAMING64/MPTB_vshell.git
cd MPTB_vshell
```

### 2. Configurar el Entorno Virtual (Recomendado)
```bash
python -m venv env
source env/bin/activate  # En Linux/Mac
# .\env\Scripts\activate # En Windows
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```
> *Si no tienes un archivo `requirements.txt`, asegúrate de instalar: `python-telegram-bot`, `openai`, `requests`.*

### 4. Configuración de Variables de Entorno
Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```env
TOKEN=tu_token_de_telegram_aqui
API_HASH=tu_api_hash_de_telegram
API_ID=tu_api_id_de_telegram
OPEN_AI=tu_api_key_de_openai
```

---

## ▶️ Uso

Para iniciar el bot, simplemente ejecuta el script principal:

```bash
python bot.py
```

El bot iniciará los hilos de procesamiento y conectará con la API de Telegram. Los administradores configurados recibirán un mensaje de notificación de inicio.

---

## 🎮 Comandos Disponibles

| Comando | Descripción | Ejemplo |
| :--- | :--- | :--- |
| **/start** | Inicia la interacción con el bot. | `/start` |
| **/help** | Muestra la ayuda y comandos disponibles. | `/help` |
| **/ls** | Lista archivos y directorios en tu espacio de trabajo. | `/ls` |
| **/mkdir** | Crea un nuevo directorio. | `/mkdir nueva_carpeta` |
| **/rm** | Elimina un archivo o directorio (o por índice). | `/rm archivo.txt` |
| **/getid** | Obtiene tu ID de usuario de Telegram. | `/getid` |
| **/su_state** | (Admin) Cambia el estado de un usuario. | `/su_state <user_id> <state>` |
| **/banuser** | (Admin) Banea a un usuario del bot. | `/banuser <user_id>` |
| **/kill** | (Admin) Detiene el proceso del bot remotamente. | `/kill` |

---

## 📂 Estructura del Proyecto

```text
MPTB_vshell/
├── bot.py              # 🚀 Punto de entrada principal
├── modules/            # 🧠 Lógica del negocio y módulos
│   ├── brain.py        # Orquestador principal de tareas
│   ├── chatgpt.py      # Integración con OpenAI
│   ├── database.py     # Manejo de base de datos
│   ├── core/           # Núcleo (comandos, colas, handlers)
│   ├── entity/         # Definiciones de entidades (User, Peer)
│   └── utils.py        # Utilidades y helpers
├── docs/               # 📚 Documentación detallada
├── env/                # 📦 Almacenamiento de usuarios (generado)
└── README.md           # 📄 Este archivo
```

## 📚 Documentación

Para una guía más profunda sobre la arquitectura y cómo extender el bot, consulta la documentación en la carpeta `docs/`.

*   [Guía de Desarrollo y Arquitectura](docs/index.md)

---

## 🤝 Contribución

¡Las contribuciones son bienvenidas! Por favor, abre un *issue* para discutir cambios mayores antes de enviar un *pull request*.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
