import os

from nomad.datamodel import EntryArchive
from nomad.parsing import MatchingParser

from cube.schema_packages.uu_schema import GroundState, UUData


class UUParser(MatchingParser):
  def is_mainfile(
    self,
    filename: str,
    mime: str,
    buffer: bytes,
    decoded_buffer: str,
    compression: str = None,
  ):
    print(f'filename {filename}, mime {mime}, compression {compression}')

    if os.path.basename(filename) != "structure.cif":
      return False

    self.dir = os.path.dirname(filename)

    return self.checkFilesPresent()
  
  def checkFilesPresent(self, 
                        check_subfolders=True,
                        check_optional_subf=True,
                        check_README=False,
                        check_structure_cif=True,
                        check_out_last_files=True):
    readme_exists = False
    mandatory_subfolders_exist = False
    structure_cif_exists = False
    out_last_x_exists = False
    out_last_z_exists = False

    if check_README:
      readme_exists = os.path.isfile(os.path.join(self.dir, 'README'))
    if check_subfolders:
      mandatory_subfolders_exist, _ = self.check_subfolders_exist(check_optional_subf)

      if mandatory_subfolders_exist:
        if check_out_last_files:
          out_last_x_exists = os.path.isfile(self.dir+'/GS/x/out_last')
          out_last_z_exists = os.path.isfile(self.dir+'/GS/z/out_last')

        posfile_exists = os.path.isfile(self.dir+'/MC/posfile')
        jfile_exists = os.path.isfile(self.dir+'/MC/jfile')
        momfile_exists = os.path.isfile(self.dir+'/MC/momfile')

        if (posfile_exists or jfile_exists or momfile_exists):
          mom_j_pos_file_exists = True
        else:
          mom_j_pos_file_exists = False

    if check_structure_cif:
      structure_cif_exists = os.path.isfile(os.path.join(self.dir,'structure.cif'))

    return_values = [readme_exists or not check_README, mandatory_subfolders_exist,
                      structure_cif_exists, out_last_x_exists, out_last_z_exists,
                      mom_j_pos_file_exists]

    return all(return_values)

  def check_subfolders_exist(self, check_optional_subf=True):
    mandatory_subfolders = ['GS', 'GS/x', 'GS/z', 'Jij', 'MC']
    non_mandatory_subfolders = ['GS/y']

    mandatory_exist = []
    non_mandatory_exist = []

    for subfolder in mandatory_subfolders:
      subfolder_path = os.path.join(self.dir, subfolder)
      if os.path.isdir(subfolder_path):
        mandatory_exist.append(True)
      else:
        mandatory_exist.append(False)

    if check_optional_subf:
      for subfolder in non_mandatory_subfolders:
        subfolder_path = os.path.join(self.dir, subfolder)
        if os.path.isdir(subfolder_path):
          non_mandatory_exist.append(True)
        else:
          non_mandatory_exist.append(False)
    else:
        non_mandatory_exist = [None] * len(non_mandatory_subfolders)

    return all(mandatory_exist), non_mandatory_exist

  def parse(
      self,
      mainfile: str,
      archive: EntryArchive,
      logger=None,
      child_archives: dict[str, EntryArchive] = None,
    ) -> None:
      print(f'mainfile {mainfile}, archive {archive}, child_archives {child_archives}')
      logger.info('UUParser called')

      baseDir = os.path.dirname(mainfile)
      idx = baseDir.rfind('raw/')
      if idx == -1:
        archiveBaseDir = baseDir
      else:
        archiveBaseDir = baseDir[idx + 4:]

      data_dir_GS = baseDir + "/GS/"
      archiveData_dir_GS = archiveBaseDir + "/GS/"
      data_dir_MC = baseDir + "/MC"

      xyz_dirs = [dirdir for dirdir in os.listdir(data_dir_GS) if len(dirdir) == 1]

      print(f'data_dir_GS {data_dir_GS} data_dir_MC {data_dir_MC}'
             f' xyz_dirs {xyz_dirs} idx{idx}')

      # Reading file into lines; all folders are equivalent according to 
      # UU-colleagues, so we can use the first one
      file_Name_Ms = archiveBaseDir + "/GS/" + f"{xyz_dirs[0]}/out_last"
      print(f'file_Name_Ms {file_Name_Ms}')

      fx = archiveData_dir_GS + "x/out_MF_x" if 'x' in xyz_dirs else None
      fy = archiveData_dir_GS + "y/out_MF_y" if 'y' in xyz_dirs else None
      fz = archiveData_dir_GS + "z/out_MF_z" if 'z' in xyz_dirs else None
      fol = f"{archiveData_dir_GS}{xyz_dirs[0]}/out_last"

      # entry = Cube(data_file=file)
      groundState = GroundState(out_MF_x=fx,out_MF_y=fy,out_MF_z=fz)
      # groundState.normalize(archive=archive,logger=logger)
      entry = UUData(groundState=groundState,out_last_file=fol)

      archive.data = entry
