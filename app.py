from pyodide import create_proxy
from js import document

# Template HTML con placeholder
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
document.addEventListener("DOMContentLoaded", create_proxy(render_content))
