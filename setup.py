# from setuptools import setup

# setup(
#     name='milcatrusspy',
#     version='0.1.1',
#     packages=['milcatrusspy'],
#     description='Librería para el análisis de estructuras (Truss).',
#     long_description=open('README.md', encoding='utf-8').read(),
#     long_description_content_type='text/markdown',
#     author='Amilcar',
#     author_email='200190@unsaac.edu.pe',
#     url='https://github.com/Milca-py/milcatrusspy',
#     install_requires=[
#         'numpy',
#         'pandas',
#         'matplotlib',
#     ],
# )






from milcatrusspy import Model

cercha = Model()

nodes = [
    [1, 0, 0, 0],
    [2, 0, 0, 4],
    [3, 4, 0, 4],
    [4, 4, 0, 0],
    [5, 0, 4, 0],
    [6, 0, 4, 4],
    [7, 4, 4, 4],
    [8, 4, 4, 0],
    [9, 0, 8, 0],
    [10, 0, 8, 4],
    [11, 4, 8, 4],
    [12, 4, 8, 0]
]

elements = [
    [1, 1, 2, 2100000.0, 0.15],
    [2, 2, 3, 2100000.0, 0.15],
    [3, 3, 4, 2100000.0, 0.15],
    [4, 4, 1, 2100000.0, 0.15],
    [5, 5, 6, 2100000.0, 0.15],
    [6, 6, 7, 2100000.0, 0.15],
    [7, 7, 8, 2100000.0, 0.15],
    [8, 8, 5, 2100000.0, 0.15],
    [9, 9, 10, 2100000.0, 0.15],
    [10, 10, 11, 2100000.0, 0.15],
    [11, 11, 12, 2100000.0, 0.15],
    [12, 12, 9, 2100000.0, 0.15],
    [13, 1, 5, 2100000.0, 0.15],
    [14, 2, 6, 2100000.0, 0.15],
    [15, 3, 7, 2100000.0, 0.15],
    [16, 4, 8, 2100000.0, 0.15],
    [17, 5, 9, 2100000.0, 0.15],
    [18, 6, 10, 2100000.0, 0.15],
    [19, 7, 11, 2100000.0, 0.15],
    [20, 8, 12, 2100000.0, 0.15],
    [21, 1, 6, 2100000.0, 0.15],
    [22, 4, 7, 2100000.0, 0.15],
    [23, 6, 9, 2100000.0, 0.15],
    [24, 7, 12, 2100000.0, 0.15]
]

for (tag, x, y, z) in nodes:
    cercha.add_node(tag, x, y, z)

for (tag, tag_node_i, tag_node_j, E, A) in elements:
    cercha.add_element(tag, tag_node_i, tag_node_j, E, A)

for i in range(1, 5):
    cercha.set_restraints(i, True, True, True)

cercha.set_load(10, fz=-10)
cercha.set_load(11, fz=-10)

cercha.solve()
nodes, elements = cercha.get_results()
cercha.print_results()
cercha.plot_model(labels=True)
cercha.plot_deformed(scale=500, labels=False)
cercha.plot_axial_forces(0.05, labels=False)
cercha.plot_reactions()