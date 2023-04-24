import pandas as pd
import matplotlib.pyplot as plt
from iertools.read import read_sql
from dateutil.parser import parse
import numpy as np
import matplotlib.dates as mdates


def import_dat(file):
    analisis = read_sql(file)
    nombres = {'Environment:Site Outdoor Air Drybulb Temperature (C)': 'To',
     'Environment:Site Outdoor Air Relative Humidity (%)': 'hr',
     'Environment:Site Wind Speed (m/s)': 'ws',
     'Environment:Site Wind Direction (deg)': 'wd',
     'THERMAL ZONE 1:Zone Mean Air Temperature (C)': 'Ti_THERMALZONE1',
     'THERMAL ZONE 1:Zone Mean Air Humidity Ratio (kgWater/kgDryAir)': 'wi_THERMALZONE1',
     'THERMAL ZONE 1:AFN Zone Infiltration Volume (m3)': "Infiltration_Volume",
     'THERMAL ZONE 1:Zone Air Relative Humidity (%)': 'rhi_THERMALZONE1',
     "THERMAL ZONE 1:Zone Outdoor Air Wind Speed (m/s)": "ws_zone",
      "THERMAL ZONE 1:Zone Outdoor Air Wind Direction (deg)":"wd_zone",
              }
    analisis.rename(columns=nombres)
    data =analisis.data
    return data



def graph_general(fecha1,timedelta,data, ylim, area = None):
    fecha1 = parse(fecha1)
    fecha2 = fecha1 + pd.Timedelta(timedelta)

    def formato(ax, titulo):
        ax.set_title(titulo)
        ax.legend()
        ax.set_xlim(fecha1,fecha2)

    if area == None:
        sale1       = data["VENTANA_ESTE:AFN Linkage Node 1 to Node 2 Volume Flow Rate (m3/s)"]
        entra1      = data["VENTANA_ESTE:AFN Linkage Node 2 to Node 1 Volume Flow Rate (m3/s)"]
        sale2       = data["VENTANA_OESTE:AFN Linkage Node 1 to Node 2 Volume Flow Rate (m3/s)"]
        entra2      = data["VENTANA_OESTE:AFN Linkage Node 2 to Node 1 Volume Flow Rate (m3/s)"]
        label_entra = "Linkage in-window [m3/s]"
        label_sale  = "Linkage out-window [m3/s]"

    else:
        sale1  = data["VENTANA_ESTE:AFN Linkage Node 1 to Node 2 Volume Flow Rate (m3/s)"]/area
        entra1 = data["VENTANA_ESTE:AFN Linkage Node 2 to Node 1 Volume Flow Rate (m3/s)"]/area
        sale2  = data["VENTANA_OESTE:AFN Linkage Node 1 to Node 2 Volume Flow Rate (m3/s)"]/area
        entra2 = data["VENTANA_OESTE:AFN Linkage Node 2 to Node 1 Volume Flow Rate (m3/s)"]/area
        label_entra = "Linkage in-window [m/s]"
        label_sale  = "Linkage out-window [m/s]"



    fig, ax = plt.subplots(3,2, figsize=(15,6), sharex=True)

    ax[0][0].plot(data.To, "b.", label="outdoors")
    ax[0][0].plot(data.Ti_THERMALZONE1, "r", label="Zone")
    formato(ax[0][0], "Temperature [°C]")
    if ylim[0] != None:
        ax[0][0].set_ylim(ylim[0][0], ylim[0][1])

    ax[0][1].plot(data.hr, "b.", label="outdoors")
    ax[0][1].plot(data.rhi_THERMALZONE1, "r", label="Zone")
    formato(ax[0][1], "Humidity [%]")
    if ylim[1] != None:
        ax[0][1].set_ylim(ylim[1][0], ylim[1][1])

    ax[1][0].plot(data.ws,"b.", label="outdoors")
    ax[1][0].plot(data.ws_zone, "r", label="Zone")
    formato(ax[1][0], "Wind speed [m/s]")
    if ylim[2] != None:
        ax[1][0].set_ylim(ylim[2][0], ylim[2][1])

    ax[1][1].plot(data.wd,"b.", label="outdoors")
    ax[1][1].plot(data.wd_zone,"r", label="Zone")
    formato(ax[1][1], "Wind direction [°]")
    if ylim[3] != None:
        ax[1][1].set_ylim(ylim[3][0], ylim[3][1])

    ax[2][0].plot(sale2,"b.", label="out")
    ax[2][0].plot(entra2, label="in")
    formato(ax[2][0], label_entra)
    if ylim[4] != None:
        ax[2][0].set_ylim(ylim[4][0], ylim[4][1])

    ax[2][1].plot(sale1,"b.", label="out")
    ax[2][1].plot(entra1, label="in")
    formato(ax[2][1], label_sale)
    if ylim[5] != None:
        ax[2][1].set_ylim(ylim[5][0], ylim[5][1])
