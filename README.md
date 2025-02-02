
# FAQ API (bharatFD)

This project provides a RESTful API for managing Frequently Asked Questions (FAQs) with multilingual support using Django and Django REST Framework. The FAQs are stored in a database and can be retrieved in different languages using Google Translate. The project also uses Redis for caching.

## Installation

### Prerequisites

- Docker
- Docker Compose

### Key Features:
- **Multilingual Support:** FAQs can be retrieved in different languages (English, Hindi, Bengali) using Google Translate.
- **Caching:** FAQs are cached in Redis for 15 minutes to improve performance.
- **Admin Interface:** Django admin interface is available for managing FAQs with rich text support using CKEditor.

The project uses the following technologies:

- **Django:** Web framework for building the FAQ API.
- **Django REST Framework:** Toolkit for building Web APIs.
- **Docker:** Containerization platform to package the application.
- **Docker Compose:** Tool for defining and running multi-container Docker applications.
- **Redis:** In-memory data structure store used for caching FAQs.
- **Google Translate:** Service for translating FAQs into different languages.
- **CKEditor:** Rich text editor for the Django admin interface.
- **Python:** Programming language used for the application logic.


### Steps

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/faq-api.git
    cd faq-api
    ```

2. Build and start the Docker containers:

    ```sh
    docker-compose up --build
    ```

3. Apply database migrations:

    ```sh
    docker-compose exec web python manage.py migrate
    ```

4. Create a superuser to access the Django admin:

    ```sh
    docker-compose exec web python manage.py createsuperuser
    ```



5. Access the application at `http://localhost:8000`.

## API Usage

### List FAQs

- **URL:** `/api/faqs/`
- **Method:** GET
- **Query Parameters:**(optional): The language code for translation (default is `en`).

#### Example Request

```sh
curl -X GET "http://localhost:8000/api/faqs/"
```

#### Example Response

```json
[
    {
        "question": "What is your name?",
        "answer": "My name is John Doe."
    }
]
```

### List FAQs in Hindi

- **URL:** `/api/faqs/?lang=hi`
- **Method:** GET

#### Example Request

```sh
curl -X GET "http://localhost:8000/api/faqs/?lang=hi"
```

#### Example Response

```json
[
    {
        "question": "आपका नाम क्या है?",
        "answer": "मेरा नाम जॉन डो है।"
    }
]
```

### List FAQs in Bengali

- **URL:** `/api/faqs/?lang=bn`
- **Method:** GET

#### Example Request

```sh
curl -X GET "http://localhost:8000/api/faqs/?lang=bn"
```

#### Example Response

```json
[
    {
        "question": "তোমার নাম কি?",
        "answer": "আমার নাম জন ডো।"
    }
]
```

## Additional Notes

- The FAQs are cached in Redis for 15 minutes to improve performance.
- The project uses Google Translate for translating FAQs into different languages.
- The admin interface is available at `http://localhost:8000/admin/` for managing FAQs.

