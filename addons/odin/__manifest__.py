{
    'name': 'Odin - Custom Website Theme',
    'version': '1.1.0',
    'summary': 'Odoo + Tailwind theme',
    'category': 'Website/Website',
    'author': 'lintermemdaire.be',
    'license': 'LGPL-3',
    'depends': ['website'],
    'data': [
        'views/odin_layout.xml',
        'views/includes/logo.xml',
        'views/includes/navigation.xml',
        'views/includes/about.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            'odin/static/src/css/style.css',
            'https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4',
        ],
    },
    'installable': True,
    'application': False,
}

# ok