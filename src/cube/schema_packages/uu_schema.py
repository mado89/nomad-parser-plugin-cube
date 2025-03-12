from typing import (
  TYPE_CHECKING,
)

import numpy as np
import os
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
from nomad.units import ureg

from .mammos_ontology import MagnetocrystallineAnisotropyConstantK1

if TYPE_CHECKING:
  from nomad.datamodel.datamodel import (
      EntryArchive,
  )
  from structlog.stdlib import (
      BoundLogger,
  )

m_package = Package(name='Schema for UU data')
m_package.__init_metainfo__()

def find_line_val_dict(fileName, valname, verbose=False):
  """
  Find last line in lines (list) with valname (string) and
  return a dict of IDs and valuse coming after valname
  """
  # Check if file exists
  if not os.path.isfile(fileName):
    raise FileNotFoundError(f"The file '{fileName}' does not exist.")

  with open(fileName, 'rt') as f:
    lines = f.read().splitlines()

  if verbose:
      print(lines)

  last_lines_with_valname = {}
  for line in lines:
    if valname in line:
      if verbose:
          print(line)
      pos = line.find(valname) + len(valname)
      # TODO: check if part of the line can be converted to float; introduce boundaries in which the value should be
      key, value = line.split()[0], [float(x)
                                      for x in line[pos:].split()]
      last_lines_with_valname[key] = value
  return last_lines_with_valname

def compute_magnetizationW(tot_moments_D, dir_of_JD, file_Name_Ms):
  """
  Calculating total magnetic moment by summing all

  (Total moment (of an orbital) * Direction of J (takes the one with abs value > 0.9, should be +/-1))
  """
  tot_magn_mom_C = 0
  for key in tot_moments_D.keys():
    tot_magn_mom_C += tot_moments_D[key][0]*[x for x in dir_of_JD[key] if abs(x) > 0.9][0]

  # Getting unit cell volume in A^3 from the file
  ucvA = get_unit_cell_volume(file_Name_Ms)
  print(f'Unit cell volume: {ucvA} A\N{SUPERSCRIPT THREE}')

  # Calculating magnetization in Tesla
  magnetization_in_T = tot_magn_mom_C/ucvA*11.654

  return magnetization_in_T, ucvA

def compute_magnetization(tot_moments_D, dir_of_JD, lines):
  """
  Calculating total magnetic moment by summing all

  (Total moment (of an orbital) * Direction of J (takes the one with abs value > 0.9, should be +/-1))
  """
  tot_magn_mom_C = 0
  for key in tot_moments_D.keys():
    tot_magn_mom_C += tot_moments_D[key][0]*[x for x in dir_of_JD[key] if abs(x) > 0.9][0]

  # Getting unit cell volume in A^3 from the file
  ucvA = get_unit_cell_volume(lines)
  print(f'Unit cell volume: {ucvA} A\N{SUPERSCRIPT THREE}')

  # Calculating magnetization in Tesla
  magnetization_in_T = tot_magn_mom_C/ucvA*11.654

  return magnetization_in_T, ucvA

def get_unit_cell_volumeW(file_name):
    """
    Extracts the unit cell volume from the given file.
    :param file_name: The name of the file to extract the unit cell volume from.
    :return: The unit cell volume in cubic angstroms (A^3).
    """
    ucv = find_line_val_dict(file_name, 'unit cell volume:')
    ucvA = ucv[list(ucv.keys())[0]][0] / 1.8897259**3  # unit cell volume in A^3
    return ucvA

def get_unit_cell_volume(lines):
    """
    Extracts the unit cell volume from the given file.
    :param file_name: The name of the file to extract the unit cell volume from.
    :return: The unit cell volume in cubic angstroms (A^3).
    """
    ucv = lastThingy(lines, 'unit cell volume:')
    ucvA = ucv[list(ucv.keys())[0]][0] / 1.8897259**3  # unit cell volume in A^3
    return ucvA

def lastThingy(lines, valname,verbose=False):
  last_lines_with_valname = {}
  for line in lines:
    if valname in line:
      if verbose:
          print(line)
      pos = line.find(valname) + len(valname)
      # TODO: check if part of the line can be converted to float; introduce boundaries in which the value should be
      key, value = line.split()[0], [float(x)
                                      for x in line[pos:].split()]
      last_lines_with_valname[key] = value
  return last_lines_with_valname

class GroundState(ArchiveSection):
  m_def = Section()
  out_MF_x = Quantity(
    type=str,
    description='The \'out_MF_x\' file.',
    a_eln={
        "component": "FileEditQuantity",
    },
  )
  out_MF_y = Quantity(
    type=str,
    description='The \'out_MF_y\' file.',
    a_eln={
        "component": "FileEditQuantity",
    },
  )
  out_MF_z = Quantity(
    type=str,
    description='The \'out_MF_z\' file.',
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

    logger.info(f'Normalising groundstate able?:{self.out_MF_x and self.out_MF_y and self.out_MF_z}, {self.out_MF_x} {self.out_MF_y} {self.out_MF_z}')
    energies = {}
    if self.out_MF_x and self.out_MF_y and self.out_MF_z:
      with archive.m_context.raw_file(self.out_MF_x) as file:
        lines = file.read().splitlines()

      eigenvalue_sum = lastThingy(lines, 'Eigenvalue sum:')
      energies['x'] = eigenvalue_sum[list(eigenvalue_sum.keys())[0]][0]

      with archive.m_context.raw_file(self.out_MF_y) as file:
        lines = file.read().splitlines()

      eigenvalue_sum = lastThingy(lines, 'Eigenvalue sum:')
      energies['y'] = eigenvalue_sum[list(eigenvalue_sum.keys())[0]][0]

      with archive.m_context.raw_file(self.out_MF_z) as file:
        lines = file.read().splitlines()

      eigenvalue_sum = lastThingy(lines, 'Eigenvalue sum:')
      energies['z'] = eigenvalue_sum[list(eigenvalue_sum.keys())[0]][0]

    logger.info(f'Normalising groundstate energies: {energies}')
    self.energies = energies
    

class UUData(EntryData, ArchiveSection):
  m_def = Section()

  k1 = SubSection(
    section_def=MagnetocrystallineAnisotropyConstantK1,
    repeats = False,
  )

  groundState = SubSection(
    section_def=GroundState,
    repeats = False,
  )

  out_last_file = Quantity(
    type=str,
    description='The \'out_last\' file.',
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

    if self.out_last_file and self.groundState and self.groundState.energies != {}:
      with archive.m_context.raw_file(self.out_last_file) as file:
        lines = file.read().splitlines()

      tot_moments_D = lastThingy(lines, 'Total moment [J=L+S] (mu_B):')
      dir_of_JD = lastThingy(lines, 'Direction of J (Cartesian):')

      magnetization_in_T, ucvA = compute_magnetization(tot_moments_D, dir_of_JD, lines)
      #print(f'Magnetization Ms: {magnetization_in_T} T')

      K1_in_JPerCubibm = self.compute_anisotropy_constant(ucvA, self.groundState.energies)
      print(f'Anisotropy constant (max of all): {K1_in_JPerCubibm} J/m\N{SUPERSCRIPT THREE}')
      logger.info(f'Anisotropy constant (max of all): {K1_in_JPerCubibm} J/m\N{SUPERSCRIPT THREE}')
      try:
        self.k1 = ureg.Quantity(float(K1_in_JPerCubibm), 'J/m**3')
      except Exception as e:
        print(e)
        logger.error(f'Exception {e}')

  def compute_anisotropy_constant(self, ucvA, energies):
    allKs = list()
    if 'z' in energies.keys():
        if 'x' in energies.keys():
            Kxz = (energies['x'] - energies['z'])/ucvA*2179874
            allKs.append(Kxz)
        if 'y' in energies.keys():
            Kyz = (energies['y'] - energies['z'])/ucvA*2179874
            allKs.append(Kyz)

    K1_in_JPerCubibm = max(allKs) * 1e6            # anisotropy J/m³; MagnetocrystallineAnisotropyConstantK1
    return K1_in_JPerCubibm
