# 1. Basic Diagram

from diagrams import Diagram

def simple_diagram():
    with Diagram("Simple Website Diagram") as diag:
        pass
    print(diag) # This will illustrate the diagram if you are using a Google Colab or Jypiter notebook.


simple_diagram()
