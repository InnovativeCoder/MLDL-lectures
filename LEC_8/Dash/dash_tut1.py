import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children =[html.H1('Dash tutorials')])# replace with children =[html.H1('Dash tutorials')]) #H1 tag from html

if __name__ =='__main__':
    app.run_server(debug =True)

#move to second file
