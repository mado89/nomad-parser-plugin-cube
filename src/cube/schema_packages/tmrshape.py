#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from typing import (
  TYPE_CHECKING,
)

import numpy as np
import pandas as pd
import plotly.express as px
import yaml
from nomad.datamodel.data import (
  ArchiveSection,
  EntryData,
)
from nomad.datamodel.metainfo.plot import PlotlyFigure, PlotSection
from nomad.datamodel.results import Simulation
from nomad.metainfo import (
  Package,
  Quantity,
  Section,
  SubSection,
)

if TYPE_CHECKING:
  from nomad.datamodel.datamodel import (
      EntryArchive,
  )
  from structlog.stdlib import (
      BoundLogger,
  )

m_package = Package(name='Schema for TMRB4Vex Simulation')


class DatabaseConfig(EntryData):
    # use_DB: bool
    # read: bool
    # write: bool
    # name: str
    # db_path: str
    # postProc_global_path: str
  m_def= Section(
    a_eln=dict(
      properties=dict(order=[
        'use_DB',
        'read',
        'write',
        'name',
        'db_path',
        'postProc_global_path'
      ])
    )
  )

class SimulationConfigShape(EntryData):
  m_def= Section(
    a_eln=dict(
      properties=dict(order=[
        'name'
      ])
    )
  )
  name = Quantity(
      type=str,
      description='Name',
  )

class EllipseConfig(SimulationConfigShape, EntryData):
  m_def= Section(
    a_eln=dict(
      properties=dict(order=[
        'init_r1',
        'init_r2',
        'init_h',
      ])
    )
  )
  init_r1 = Quantity(
      type=np.float64,
      description='Radius 1',
      a_eln={
          "component": "NumberEditQuantity",
          "defaultDisplayUnit": "nanometer"
      },
      # unit="celsius",
  )
  init_r2 = Quantity(
      type=np.float64,
      description='Radius 2',
      a_eln={
          "component": "NumberEditQuantity",
          "defaultDisplayUnit": "nanometer"
      },
      # unit="celsius",
  )
  init_h = Quantity(
      type=np.float64,
      description='Height',
      a_eln={
          "component": "NumberEditQuantity",
          "defaultDisplayUnit": "nanometer"
      },
      # unit="celsius",
  )

class BoxConfig(SimulationConfigShape, EntryData):
  m_def= Section(
    a_eln=dict(
      properties=dict(order=[
        'init_xlen',
        'init_ylen',
        'init_zlen',
      ])
    )
  )
  init_xlen = Quantity(
      type=np.float64,
      description='Initial length x',
      a_eln={
          "component": "NumberEditQuantity",
          "defaultDisplayUnit": "nanometer"
      },
      # unit="celsius",
  )
  init_ylen = Quantity(
      type=np.float64,
      description='Initial length y',
      a_eln={
          "component": "NumberEditQuantity",
          "defaultDisplayUnit": "nanometer"
      },
      # unit="celsius",
  )
  init_zlen = Quantity(
      type=np.float64,
      description='Initial length z',
      a_eln={
          "component": "NumberEditQuantity",
          "defaultDisplayUnit": "nanometer"
      },
      # unit="celsius",
  )

class SimulationConfigSimulation(EntryData):
  m_def = Section(
    a_eln=dict(
      properties=dict(order=[
        'sim_name',
        'iter',
        'main_Mesh_min',
        'main_mesh_max',
        'object_Mesh_max',
        'xlen_start',
        'xlen_stop',
        'ylen_start',
        'ylen_stop',
        'zlen_start',
        'zlen_stop',
        'hstart',
        'hfinal',
        'hstep',
      ])
    ),
  )
  # sim_name: str
  # iter: int
  # main_Mesh_min: float
  # main_mesh_max: float
  # object_Mesh_max: float
  # xlen_start: float
  # xlen_stop: float
  # ylen_start: float
  # ylen_stop: float
  # zlen_start: float
  # zlen_stop: float
  # hstart: float
  # hfinal: float
  # hstep: float

class ServerConfig(EntryData):
    # number_cores: int
    # mem_GB: int
    # gpu: str
  m_def= Section(
    a_eln=dict(
      properties=dict(order=[
        'number_cores',
        'mem_GB',
        'gpu',
      ])
    )
  )

class GeneralSettingsConfig(EntryData):
    # log_level: int
    # location: str
  m_def= Section(
    a_eln=dict(
      properties=dict(order=[
        'log_level',
        'location',
      ])
    )
  )

class Optimizer(EntryData):
    # acq_kind: str
    # kappa: float
    # xi: float
    # kappa_decay: float
    # kappa_decay_delay: int
  m_def= Section(
    a_eln=dict(
      properties=dict(order=[
        'acq_kind',
        'kappa',
        'xi',
        'kappa_decay',
        'kappa_decay_delay',
      ])
    )
  )


class SimulationConfig(EntryData):
  m_def = Section()
  database = SubSection(
    section_def=DatabaseConfig,
    repeats=False
  )
  shape = SubSection(
    section_def=SimulationConfigShape,
    repeats=False
  )
  simulation = SubSection(
    section_def=SimulationConfigSimulation,
    repeats=False,
  )
  server = SubSection(
    section_def=ServerConfig,
    repeats=False,
  )
  generalSettings = SubSection(
    section_def=GeneralSettingsConfig,
    repeats=False,
  )
  optimizer = SubSection(
    section_def=Optimizer,
    repeats=False,
  )
  #
  # database: DatabaseConfig
  # shape: ShapeConfig
  # simulation: SimulationConfig
  # server: ServerConfig
  # generalSettings: generalSettingsConfig
  # optimizer: Optimizer

class Row(ArchiveSection):
  m_def = Section(
      a_eln={
          "properties": {
              "order": [
                  "time",
                  "H_ex",
                  "M",
              ]
          }
      },)

  M = Quantity(
      type=np.float64,
      description='Magnetisation',
      a_eln={
          "component": "NumberEditQuantity",
          "defaultDisplayUnit": "celsius"
      },
      # unit="celsius",
  )

  def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
      '''
      The normalizer for the `TemperatureRamp` class.

      Args:
          archive (EntryArchive): The archive containing the section that is being
          normalized.
          logger (BoundLogger): A structlog logger.
      '''
      super().normalize(archive, logger)


class B4VexSimulation(Simulation, PlotSection, EntryData, ArchiveSection):
  m_def = Section()
  configuration = SubSection(
    section_def=SimulationConfig,
    repeats = False,
  )
  steps = SubSection(
    section_def=Row,
    repeats=True,
  )
  result_file = Quantity(
    type=str,
    description='The recipe file for the sintering process.',
    a_eln={
        "component": "FileEditQuantity",
    },
  )
  config_file = Quantity(
    type=str,
    description='The configuration file for the simulation.',
    a_eln={
        "component": "FileEditQuantity",
    },
  )

  def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
    '''
    The normalizer for the `B4VexSimulation` class.

    Args:
        archive (EntryArchive): The archive containing the section that is being
        normalized.
        logger (BoundLogger): A structlog logger.
    '''
    super().normalize(archive, logger)
    if self.result_file:
      self.readResult(archive)
    if self.config_file:
      self.readConfig(archive)
      logger.info("Reading configuration from file done")

    # self.createFigures()

  def readConfig(self, archive: 'EntryArchive'):
    with archive.m_context.raw_file(self.config_file) as file:
      config_data = yaml.safe_load(file)
      # print(config_data)
      
      config = SimulationConfig()
      config.database = DatabaseConfig()
      config.shape = BoxConfig() \
                      if config_data['shape']['name'] == 'Box' else EllipseConfig()
      config.simulation = SimulationConfigSimulation()
      config.server = ServerConfig()
      config.generalSettings = GeneralSettingsConfig()
      config.optimizer = Optimizer()

      for key in config_data['database']:
        setattr(config.database, key, config_data['database'][key])
      for key in config_data['shape']:
        setattr(config.shape, key, config_data['shape'][key])
      for key in config_data['simulation']:
        setattr(config.simulation, key, config_data['simulation'][key])
      for key in config_data['database']:
        setattr(config.database, key, config_data['database'][key])

      self.configuration = config
      print(f"Config {config}")

  def readResult(self, archive: 'EntryArchive'):
    steps = []
    with archive.m_context.raw_file(self.result_file) as file:
      df = pd.read_csv(file, sep=' ', header=0, names=['time', 'H_ex', 'M'])
    for i, row in df.iterrows():
      step = Row()
      step.time = row['time']
      step.H_ex = row['H_ex']
      step.M = row['M']
      steps.append(step)
    self.steps = steps

  def createFigures(self):
    x = [s.H_ex for s in self.steps]
    y = [s.M for s in self.steps]
    figure2 = px.scatter(x=x, y=y, 
                          labels={
                            "x": "H_ex",
                            "y": "M"
                          },
                          title="Figure title")
    self.figures.append(PlotlyFigure(label='figure 1', index=1, 
                                      figure=figure2.to_plotly_json()))


m_package.__init_metainfo__()

        
