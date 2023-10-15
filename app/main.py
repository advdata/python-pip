import utils
import read_csv
import charts
import pandas as pd

def run():
  ''' # Estas líneas de código ya no son necesarias porque Pandas hace mejor la consulta (sesde que instalamos Pandas en el directorio app
  data = read_csv.read_csv('data.csv') # Comentada N° 1
  data = list(filter(lambda item : item['Continent'] == 'South America',data)) # Comentada N° 2
  countries = list(map(lambda x: x['Country'], data)) # Comentada N° 3
  percentages = list(map(lambda x: x['World Population Percentage'], data)) # Comentada N° 3
  '''

  df = pd.read_csv('data.csv') # Con esta línea de pandas nos ahorramos la función que creamos en read.csv
  df = df[df['Continent'] == 'Africa'] # Filtrar por continente. Esta línea es equivalente en resultado a la línea arriba Comentada N° 2

  countries = df['Country'].values # Obtener los valores por países. Esta línea es equivalente en resultado a la línea arriba Comentada N° 3

  percentages = df['World Population Percentage'].values # Obtener los porcentajes por países. Esta línea es equivalente en resultado a la línea arriba Comentada N° 4
  charts.generate_pie_chart(countries, percentages)

  data = read_csv.read_csv('data.csv')
  country = input('Type Country => ')
  print(country)

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country'], labels, values)

if __name__ == '__main__':
  run()