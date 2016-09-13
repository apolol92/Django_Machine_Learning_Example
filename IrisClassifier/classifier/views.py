from django.shortcuts import render
from django.views.generic import TemplateView
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
# Create your views here.

class IndexView(TemplateView):
    template_name = "classifier/index.html"

    # display blank form
    def get(self, request):
        if(request.GET.get('sepal_width')):
            df = pd.read_csv("iris.csv")
            X = df.iloc[:,0:4]
            y = df.iloc[:,4]
            neigh = KNeighborsClassifier(n_neighbors=10)
            neigh.fit(X, y)
            pY = neigh.predict([request.GET.get('sepal_length'),request.GET.get('sepal_width'),
            request.GET.get('petal_length'),
            request.GET.get('petal_width')])
            return render(request, self.template_name, {'sepal_length': request.GET.get('sepal_length'),
                                                        'sepal_width': request.GET.get('sepal_width'),
                                                        'petal_length': request.GET.get('petal_length'),
                                                        'petal_width': request.GET.get('petal_width'),
                                                        'predictedLabel':pY
                                                        })
        else:
            return render(request, self.template_name)
