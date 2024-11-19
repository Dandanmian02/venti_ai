from glob import glob

from streamlit_image_viewer import image_viewer

import streamlit as st

st.title("ImageViewer App_test")
st.title("Images")
image_path_list = glob('./images/vent.png') + glob("./images/paimeng.png") 
image_viewer(image_path_list, ncol=3, nrow=2, key="image_viewer")

image_viewer(
    image_path_list: List[str],
    ncol: int = 2,
    nrow: int = 2,
    image_name_visible: bool = True
    key: Optional[str] = None
)
