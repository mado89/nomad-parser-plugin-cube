import os

from nomad.datamodel import EntryArchive
from nomad.parsing import MatchingParser

from cube.schema_packages.cube import Cube


class CubeParser(MatchingParser):
    def is_mainfile(
        self,
        filename: str,
        mime: str,
        buffer: bytes,
        decoded_buffer: str,
        compression: str = None,
    ):
        is_mainfile_super = super().is_mainfile(filename, mime, buffer, decoded_buffer,
                                                 compression)
        if not is_mainfile_super:
            return False
        file = os.path.basename(filename)
        #TODO: here could be more checks whether it is actually a correct cube.dat
        return file == "cube.dat"

    def parse(
        self,
        mainfile: str,
        archive: EntryArchive,
        logger=None,
        child_archives: dict[str, EntryArchive] = None,
    ) -> None:
        file = os.path.basename(mainfile)
        # print("Hello", file, mainfile, archive, child_archives)
        logger.info('CubeParser called')

        entry = Cube(data_file=file)

        archive.data = entry