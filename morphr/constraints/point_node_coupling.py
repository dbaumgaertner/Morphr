import eqlib as eq
import numpy as np
import hyperjet as hj
from morphr.constraints.utility import evaluate_ref, evaluate_act, evaluate_act_2


class PointNodeCoupling(eq.Objective):
    def __init__(self, nodes, shape_functions, target_node, weight):
        eq.Objective.__init__(self)

        self.nodes = nodes
        self.target_node = target_node
        self.shape_functions = np.asarray(shape_functions, float)
        self.weight = weight

        variables = []
        for node in nodes:
            variables += [node.x, node.y, node.z]
        self.variables = variables + [target_node.x, target_node.y, target_node.z]

    def evaluate_act_2(self, index):
        return evaluate_act_2(self.nodes, self.shape_functions[index], self.nb_variables, 0)

    def evaluate_act_target_2(self):
        xyz = np.array(hj.HyperJet.constants(self.nb_variables, self.target_node.act_location))

        xyz[0].g[-3] = 1
        xyz[1].g[-2] = 1
        xyz[2].g[-1] = 1

        return xyz

    def compute(self, g, h):
        location = self.evaluate_act_2(0)
        target = self.evaluate_act_target_2()

        delta = target - location

        p = np.dot(delta, delta) * self.weight / 2

        g[:] = p.g
        h[:] = p.h
        return p.f