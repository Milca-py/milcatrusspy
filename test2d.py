from milcatrusspy import Model

cercha = Model(2)

cercha.add_node(1, 0, 0)
cercha.add_node(2, 0, 4)
cercha.add_node(3, 4, 0)
cercha.add_node(4, 4, 4)
cercha.add_node(5, 8, 0)
cercha.add_node(6, 8, 4)

cercha.add_element(1, 1, 2, 2.1e6, 0.3*0.5)
cercha.add_element(2, 1, 4, 2.1e6, 0.3*0.5)
cercha.add_element(3, 1, 3, 2.1e6, 0.3*0.5)
cercha.add_element(4, 2, 4, 2.1e6, 0.3*0.5)
cercha.add_element(5, 3, 4, 2.1e6, 0.3*0.5)
cercha.add_element(6, 3, 5, 2.1e6, 0.3*0.5)
cercha.add_element(7, 4, 5, 2.1e6, 0.3*0.5)
cercha.add_element(8, 4, 6, 2.1e6, 0.3*0.5)
cercha.add_element(9, 5, 6, 2.1e6, 0.3*0.5)

cercha.set_restraints(1, True, True)
cercha.set_restraints(2, True, True)

cercha.set_load(6, fy=-10)

cercha.solve()
nodes, elements = cercha.print_results()
cercha.plot_model()
cercha.plot_deformed(500)
cercha.plot_forces(0.05)
cercha.plot_reactions()

