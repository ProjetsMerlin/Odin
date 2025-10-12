{
    'name': 'Odin - Custom Website Theme',
    'version': '1.1.0',
    'summary': 'Odoo + Tailwind theme',
    'category': 'Website/Website',
    'author': 'lintermemdaire.be',
    'license': 'LGPL-3',
    'depends': ['base','website'],
    'data': [
        'security/ir.model.access.csv',
        'views/content.xml',
        'views/odin_layout.xml',
        'views/includes/logo.xml',
        'views/includes/navigation.xml',
        'views/includes/footer.xml',
        'views/includes/about.xml',
        'views/includes/textCenter.xml',
        'views/includes/team.xml',
        'views/includes/contactForm.xml',
        'views/includes/services.xml',
        'views/tankyou.xml',
        'views/page404.xml',
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