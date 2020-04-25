import morphr as mo

import anurbs as an
import eqlib as eq
import numpy as np

SHELL_3P = mo.Shell3P


class ApplyShell3P(mo.Task):
    thickness: float
    youngs_modulus: float
    poissons_ratio: float
    weight: float = 1

    def run(self, config, job, data, log):
        cad_model = data.get('cad_model', None)
        model_tolerance = job.model_tolerance

        nb_conditions = 0

        # FIXME: Check for None

        data['nodes'] = data.get('nodes', {})
        elements =[]

        thickness = self.thickness
        youngs_modulus = self.youngs_modulus
        poissons_ratio = self.poissons_ratio

        for key, face in cad_model.of_type('BrepFace'):
            surface_geometry_key = surface_geometry = face.surface_geometry.data

            if surface_geometry_key not in data['nodes']:
                nodes = []

                for x, y, z in surface_geometry.poles:
                    nodes.append(eq.Node(x, y, z))
                nodes = np.array(nodes, object)
                data['nodes'][surface_geometry_key] = nodes
            else:
                nodes = data['nodes'][surface_geometry_key]

            for u, v, weight in an.integration_points(face, model_tolerance):
                nonzero_indices, shape_functions = surface_geometry.shape_functions_at(u, v, 2)

                element = SHELL_3P(nodes[nonzero_indices], thickness, youngs_modulus, poissons_ratio)
                element.add(shape_functions, weight)
                elements.append(element)

                nb_conditions += 1

        data['elements'] = data.get('elements', [])
        data['elements'].append(('Shell3P', elements, self.weight))

        # output

        log.info(f'{nb_conditions} new conditions')
