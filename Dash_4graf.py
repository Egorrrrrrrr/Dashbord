import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Загрузка данных
df = pd.read_csv(r'C:\Users\Admin\PycharmProjects\pythonProject\TextFile1.csv')

# Создание экземпляра приложения
app = dash.Dash(__name__)

# Определение структуры дашборда
app.layout = html.Div([
    html.Div([
        html.H1('Дашборд анализа данных о состоянии продаж услуг автосервиса', style={'textAlign': 'center'}),
        html.P('Этот дашборд предоставляет информацию об услугах сервиса, их стоимости и количества проданных услуг.',
               style={'textAlign': 'center'}),
        html.Div([
            html.Label('Отзыв:', style={'fontSize': 18}),
            dcc.Dropdown(
                id='date-dropdown',
                options=[{'label': date, 'value': date} for date in df['отзыв']],
                value=df['отзыв'].iloc[0],
                clearable=False,
                style={'width': '50%', 'margin': '0 auto'}
            ),
        ], style={'textAlign': 'center', 'marginBottom': '30px'}),
    ], style={'marginBottom': '30px'}),


    html.Div([
        # Ящик с усами
        dcc.Graph(id='box-plot'),
    ], style={'width': '48%', 'display': 'inline-block'}),



], style={'padding': '20px'})

# Определение логики дашборда
@app.callback(

    Output('box-plot', 'figure'),

    [Input('date-dropdown', 'value')]
)
def update_charts(selected_date):


    # Boxplot
    box_plot = px.box(df, x='Тип_услуги', y='колво_проданных',
                      title='Boxplot')


    return box_plot

# Запуск приложения
if __name__ == '__main__':
    app.run_server(debug=True)