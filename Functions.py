
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import warnings

import profiler as profiler

warnings.filterwarnings('ignore')


# import geopandas as gpd

def remove_null(dataframe):
    """
        This function takes dataframe to remove the Nan values from the specific column name
        param1: The dataframe for whose column we want to remove Nan's from

        return: The dataframe with no Nan values in the specific column

        >>> df = pd.DataFrame([[1, None, 3], [ 1, 3, 6 ], [4, 5, None]])
        >>> new_df = remove_null(df)
        >>> new_df
           0    1    2
        1  1  3.0  6.0
    """

    dataframe = dataframe.dropna()
    return dataframe

def replace_values(dataframe, values_dict, column_name):
    """
    This function takes dataframe and the dictionary containing the specific column that we want to update the values of
    param1: The dataframe for whose columns we want to rename
    param2: A dictionary containing the orginal column values and the new values as the key value pair
    param3: The column name of the dataframe whose values we want to update

    return: The dataframe with updated values in tha particular column

    >>> df = pd.DataFrame([[1, 'MP', 'InDIA'], [ 2, 'Colombo', 'Sri LANKA']], columns = ['ID', 'State', 'Country'])
    >>> column_name = 'Country'
    >>> values_dict = {"InDIA": "India", "Sri LANKA" : "Sri Lanka"}
    >>> column_name = 'Country'
    >>> new_df = replace_values(df, values_dict, column_name)
    >>> new_df
       ID    State    Country
    0   1       MP      India
    1   2  Colombo  Sri Lanka
    """
    dataframe[column_name] = dataframe[column_name].replace(values_dict, regex=True)
    return dataframe

def rename_columns(dataframe, column_dict):
    """
    This function takes dataframe and the dictionary containing the specific column that we want to update the values of
    param1: The dataframe for whose columns we want to rename
    param2: A dictionary containing the orginal column name and the new name as the key value pair

    return: The dataframe with updated column name

    >>> df = pd.DataFrame([[1, 'MP', 'InDIA'], [ 2, 'Colombo', 'Sri LANKA']], columns = ['ID', 'STAte', 'COUnTRy'])
    >>> column_dict = {"COUnTRy": "Country", "STAte" : "State"}
    >>> new_df = rename_columns(df, column_dict)
    >>> new_df
       ID    State    Country
    0   1       MP      InDIA
    1   2  Colombo  Sri LANKA
    """
    dataframe.rename(columns=column_dict, inplace=True)
    return dataframe

def plot_world_map(dataframe):
    """
    This function is used to display the world map and it gives us the breakdown of internet usage all over the world.
    The countries with darker shades have higher internet usage compared to countries with lighter shade.

    param : dataframe
    return: plot
    """
    variable = "2017"
    vmin, vmax = 120, 220

    # Create colorbar as a legend
    sm = plt.cm.ScalarMappable(cmap="PuRd", norm=plt.Normalize(vmin=vmin, vmax=vmax))
    # Empty array for the data range
    sm._A = []

    fig = dataframe.plot(column=variable, cmap="Blues", figsize=(20, 20))

    plt.title("Internet Usage over the world")
    # try adding interactivity
    return fig

def plot_bar_graph(x, y, title, x_label, y_label):
    """
    This function the x and y co-ordinates to plot a bar graph
    param1: The dataframe for whom we want to plot bar graph
    param2: The value for the x co-ordinate
    param3: The value for the y co-ordinate
    param4: The title of the bar graph
    param5: The x_label of the bar graph
    param6: The y_label of the bar graph

    return: The bar graph plot

    """

    fig, ax = plt.subplots(figsize=(15, 5))
    frequency = y
    points = x
    ax.bar(points, frequency)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    return plt

def scatter_plot(dataframe, x, y, color, size, hover_name, log_x, size_max):
    """
    This function is used to plot a scatter plot for the GDP of a country against the average internet usage over the years.

    param : Dataferame

    return: scatter plot
    >>> plot = pd.DataFrame([["Afghanistan",5.594427,"Afghanistan",623.2,35530.0],["Yemen",14.887779,"Yemen",1106.4,28250.0]],columns=["Country","Average Internet usage over the years","country","GDP per capita (current US$)","Population in thousands (2017)"])
    >>> x= "GDP per capita (current US$)"
    >>> y= "Average Internet usage over the years"
    >>> color= "Country"
    >>> size= "Average Internet usage over the years"
    >>> name="country"
    >>> log_x=True
    >>> size_max=60
    >>> scatter_plot(plot,x, y, color, size, name, log_x, size_max)
    Figure({
        'data': [{'hovertemplate': ('<b>%{hovertext}</b><br><br>Cou' ... '=%{marker.size}<extra></extra>'),
                  'hovertext': array(['Afghanistan'], dtype=object),
                  'legendgroup': 'Afghanistan',
                  'marker': {'color': '#636efa',
                             'size': array([5.594427]),
                             'sizemode': 'area',
                             'sizeref': 0.0041354941666666666,
                             'symbol': 'circle'},
                  'mode': 'markers',
                  'name': 'Afghanistan',
                  'showlegend': True,
                  'type': 'scatter',
                  'x': array([623.2]),
                  'xaxis': 'x',
                  'y': array([5.594427]),
                  'yaxis': 'y'},
                 {'hovertemplate': ('<b>%{hovertext}</b><br><br>Cou' ... '=%{marker.size}<extra></extra>'),
                  'hovertext': array(['Yemen'], dtype=object),
                  'legendgroup': 'Yemen',
                  'marker': {'color': '#EF553B',
                             'size': array([14.887779]),
                             'sizemode': 'area',
                             'sizeref': 0.0041354941666666666,
                             'symbol': 'circle'},
                  'mode': 'markers',
                  'name': 'Yemen',
                  'showlegend': True,
                  'type': 'scatter',
                  'x': array([1106.4]),
                  'xaxis': 'x',
                  'y': array([14.887779]),
                  'yaxis': 'y'}],
        'layout': {'legend': {'itemsizing': 'constant', 'title': {'text': 'Country'}, 'tracegroupgap': 0},
                   'margin': {'t': 60},
                   'template': '...',
                   'xaxis': {'anchor': 'y',
                             'domain': [0.0, 1.0],
                             'title': {'text': 'GDP per capita (current US$)'},
                             'type': 'log'},
                   'yaxis': {'anchor': 'x', 'domain': [0.0, 1.0], 'title': {'text': 'Average Internet usage over the years'}}}
    })
    """
    fig = px.scatter(dataframe, x=x, y=y,
                     color=color, size=size,
                     hover_name=hover_name, log_x=log_x, size_max=size_max)

    return fig

def data_breach_plot(dataframe, x, y):
    """
    This function is used to create a scatter plot for no. of data breaches, against the average internet usage.

    param : dataframe

    return: scatter plot
    """
    fig = px.scatter(dataframe, x=x, y=y)

    return fig

def plot_treemap(dataframe, path, values, color, hover_data, color_continuous_scale):
    """
    This function is used to create a treemap for the no.of secure servers in a country against the no. of data breaches.

    param : dataframe
    return : treemap plot

    """
    fig = px.treemap(dataframe, path=path, values=values,
                     color=color, hover_data=hover_data,
                     color_continuous_scale=color_continuous_scale)
    return fig

def check_correlation(dataframe, col_list):
    """
    This function is designed to check the correlation between two columns of a dataframe
    param1: The dataframe for whose column we need to check the correlation
    param2: A list of columns to check the correlation in

    return: The correlation value
    >>> df = pd.DataFrame([['Afghanistan', 'AFG',2017.0, 27.22, 13.50], ['Albania', 'ALB', 2017.0, 23.78, 71.85], ['Algeria', 'DZA', 2017.0, 34.02, 47.69]], columns = ['country', 'Code', 'Year' , '% of Depressed People', '% of Internet Users'])
    >>> col_list = ['% of Depressed People', '% of Internet Users']
    >>> corr_value = check_correlation(df, col_list)
    >>> corr_value
    -0.23523022161905166
    """

    corr_value = dataframe[col_list[0]].corr(dataframe[col_list[1]], method="pearson")

    return corr_value

# shapefile = 'C:/Users/Acer/Desktop/final_project_2020Sp/110m_cultural/ne_110m_admin_0_countries.shp'
# Read shapefile using Geopandas
# gdf = gpd.read_file(shapefile)[['ADMIN', 'ADM0_A3', 'geometry']]

