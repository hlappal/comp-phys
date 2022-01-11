from IPython.display import HTML
from IPython.display import Video
from numpy import pi

def play_lazy_man():

 return HTML("""
 <video  controls id="lazyman" width="500" height="500">
 <source src="./lazy_man.mp4">
 </video>

 <script>
 video = document.getElementById("lazyman")
 video.playbackRate = 2.0;
 </script>
 """)


def play_H2O_on_Pt():
  return HTML("""
  <video  controls id="H2OPt" width="500" height="500">
  <source src="./H2O_on_Pt.mp4">
  </video>

  <script>
  video = document.getElementById("H2OPt")
  video.playbackRate = 2.0;
  </script>
  """)

def play_VelocityVerlet(): 
 return HTML("""
 <video  controls id="vverlet" width="500" height="500">
 <source src="./VelocityVerlet.mp4">
 </video>

 <script>
 video = document.getElementById("vverlet")
 video.playbackRate = 2.0;
 </script>
 """)


