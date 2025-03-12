from typing import (
  TYPE_CHECKING,
)

import numpy as np
from nomad.datamodel.data import (
  ArchiveSection,
  EntryData,
)
from nomad.metainfo import (
  Package,
  Quantity,
  Section,
  SubSection,
)

from MagneticMaterialsOntology import MagnetocrystallineAnisotropyConstantK1

if TYPE_CHECKING:
  from nomad.datamodel.datamodel import (
      EntryArchive,
  )
  from structlog.stdlib import (
      BoundLogger,
  )

m_package = Package(name='Schema for UU data')
m_package.__init_metainfo__()

class UUData(EntryData, ArchiveSection):
  m_def = Section()

  k1 = SubSection(
    section_def=MagnetocrystallineAnisotropyConstantK1,
    repeats = False,
  )

  data_file = Quantity(
    type=str,
    description='A test.',
    a_eln={
        "component": "FileEditQuantity",
    },
  )

  def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
    '''
    The normalizer for the `UU data`.

    Args:
        archive (EntryArchive): The archive containing the section that is being
        normalized.
        logger (BoundLogger): A structlog logger.
    '''
    super().normalize(archive, logger)
