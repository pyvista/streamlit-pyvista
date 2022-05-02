import io

import streamlit as st
import streamlit.components.v1 as components
from ipywidgets import embed
import pyvista as pv
from pyvista.jupyter.pv_pythreejs import convert_plotter

pv.start_xvfb()

pv.set_plot_theme('document')


def pyvista_streamlit(plotter):
    widget = convert_plotter(plotter)
    state = embed.dependency_state(widget)
    fp = io.StringIO()
    embed.embed_minimal_html(fp, None, title="", state=state)
    fp.seek(0)
    snippet = fp.read()
    components.html(snippet, width=900, height=500)


with st.echo():
    import pyvista as pv
    from pyvista import examples

    # Example dataset with normals
    mesh = examples.load_random_hills()

    # create a subset of arrows using the glyph filter
    arrows = mesh.glyph(scale="Normals", orient="Normals", tolerance=0.05)

    p = pv.Plotter()
    p.add_mesh(arrows, color="black")
    p.add_mesh(mesh, scalars="Elevation", cmap="terrain", smooth_shading=True)

    pyvista_streamlit(p)
