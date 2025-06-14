from milcatrusspy import Model


cercha = Model()

cercha.add_node(1, 0, 0, 0)
cercha.add_node(2, 4, 0, 0)
cercha.add_node(3, 4, 4, 0)
cercha.add_node(4, 0, 4, 0)
cercha.add_node(5, 2, 2, 4)

cercha.add_element(1, 1, 5, 2.1e6, 0.3*0.5)
cercha.add_element(2, 2, 5, 2.1e6, 0.3*0.5)
cercha.add_element(3, 3, 5, 2.1e6, 0.3*0.5)
cercha.add_element(4, 4, 5, 2.1e6, 0.3*0.5)

cercha.set_load(5, fz=-100, fx=10, fy=10)

cercha.set_restraints(1, True, True, True)
cercha.set_restraints(2, True, True, True)
cercha.set_restraints(3, True, True, True)
cercha.set_restraints(4, True, True, True)

cercha.solve()
cercha.print_results()
cercha.plot_model()
cercha.plot_deformed(scale=1000)
cercha.plot_axial_forces(scale=0.01)