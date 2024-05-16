import dash_bootstrap_components as dbc
from dash import html, dcc


def inputs(header, id, placeholder, options, size=2, offset=0, text_align='center',value = None):
    ip = dbc.Col([html.Header(header),
                     dcc.Dropdown(id=id, multi=False, value=value, placeholder=placeholder, optionHeight=20,
                                  options=options,
                                  style={'color': 'black', 'background': 'white'}),
                     ], xl={'size':2,'offset':1},lg={'size':2,'offset':1},md={'size':2,'offset':1},
                    sm={'size':6,'offset':1},xs={'size':6,'offset':1}, style={'text-align': text_align})
    return ip


def selectTime(hour_id, min_id,value=None,value2=None):
    time = dbc.Row([
        dbc.Col([
            dcc.Input(id=hour_id, type='number', placeholder='Hour', min=0, max=23,value=value,style={'width':80}),
            dcc.Input(id=min_id, type='number', placeholder='Minute', min=0, max=59,value=value2,style={'width':80}),
        ])
    ])
    return time

def airlines(x=0):
    airline = ['Air India', 'GoAir', 'IndiGo',
               'Jet Airways', 'Multiple carriers', 'Other',
               'SpiceJet', 'Vistara']

    airline_val = [0, 0, 0, 0, 0, 0, 0, 0]
    if x in airline:
        a = airline.index(x)
        airline_val[a] = 1
    return airline_val

def source(x=0):
    src = ['Chennai','Delhi','Kolkata','Mumbai']
    source_value = [0, 0, 0, 0]
    if x in src:
        a = src.index(x)
        source_value[a] = 1
    return source_value


def destination(x=0):
    dest = ['Cochin', 'Delhi', 'Hyderabad','Kolkata','New Delhi']
    dt_value = [0, 0, 0, 0,0]
    if x in dest:
        a = dest.index(x)
        dt_value[a] = 1
    return dt_value


def dateFormat(x):
    import datetime
    ip = x
    ft = '%Y-%m-%d'
    datetime = datetime.datetime.strptime(ip, ft)
    return [ datetime.date().month, datetime.date().day, datetime.date().isocalendar().week]


def fClass(x):
    cls =  ['Business','First','Economy']
    if x == 'Business': return 2
    elif x == 'First': return 1
    else : return 0

def ArivalTime(dep_h,dep_m,trav_h,trav_m):
    from datetime import datetime, timedelta
    datetimeOrg = datetime(2022, 6, 6, dep_h, dep_m)
    timeDelta = timedelta(hours=trav_h, minutes=trav_m)
    newDatetime = datetimeOrg + timeDelta
    arrivTime = [newDatetime.hour,newDatetime.minute]
    return arrivTime