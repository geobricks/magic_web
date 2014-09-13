modules = [
    {
        # The path to the Python file containing the Blueprint
        'module_name': 'magic_modis.rest.rest_modis',
        # The name of the Blueprint
        'rest_name': 'browse_modis',
        # The prefix to be used for the Blueprint
        'url_prefix': '/browse/modis'
    },
    {
        'module_name': 'magic_modis.rest.rest_trmm',
        'rest_name': 'browse_trmm',
        'url_prefix': '/browse/trmm'
    }
]