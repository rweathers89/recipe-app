# src/recipes/utils.py
from recipes.models import Recipe   #you need to connect parameters from books model
from io import BytesIO 
import base64
import matplotlib.pyplot as plt

#define a function that takes the ID
def get_recipename_from_id(val): 
    #this ID is used to retrieve the name from the record
    recipename=Recipe.objects.get(id=val)
    #and the name is returned back 
    return recipename


def get_graph():
    #create a BytesIO buffer for the image
    buffer = BytesIO()          

    #create plot with bytesIO object as a file-like object. Set format to png
    plt.savefig(buffer, format='png') 

    #set cursor to the beginning of the stream
    buffer.seek(0)

    #retrieve the content of the file
    image_png=buffer.getvalue()

    #encode the bytes-like object
    graph=base64.b64encode(image_png)

    #decode to get the string as output
    graph=graph.decode('utf-8')

    #free up the memory of buffer
    buffer.close()

    #return the image/graph
    return graph

#chart_type: user input o type of chart,
#data: pandas dataframe
def get_chart(chart_type, data, **kwargs):
    #switch plot backend to AGG (Anti-Grain Geometry) - to write to file
    #AGG is preferred solution to write PNG files
    plt.switch_backend('AGG')

    #specify figure size
    fig=plt.figure(figsize=(10,6))

    # Counting the number of ingredients for each recipe
    data['number_ingredients'] = data['ingredients'].apply(lambda x: len(x.split(',')))

    #select chart_type based on user input from the form
    if chart_type == '#1':
       #plot bar chart between name on x-axis and cooking time on y-axis
       plt.bar(data['name'], data['cooking_time'])
       plt.xlabel('Recipe Name')
       plt.ylabel('Cooking Time in minutes')
       plt.title('Recipes by Cooking Time')
       plt.xticks(rotation=65)

    elif chart_type == '#2':
        #generate pie chart based on difficulty.
        #The recipe titles are sent from the view as labels
        difficulty_counts = data['difficulty'].value_counts()
        labels=difficulty_counts.index
        values=difficulty_counts.values
        plt.pie(values, labels=labels)
        plt.title('Recipes by Difficulty')
        plt.xticks(rotation=65)

    elif chart_type == '#3':
        #plot line chart based on recipe name on x-axis and number of ingredients on y-axis
        plt.plot(data['name'], data['number_ingredients'])
        plt.xlabel('Recipe Name')
        plt.ylabel('Number of Ingredients')
        plt.title('Recipes by Number of Ingredients')
        plt.xticks(rotation=65)
        
    else:
        print ('unknown chart type')

    #specify layout details
    plt.tight_layout()

    #render the graph to file
    chart =get_graph() 
    return chart         