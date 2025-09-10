import json

PROMPT_TMPL = """
Eres un analista de datos experto.
Recibirás: (1) esquema de columnas (nombre, tipo, nulos), (2) shape, (3) describe numérico y (4) top categorías.
Devuelve de 3 a 5 visualizaciones útiles en JSON (sin comentarios), arreglo de objetos con claves exactas:
- title
- chart_type oneof [bar, line, pie, scatter, area]
- parameters (ej: {"x_axis":"Col","y_axis":"Valor","group_by":"OtraCol","agg":"sum"})
- insight (breve)

Datos:
{data}
"""

def suggest_charts(llm_client, schema_summary: dict) -> list[dict]:
    prompt = PROMPT_TMPL.format(data=json.dumps(schema_summary, ensure_ascii=False))
    # Conecta aquí tu proveedor LLM si lo deseas.
    return [
        {
            "title": "Distribución de Ventas por Región",
            "chart_type": "bar",
            "parameters": {"x_axis":"Region","y_axis":"Ventas","agg":"sum"},
            "insight": "Resalta las regiones con mayor contribución total."
        },
        {
            "title": "Tendencia Mensual de Ventas",
            "chart_type": "line",
            "parameters": {"x_axis":"Mes","y_axis":"Ventas","agg":"sum"},
            "insight": "Permite ver estacionalidad y crecimientos."
        },
        {
            "title": "Top 10 Productos por Ingreso",
            "chart_type": "bar",
            "parameters": {"x_axis":"Producto","y_axis":"Ingresos","agg":"sum"},
            "insight": "Identifica productos estrella."
        }
    ]
