## Project setup

Project setup instructions here.

```bash
mkdir -p local
cp todo_app/project/settings/templates/settings.dev.py ./local/settings.dev.py
cp todo_app/project/settings/templates/settings.unittests.py ./local/settings.unittests.py
```

```bash
make shell

#from todo_app.config.models import Config
#Config.objects.create(owner=None, transaction_fee=1)
```

### Main Dependencies:

Python (^3.9): The programming language used for developing the Django application. It provides the core functionality
and syntax for writing Python code.

Django (^4.2): A high-level web framework that simplifies the development of complex web applications. It provides
features such as URL routing, model-view-controller (MVC) architecture, database abstraction, and authentication.

Django REST Framework (^3.14.0): A powerful and flexible toolkit for building Web APIs in Django. It includes
serialization, authentication, permission handling, and pagination features.

Psycopg2 (^2.9.6): A PostgreSQL adapter for Python, allowing Django to interact with PostgreSQL databases.

Django Filter (^23.2): A reusable Django application for creating filters for querysets. It simplifies the process of
filtering and searching data in Django views.

Django Split Settings (^1.2.0): A library that allows you to split your Django settings into multiple files for better
organization and management.

PyYAML (^6.0): A YAML parser and emitter for Python. It enables reading and writing YAML files, which can be useful for
configuration and data storage.

Django CORS Headers (^3.14.0): A Django application that adds Cross-Origin Resource Sharing (CORS) headers to responses.
It allows your API to be accessed from different domains.

Pydantic (^1.10.7): A runtime type-checking and validation library for Python. It provides tools for defining and
validating data structures, which can be useful for API input/output validation.

PyNaCl (^1.5.0): A Python binding to the Networking and Cryptography (NaCl) library. It provides easy-to-use
cryptographic functionality for secure communication.

Django REST Framework SimpleJWT (^5.2.2): A JSON Web Token (JWT) authentication plugin for Django REST Framework. It
enables authentication using JWT tokens.

Channels (^4.0.0): A Django library that extends the capabilities of Django to handle WebSocket communication and
real-time applications. It allows bidirectional communication between clients and the server.

Django Model Utils (^4.3.1): A collection of utilities for Django models, including abstract models, mixins, and model
field utilities.

Whitenoise (^6.4.0): A Django middleware for serving static files efficiently. It improves performance by caching static
files and serving them directly.

Pillow (^9.5.0): A Python Imaging Library (PIL) fork that provides image processing capabilities. It is commonly used
for image manipulation, resizing, and generating thumbnails.

Django Storages (^1.13.2): A collection of storage backends for Django, including support for storing files on remote
services like AWS S3.

Boto3 (^1.26.137): The AWS SDK for Python. It provides an easy-to-use interface for interacting with various AWS
services, such as S3 for file storage.

Pytest (^7.3.1): A testing framework for Python. It allows you to write test cases and run them easily. It provides
features such as test discovery, fixtures, and assertions.

Pytest xdist (^3.3.1): A plugin for Pytest that enables parallel test execution across multiple CPUs or machines. It can
significantly speed up the test execution process.

Pytest Django (^4.5.2): A Pytest plugin that provides useful fixtures and configuration for testing Django applications.

Model Bakery (^1.11.0): A library for creating model instances in Django tests. It simplifies the process of creating
test data by automatically populating fields with realistic values.

### Development Dependencies:

Pre-commit (^3.3.1): A framework for managing and maintaining multi-language pre-commit hooks. It allows you to enforce
code formatting, linting, and other checks before committing code.

Colorlog (^6.7.0): A Python library that adds color to log output. It provides a colorful and readable log format for
better debugging and readability.

Django Debug Toolbar (^4.1.0): A Django extension that displays various debugging information in the browser toolbar. It
helps in profiling, identifying performance issues, and debugging Django applications.


