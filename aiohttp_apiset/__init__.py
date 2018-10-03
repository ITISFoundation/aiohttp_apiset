from .swagger.router import SwaggerRouter
from .views import ApiSet

try:
    from .version import __version__
except ImportError:
    __version__ = '0.0.0-dev'


__all__ = [
    'ApiSet',
    'SwaggerRouter',
]
