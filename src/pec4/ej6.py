import folium
import pandas as pd

def plot_choropleth(df: pd.DataFrame, save_path: str = '') -> folium.Map:
    """
    Crea un mapa coroplético que muestra permit_perc, handgun_perc y longgun_perc en Estados Unidos utilizando folium

    Parámetros:
        df: Dataframe con datos de permit_perc, handgun_perc y longgun_perc y con los
        códigos de los estados almacenados en un campo 'code'
        save_path: Cadena de caracteres indicando la ruta donde se va a guardar el mapa y su nombre.
                   Es un parámetro opcional

    Returns:
        folium.Map: mapa coroplético
    """
    state_geo = 'https://raw.githubusercontent.com/python-visualization/folium/main/examples/data/us-states.json'
    target_labels = {
        'permit_perc': 'Permisos de armas',
        'handgun_perc': 'Solicitudes de pistolas',
        'longgun_perc': 'Solicitudes de rifles'
    }
    colors = {
        'permit_perc': 'YlGn',
        'handgun_perc': 'BuPu',
        'longgun_perc': 'OrRd'
    }

    m = folium.Map(location=[40, -95], zoom_start=4)

    for target in target_labels.keys():
        folium.Choropleth(
            geo_data=state_geo,
            name=target_labels[target],
            data=df,
            columns=['code', target],
            key_on="feature.id",
            fill_color=colors[target],
            fill_opacity=0.5,
            line_opacity=.1,
            legend_name=f"{target_labels[target]} como % de la población estatal",
        ).add_to(m)

    folium.LayerControl().add_to(m)

    if save_path != '':
        m.save(save_path)

    return m