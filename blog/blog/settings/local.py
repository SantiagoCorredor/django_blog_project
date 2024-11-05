from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DB_NAME'),
        'USER': get_secret('USER'),
        'PASSWORD': get_secret('PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')

#ckeditor settings
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            # Herramientas agrupadas según tus necesidades
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript'],
            ['NumberedList', 'BulletedList', 'Outdent', 'Indent'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Table', 'HorizontalRule', 'SpecialChar'],
            ['Source', 'Maximize'],
            ['Format', 'Font', 'FontSize'],
            ['TextColor', 'BGColor'],
            ['Blockquote', 'HorizontalRule', 'PageBreak'],
            ['Undo', 'Redo'],  # Deshacer y rehacer
            ['SelectAll', 'RemoveFormat'],  # Seleccionar todo y eliminar formato
            ['ShowBlocks', 'About'],  # Mostrar bloques y sobre el editor
            ['SpecialChar', 'Table'],
            ['InsertPre', 'CodeSnippet'],  # Código preformateado y snippets de código
            ['CopyFormatting', 'PasteText', 'PasteFromWord'],  # Copiar formato, pegar texto y pegar de Word
        ],
        'height': 300,
        'width': 'auto',
        'toolbarCanCollapse': True,
        'mathJaxLib': 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML',
        'extraPlugins': ','.join([
            'uploadimage',
            'image2',
            'widget', 'lineutils', 'codesnippet',
            'mathjax',
            # Se quitaron los plugins problemáticos
            # 'autosave',  # Comentado para evitar el error 404
            # 'uploadfile',  # Comentado para evitar el error 404
            # 'fontawesome',  # Comentado para evitar el error 404
            # 'emoji',  # Comentado para evitar el error 404
        ]),
        'removePlugins': 'elementspath',  # Opcional: elimina la ruta de elementos del editor
        'filebrowserBrowseUrl': '/path/to/browse/',  # Personaliza la URL del explorador de archivos
        'filebrowserUploadUrl': '/path/to/upload/',  # Personaliza la URL de carga de archivos
        'allowedContent': True,  # Permite cualquier contenido
        'autoGrow_onStartup': True,  # Habilita el crecimiento automático del editor
        'autoGrow_minHeight': 200,  # Altura mínima del editor
        'autoGrow_maxHeight': 600,  # Altura máxima del editor
        'disableNativeSpellChecker': False,  # Habilita el corrector ortográfico nativo
    }
}


# EMAIL SETTINGS
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = get_secret('EMAIL')
# EMAIL_HOST_PASSWORD = get_secret('PASS_EMAIL')
# EMAIL_PORT = 587