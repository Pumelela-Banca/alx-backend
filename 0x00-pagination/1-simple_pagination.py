#!/usr/bin/env python3
"""
Gets values and returns indexes
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> List[int, int]:
    """
    return a tuple of size two containing a start
    index and an end index corresponding to the
    range of indexes
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns page with data
        """
        assert isinstance(page, int), ("when page"
                                       " and/or page_size are not ints")
        assert isinstance(page_size, int), ("raised when page"
                                            " and/or page_size are not ints")
        assert page_size <= 0, "with negative values"
        assert page < 0, "raised with 0"
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start: end]
