
from js import document

# Template HTML con placeholder
def render_template(template, **context):
    """
    Simula un motore di template semplice.
    :param template: Template HTML come stringa con {{variabili}}
    :param context: Variabili da passare al template
    :return: Stringa HTML renderizzata
    """
    # Sostituzione delle variabili {{ ... }}
    for key, value in context.items():
        if isinstance(value, dict):  # Gestisce i dizionari per liste dinamiche
            list_items = "".join(
                f"<li>{k}: {v}</li>" for k, v in value.items()
            )
            template = template.replace(
                "{% for key, value in data.items() %}{{ key }}: {{ value }}{% endfor %}", 
                list_items
            )
        else:
            template = template.replace(f"{{{{ {key} }}}}", str(value))
    
    return template
    
template_html = """
<div>
    <h1>{{ title }}</h1>
    <p>{{ description }}</p>
    <ul>
        {% for key, value in data.items() %}
        <li>{{ key }}: {{ value }}</li>
        {% endfor %}
    </ul>
</div>
"""

# Funzione per "renderizzare" il contenuto
def render_content():
    # Definizione dei dati da passare al template
    context = {
        "title": "Benvenuti nella mia applicazione!",
        "description": "Questo è un esempio di rendering di template in PyScript.",
        "data": {
            "Python": "Eccellente",
            "JavaScript": "Ottimo",
            "HTML": "Indispensabile"
        }
    }

    # Renderizza il template
    rendered_html = render_template(template_html, **context)

    # Inserisci il risultato nel DOM
    content_div = document.getElementById('content')
    content_div.innerHTML = rendered_html

# Collega la funzione al caricamento della pagina
document.addEventListener("DOMContentLoaded", render_content())
