# Documentación de MPTB_vshell

Bienvenido a la documentación técnica de **MPTB_vshell**. Esta guía está diseñada para desarrolladores que deseen entender la arquitectura interna del bot, cómo extender sus funcionalidades y cómo funciona el flujo de datos.

## 🏗️ Arquitectura del Sistema

MPTB_vshell no es un bot de Telegram convencional. Utiliza un diseño modular y asíncrono para maximizar la eficiencia.

### Componentes Principales

1.  **Bot.py (Entry Point)**:
    *   Inicializa la aplicación `python-telegram-bot`.
    *   Carga los módulos dinámicamente.
    *   Inicia el hilo principal de `brain.py`.

2.  **Brain.py (El Cerebro)**:
    *   Es el núcleo lógico del bot.
    *   Contiene el bucle principal (`mainloop`) que procesa las colas de mensajes.
    *   Decide qué hacer con cada mensaje: ¿Es un comando? ¿Es una petición de IA? ¿Es una descarga?
    *   Gestiona la persistencia de la base de datos en un hilo separado (`database_saver`).

3.  **Módulos (Modules/)**:
    *   **core/queues.py**: Define las colas de prioridad para el procesamiento de mensajes. Esto evita que una tarea pesada bloquee a los usuarios ligeros.
    *   **core/commands.py**: Contiene la implementación de todos los comandos (`/start`, `/ls`, etc.).
    *   **entity/**: Define las estructuras de datos como `peer` (usuario) y sus estados.
    *   **gvar.py**: Variables globales y configuración (Tokens, IDs de admin).

### Flujo de Datos

1.  Un usuario envía un mensaje a Telegram.
2.  El `MessageHandler` en `bot.py` captura el evento.
3.  El mensaje se coloca en una cola (`MessageQueue`) en `modules/core/queues.py`.
4.  El `mainloop` en `brain.py` extrae el mensaje de la cola.
5.  Se verifica si el usuario existe en la base de datos (`database.py`); si no, se crea.
6.  Se evalúa el contenido:
    *   Si empieza con `/`, se busca en `COMMANDS` y se ejecuta.
    *   Si no, se envía al módulo de IA (`chatgpt.py`) o se procesa como archivo.

## 💻 Guía de Desarrollo

### Cómo añadir un nuevo comando

1.  Abre `modules/core/commands.py`.
2.  Define una nueva función que acepte `message: Message` como argumento.
    ```python
    def mi_comando(message: Message):
        # Tu lógica aquí
        await_exec(message.reply_text, ["Hola mundo!"])
    ```
3.  Añade tu comando al diccionario `commands` al final del archivo:
    ```python
    commands = {
        # ...
        "/mi_comando": mi_comando
    }
    ```
4.  Reinicia el bot.

### Gestión de Usuarios y Archivos

Cada usuario tiene un directorio asignado en `env/<username>-<id>`.
*   Usa `user.path` para acceder a su directorio raíz.
*   Los comandos `ls`, `mkdir`, `rm` operan sobre este directorio virtual.

### Estados de Usuario

Los usuarios tienen un campo `state` (bitmask) definido en `modules/core/enums.py`.
*   Puedes usar `/su_state` para modificar estos permisos en tiempo de ejecución si eres administrador.
*   Estados comunes: `BANNED`, `ADMIN`, etc.

## 🆘 Solución de Problemas

*   **El bot no responde**: Verifica que `brain.py` esté corriendo y que no haya excepciones en el `mainloop`.
*   **Error de base de datos**: Asegúrate de que `database.csv` tenga permisos de escritura.
*   **OpenAI Error**: Verifica tu `OPEN_AI` key en el archivo `.env`.
