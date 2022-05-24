from .data import Data
from dask import dataframe as dd
from typing import List, Tuple, Dict


class RadarFileData(Data):
    def __init__(self, data: dd.DataFrame) -> None:
        self._data = data

    def get_data(self) -> dd.DataFrame:
        return self._data

    def set_data(self, data: dd.DataFrame) -> None:
        self._data = data

    def get_data_keys(self) -> List[str]:
        return self._data.keys().tolist()

    def get_data_size(self) -> int:
        return self._data.size

    def _preprocess_data(self) -> None:
        if 'value.time' in self._data.columns:
            self._data['value.time'] = dd.to_datetime(
                self._data['value.time'], unit="s")
        if 'value.timeReceived' in self._data.columns:
            self._data['value.timeReceived'] = dd.to_datetime(
                self._data['value.timeReceived'], unit="s")
        if 'value.dateTime' in self._data.columns:
            self._data['value.dateTime'] = dd.to_datetime(
                self._data['value.dateTime'])
