# MPTB_vhsell

**MPTB_vhsell** es una nueva versión modular de un bot de Telegram escrita en Python. Está diseñado para ser extensible, eficiente y fácil de mantener, utilizando una arquitectura basada en colas y procesamiento asíncrono.

## 🚀 Características

- **Modularidad**: Código organizado en módulos independientes para facilitar la escalabilidad.
- **Concurrencia**: Uso de hilos y colas (`MessageQueue`, `Pool`) para manejar múltiples tareas simultáneamente sin bloquear el bot.
- **Integración con IA**: Soporte nativo para integración con modelos de lenguaje (como ChatGPT) para responder mensajes.
- **Gestión de Archivos**: Comandos inspirados en shell para gestionar archivos y subidas.
- **Persistencia**: Sistema de base de datos (SQLite) y gestión de entidades de usuario.

## 📋 Requisitos

- Python 3.8 o superior.
- Una cuenta de Telegram y un Bot Token (obtenido de @BotFather).
- Claves de API opcionales para funcionalidades de IA (OpenAI).

## 🛠️ Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/VIRUSGAMING64/MPTB_vhsell.git
   cd MPTB_vhsell
   ```

2. **Instalar dependencias:**
   (Asegúrate de tener un entorno virtual activo)
   ```bash
   pip install -r requirements.txt
   ```
   *Nota: Si no existe el archivo `requirements.txt`, instala las librerías principales manualmente: `python-telegram-bot`, `requests`, `openai`, etc.*

3. **Configuración:**
   Crea un archivo `.env` en la raíz del proyecto o configura las variables de entorno en tu sistema:
   ```env
   TOKEN=tu_token_de_telegram
   API_HASH=tu_api_hash
   API_ID=tu_api_id
   OPEN_AI=tu_api_key_openai
   ```

## ▶️ Uso

Para iniciar el bot, ejecuta el script principal:

```bash
python bot.py
```

### Comandos Básicos
- `/start`: Inicia la interacción con el bot.
- `/kill`: Detiene el proceso del bot.
- `/upload`: (En desarrollo) Sube archivos al servidor.
- Comandos de sistema: `ls`, `rm`, `mkdir`, etc. (según implementación).

## 📂 Estructura del Proyecto

- `bot.py`: Punto de entrada.
- `modules/`: Contiene la lógica del negocio.
  - `brain.py`: Orquestador de tareas.
  - `chatgpt.py`: Integración con IA.
  - `core/`: Componentes del núcleo (manejadores, colas, comandos).
  - `entity/`: Definiciones de objetos de usuario/peer.
  - `utils.py`: Utilidades generales (barras de progreso, manejo de loops).

## 📚 Documentación

Para más detalles técnicos, consulta la documentación en la carpeta `docs/`:
- [Inicio](docs/index.html)
- [Módulos](docs/modules.html)
- [Instalación Detallada](docs/setup.html)
