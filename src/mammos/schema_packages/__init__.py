from nomad.config.models.plugins import SchemaPackageEntryPoint


class CubeEntryPoint(SchemaPackageEntryPoint):

    def load(self):
        from cube.schema_packages.cube import m_package

        return m_package


cube = CubeEntryPoint(
    name='Cube',
    description='Schema package for describing a <please help me what it is>.',
)

class TmrEntryPoint(SchemaPackageEntryPoint):

    def load(self):
        from cube.schema_packages.tmrshape import m_package

        return m_package


tmr = TmrEntryPoint(
    name='B4Vex Simulation',
    description='Schema package for describing a B4Vex Simulation.',
)

class OntoEntryPoint(SchemaPackageEntryPoint):

    def load(self):
        from cube.schema_packages.mammos_ontology import m_package

        return m_package


onto = OntoEntryPoint(
    name='Onto',
    description='Schema package for Mammos.',
)

class UUEntryPoint(SchemaPackageEntryPoint):

    def load(self):
        from cube.schema_packages.uu_schema import m_package

        return m_package


uu = UUEntryPoint(
    name='uu',
    description='Schema package for UU data.',
)
