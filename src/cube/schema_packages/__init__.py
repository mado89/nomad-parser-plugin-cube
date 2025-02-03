from nomad.config.models.plugins import SchemaPackageEntryPoint


class CubeEntryPoint(SchemaPackageEntryPoint):

    def load(self):
        from cube.schema_packages.cube import m_package

        return m_package


cube = CubeEntryPoint(
    name='Cube',
    description='Schema package for describing a <please help me what it is>.',
)
