from typing import Dict

from nomad.datamodel import EntryArchive
from nomad.parsing import MatchingParser


class CubeParser(MatchingParser):
    def is_mainfile(
        self,
        filename: str,
        mime: str,
        buffer: bytes,
        decoded_buffer: str,
        compression: str = None,
    ):
        is_mainfile_super = super().is_mainfile(filename, mime, buffer, decoded_buffer, compression)
        print("CubeParser Hello", is_mainfile_super)
        if not is_mainfile_super:
            return False
        return False

    def parse(
        self,
        mainfile: str,
        archive: EntryArchive,
        logger=None,
        child_archives: Dict[str, EntryArchive] = None,
    ) -> None:
        print("Hello")
        logger.info('MyParser called')