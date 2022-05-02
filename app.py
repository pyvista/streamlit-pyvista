import streamlit as st
import streamlit.components.v1 as components
from ipywidgets import embed
from pyvista.jupyter.pv_pythreejs import convert_plotter


def pyvista_streamlit(plotter):
    grid = convert_plotter(plotter)
    snippet = embed.embed_snippet(views=grid)
    html = embed.html_template.format(title="", snippet=snippet)
    components.html(html, width=900, height=500)


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
