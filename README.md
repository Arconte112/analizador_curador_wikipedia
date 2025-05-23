# Wikipedia Content Analyzer & Curator

## Descripción del Proyecto

Wikipedia Content Analyzer & Curator es una aplicación web full-stack que permite a los usuarios buscar artículos en Wikipedia, ver un resumen procesado y un análisis básico del contenido (conteo de palabras, palabras más frecuentes), y guardar los artículos de interés para referencia futura.

El objetivo es proporcionar una herramienta para explorar y curar contenido de Wikipedia de manera eficiente.

## Stack Tecnológico

*   **Frontend:** Next.js (TypeScript, Tailwind CSS)
*   **Backend:** FastAPI (Python)
*   **Base de Datos:** PostgreSQL
*   **Interacción con Wikipedia:** Librería `wikipedia-api` y `requests` (para búsqueda).
*   **Análisis de Texto:** NLTK (Natural Language Toolkit)

## Decisiones de Diseño

*   **Arquitectura Full-Stack:** Separación clara entre el frontend (presentación y experiencia de usuario) y el backend (lógica de negocio, interacción con la base de datos y servicios externos).
*   **API RESTful:** El backend expone una API RESTful para que el frontend consuma los datos.
*   **Componentes Reutilizables:** El frontend se construye con componentes reutilizables para mantener un código limpio y modular.
*   **Manejo de Estado:** Se utiliza el estado local de los componentes de React (`useState`, `useEffect`) para la gestión del estado en el frontend.
*   **ORM:** SQLAlchemy se utiliza en el backend para la interacción con la base de datos PostgreSQL, facilitando las operaciones CRUD.
*   **Validación de Datos:** Pydantic se usa en el backend para la validación de datos de entrada y salida de la API.
*   **Entorno Virtualizado:** Se utiliza un entorno virtual de Python (`venv`) para gestionar las dependencias del backend.

## Instrucciones de Configuración y Ejecución

### Prerrequisitos

*   Node.js (v18.x o superior recomendado)
*   Python (v3.9 o superior recomendado)
*   PostgreSQL server instalado y corriendo.

### 1. Clonar el Repositorio (Si aplica)

```bash
# git clone <repository-url>
# cd analizador_curador_wikipedia
```

### 2. Configuración del Backend

*   **Navegar al directorio del backend:**
    ```bash
    cd backend
    ```
*   **Crear y activar el entorno virtual:**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Linux/macOS
    source venv/bin/activate
    ```
*   **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
    (Si `requirements.txt` no está actualizado, puedes instalar las dependencias directamente como se hizo en el plan: `pip install fastapi uvicorn[standard] sqlalchemy psycopg2-binary python-dotenv wikipedia-api requests pydantic[email] nltk`)
*   **Descargar recursos de NLTK (si no se hizo automáticamente):**
    Ejecutar el script `temp_nltk_download.py` o el código Python para descargar `stopwords` y `punkt` para español.
*   **Configurar variables de entorno:**
    *   Copiar `backend/.env.example` a `backend/.env`.
    *   Editar `backend/.env` con tus credenciales reales de la base de datos PostgreSQL. Asegúrate de que la base de datos especificada en `DATABASE_URL` exista en tu servidor PostgreSQL.
        ```
        DATABASE_URL=postgresql://TU_USUARIO:TU_CONTRASEÑA@TU_HOST:TU_PUERTO/NOMBRE_BD
        # Ejemplo: postgresql://user:password@localhost:5432/wikipedia_analyzer_db
        ```
*   **Ejecutar el servidor del backend:**
    Desde el directorio raíz del proyecto (`analizador_curador_wikipedia`):
    ```bash
    # Windows
    backend\venv\Scripts\uvicorn.exe main:app --reload --app-dir backend --port 8000
    # Linux/macOS (asegúrate que uvicorn esté en el PATH del venv o usa python -m uvicorn ...)
    # python -m uvicorn main:app --reload --app-dir backend --port 8000
    ```
    El backend estará disponible en `http://localhost:8000`. La base de datos se inicializará (creará las tablas) al arrancar la aplicación.

### 3. Configuración del Frontend

*   **Navegar al directorio del frontend:**
    Desde el directorio raíz del proyecto (`analizador_curador_wikipedia`):
    ```bash
    cd frontend/frontend_app
    ```
*   **Instalar dependencias (si no se hizo durante la creación con `create-next-app`):**
    ```bash
    npm install
    ```
*   **Configurar variables de entorno del frontend:**
    El archivo `frontend/frontend_app/.env.local` ya debería estar configurado con:
    ```
    NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
    ```
    Asegúrate que este URL coincida con donde está corriendo tu backend.
*   **Ejecutar el servidor de desarrollo del frontend:**
    Desde el directorio `frontend/frontend_app`:
    ```bash
    npm run dev
    ```
    El frontend estará disponible en `http://localhost:3000`.

## Definición de Endpoints API

La documentación interactiva de la API está disponible a través de Swagger UI cuando el backend está corriendo, en la siguiente URL:

*   **`http://localhost:8000/docs`**

Principales Endpoints:

### Wikipedia (`/api/v1/wikipedia`)

*   **`GET /search`**: Busca artículos en Wikipedia.
    *   Query Params: `term: str` (término de búsqueda)
    *   Respuesta: `WikipediaSearchResult` (lista de sugerencias)
*   **`GET /article-details`**: Obtiene detalles y análisis de un artículo.
    *   Query Params: `title: str` (título exacto del artículo)
    *   Respuesta: `ArticleDetail`

### Artículos Guardados (`/api/v1/saved-articles`)

*   **`POST /`**: Guarda un nuevo artículo.
    *   Request Body: `SavedArticleCreate`
    *   Respuesta: `SavedArticleInDB`
*   **`GET /`**: Obtiene una lista de artículos guardados.
    *   Query Params: `skip: int = 0`, `limit: int = 100`
    *   Respuesta: `List[SavedArticleInDB]`
*   **`GET /{article_id}`**: Obtiene un artículo guardado específico por su ID.
    *   Path Params: `article_id: int`
    *   Respuesta: `SavedArticleInDB`
*   **`PUT /{article_id}`**: Actualiza un artículo guardado (uso limitado en este proyecto).
    *   Path Params: `article_id: int`
    *   Request Body: `SavedArticleUpdate`
    *   Respuesta: `SavedArticleInDB`
*   **`DELETE /{article_id}`**: Elimina un artículo guardado.
    *   Path Params: `article_id: int`
    *   Respuesta: `SavedArticleInDB` (el artículo eliminado)

---

Este proyecto fue desarrollado como una demostración.
