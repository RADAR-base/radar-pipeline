from abc import ABC, abstractmethod
from typing import List, Tuple, Dict
import pandas as pd
from dask import dataframe as dd


class Data(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def set_data(self, data) -> None:
        pass

    @abstractmethod
    def get_data_keys(self) -> List[str]:
        pass

    @abstractmethod
    def get_data_size(self) -> int:
        pass

    def _preprocess_data(self) -> None:
        for key in self._data.keys():
            self._data[key]._preprocess_data()
