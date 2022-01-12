import numpy as np
import nibabel as nib
from matplotlib import pyplot as plt
import plotly.express as px


#affiche la k ième tranche de l'image 3D
def show_img(np_img,k):
   plt.figure()
   plt.imshow(np_img[:, :, k], cmap='gray')
   plt.show()
   return None


#affiche les différentes tranches de l'image
def show_img3D(np_img):
   fig = px.imshow(np_img.T, animation_frame=0, binary_string=True, labels=dict(animation_frame="slice"))
   fig.show()

def slice_img3D(np_img, title):
   fig = px.imshow(np_img.T, animation_frame=0, binary_string=True, labels=dict(animation_frame="slice"))
   fig.update_xaxes(
      visible=False,
   )

   fig.update_yaxes(
      visible=False,
   )
   fig.update_layout(

      dragmode=False,
      title={
         'text': title,
         'x': 0.5,
         'y': 0.27
         }
   )

   return fig


