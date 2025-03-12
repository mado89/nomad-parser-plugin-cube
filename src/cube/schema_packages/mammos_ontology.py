from importlib.resources import Package
from typing import (
  TYPE_CHECKING,
)

import numpy as np
from nomad.datamodel.data import (
  ArchiveSection,
  EntryData,
)
from nomad.metainfo import (
  Quantity,
  Section,
  SubSection,
)

if TYPE_CHECKING:
  pass


m_package = Package(name='Schema for Mammos')
m_package.__init_metainfo__()

def Length():
  return Quantity(
      type=np.float64,
      a_eln={
          "component": "NumberEditQuantity",
          "defaultDisplayUnit": "nm"
      },
      unit="nm",
  )

def Angle():
  return Quantity(
      type=np.float64,
      a_eln={
          "component": "NumberEditQuantity",
          "defaultDisplayUnit": "rad"
      },
      unit="rad",
  )

def Volume():
  return Quantity(
      type=np.float64,
      a_eln={
          "component": "NumberEditQuantity",
          "defaultDisplayUnit": "nm**3"
      },
      unit="nm**3",
  )

class LatticeConstantA(ArchiveSection):
  """
  IRI: https://w3id.org/emmo/domain/magnetic_material#EMMO_ef314f95-f3b5-5cb7-ac56-7bfc54f0d955

  elucidation: The length of lattice vectors a, where lattice vectors a, b and c 
    defines the unit cell.

  IECEntry: https://www.electropedia.org/iev/iev.nsf/display?openform&ievref=561-07-13

  altLabel: LatticeParameterA

  prefLabel: LatticeConstantA

  wikidataReference: https://www.wikidata.org/wiki/Q625641

  wikipediaReference: https://en.wikipedia.org/wiki/Lattice_constant

  Subclass of:

    is_a Length"""
  m_def= Section(
    a_eln=dict(
      properties=dict(order=[
        'length'
      ])
    )
  )
  length = Length()

class LatticeConstantB(ArchiveSection):
  """
  IRI: https://w3id.org/emmo/domain/magnetic_material#EMMO_a1f03bbf-c503-5759-9a26-2562527c0db2

  elucidation: The length of lattice vectors b, where lattice vectors a, b and c 
    defines the unit cell.

IECEntry: https://www.electropedia.org/iev/iev.nsf/display?openform&ievref=561-07-13

altLabel: LatticeParameterB

prefLabel: LatticeConstantB

wikidataReference: https://www.wikidata.org/wiki/Q625641

wikipediaReference: https://en.wikipedia.org/wiki/Lattice_constant

Subclass of:

    is_a Length"""
  m_def= Section(
    a_eln=dict(
      properties=dict(order=[
        'length'
      ])
    )
  )
  length = Length()

class LatticeConstantBeta(ArchiveSection):
  """IRI: https://w3id.org/emmo/domain/magnetic_material#EMMO_2ca16b3d-f83e-583c-8292-beb6473ea021

  elucidation: The angle between lattice vectors a and c, where lattice vectors a, b
    and c defines the unit cell.

altLabel: LatticeParameterBeta

prefLabel: LatticeConstantBeta

wikidataReference: https://www.wikidata.org/wiki/Q625641

Subclass of:

    is_a Angle"""
  m_def= Section(
    a_eln=dict(
      properties=dict(order=[
        'angle'
      ])
    )
  )
  angle = Angle()

class LatticeConstantC(ArchiveSection):
  """
  IRI: https://w3id.org/emmo/domain/magnetic_material#EMMO_9977edfa-2b42-55e4-bea0-f39fadca7126

  elucidation: The length of lattice vectors c, where lattice vectors a, b
    and c defines the unit cell.

IECEntry: https://www.electropedia.org/iev/iev.nsf/display?openform&ievref=561-07-13

altLabel: LatticeParameterC

prefLabel: LatticeConstantC

wikidataReference: https://www.wikidata.org/wiki/Q625641

wikipediaReference: https://en.wikipedia.org/wiki/Lattice_constant

Subclass of:

    is_a Length"""
  m_def= Section(
    a_eln=dict(
      properties=dict(order=[
        'length'
      ])
    )
  )
  length = Length()

class LatticeConstantAlpha(ArchiveSection):
  """IRI: https://w3id.org/emmo/domain/magnetic_material#EMMO_b2a130c3-9688-5358-94ca-f226b85b3009

  elucidation: The angle between lattice vectors b and c, where lattice vectors a, b
    and c defines the unit cell.

altLabel: LatticeParameterAlpha

prefLabel: LatticeConstantAlpha

wikidataReference: https://www.wikidata.org/wiki/Q625641

Subclass of:

    is_a Angle"""
  m_def= Section(
    a_eln=dict(
      properties=dict(order=[
        'angle'
      ])
    )
  )
  angle = Angle()

class LatticeConstantGamma(ArchiveSection):
  """IRI: https://w3id.org/emmo/domain/magnetic_material#EMMO_a205766b-7c02-5c56-90e5-96c553c316c8

  elucidation: The angle between lattice vectors a and b, where lattice vectors a, b
    and c defines the unit cell.

altLabel: LatticeParameterGamma

prefLabel: LatticeConstantGamma

wikidataReference: https://www.wikidata.org/wiki/Q625641

Subclass of:

    is_a Angle"""
  m_def= Section(
    a_eln=dict(
      properties=dict(order=[
        'angle'
      ])
    )
  )
  angle = Angle()

class CellVolume(ArchiveSection):
  """IRI: https://w3id.org/emmo/domain/magnetic_material#EMMO_2b7f8b13-d0c3-590c-9851-ca89ce5b7395

elucidation: Volume of the unit cell.

altLabel: UnitCellVolume

prefLabel: CellVolume

Subclass of:

    is_a Volume"""
  m_def = Section(
    a_eln=dict(
      properties=dict(order=[
        'volume'
      ])
    )
  )
  volume = Volume()

class SpaceGroup(ArchiveSection):
  """RI: https://w3id.org/emmo/domain/magnetic_material#EMMO_5d5fbcc0-2738-5cb8-9157-a0fbe50eebb6

  elucidation: A spacegroup is the symmetry group off all symmetry operations that
    apply to a crystal structure.

  The complete symmetry of a crystal, including the Bravais lattice and any
    translational symmetry elements, is given by one of the 240 space groups.

  A space group is identified by its Hermann-Mauguin symbol or space group number
    (and setting) in the International tables of Crystallography.

prefLabel: SpaceGroup

wikidataReference: https://www.wikidata.org/wiki/Q899033

wikipediaReference: https://en.wikipedia.org/wiki/Space_group

Subclass of:

    is_a NominalProperty
    hasStringValue some String"""
  m_def = Section(
    a_eln=dict(
      properties=dict(order=[
        'spaceGroup'
      ])
    )
  )
  spaceGroup = Quantity(
      type=str,
      a_eln={
          "component": "StringEditQuantity"
      }
  )

class CrystalStructure(EntryData, ArchiveSection):
  """
  CrystalStructure

IRI: https://w3id.org/emmo/domain/magnetic_material#EMMO_2c96e798-57dc-5c12-ad10-f3ec261549d3

elucidation: Description of ordered arrangement of atoms.

prefLabel: CrystalStructure

wikidataReference: https://www.wikidata.org/wiki/Q895901

wikipediaReference: https://en.wikipedia.org/wiki/Crystal_structure

Subclass of:

    is_a Property
    hasProperty exactly 1 LatticeConstantA
    hasProperty exactly 1 LatticeConstantC
    hasProperty exactly 1 LatticeConstantAlpha
    hasProperty exactly 1 CellVolume
    hasProperty exactly 1 LatticeConstantGamma
    hasProperty exactly 1 SpaceGroup
    hasProperty exactly 1 LatticeConstantB
    hasProperty exactly 1 LatticeConstantBeta

  """
  m_def = Section()
  latticeConstantA = SubSection(
    section_def=LatticeConstantA,
    repeats = False,
  )
  latticeConstantC = SubSection(
    section_def=LatticeConstantC,
    repeats = False,
  )
  latticeConstantAlpha = SubSection(
    section_def=LatticeConstantAlpha,
    repeats = False,
  )
  cellVolume = SubSection(
    section_def=CellVolume,
    repeats = False
  )
  latticeConstantGamma = SubSection(
    section_def=LatticeConstantGamma,
    repeats = False,
  )
  spaceGroup = SubSection(
    section_def=SpaceGroup,
    repeats = False,
  )
  latticeConstantB = SubSection(
    section_def=LatticeConstantB,
    repeats = False,
  )
  latticeConstantBeta = SubSection(
    section_def=LatticeConstantBeta,
    repeats = False,
  )
