from jinja2 import Template
import datetime

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Auto-EDA Report</title>
<style>
</style>
</head>
<body>
<h1>Auto-EDA Report</h1>
<h3>{{timestamp}} </h3>
<hr>
<h2>Overview</h2>
<ul>{% for k,v in overview.items() %}
    <li><b>{{k}}</b>: {{v}} </li>
    {% endfor %}
</ul>
<h2>Missing Value Percentage (%)</h2>
<ul>{% for k,v in missing_values.items() %}
    <li>{{k}} : {{v}} </li>
    {% endfor %} </ul>
<h2>Visualizations</h2>
<h3>Distributions</h3>
{% for img in dist_plots %}
<img src="{{img}}" />
{% endfor %}
<h3>Boxplots</h3>
{% for img in box_plots %}
<img src="{{img}}" />
{% endfor %}
{% if corr_plot %}
<h3>Correlation Matrix</h3>
<img src="{{corr_plot}}" />
{% endif %}
<h2>Automated Insights</h2>
{% for insight_group in insights %}
{% for key,val in insight_group.items() %}
<div class="insight"><b>{{key}}</b>: {{val}}</div>
{% endfor %}
{% endfor %}
</body>
</html>
"""
def generate_html_report(output_path,**kwargs):
    html = Template(HTML_TEMPLATE).render(**kwargs)
    with open(output_path , "w" , encoding="utf-8") as f:
        f.write(html)
    return output_path