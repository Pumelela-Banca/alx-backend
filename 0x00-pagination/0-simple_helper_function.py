#!/usr/bin/env python3
"""
Gets values and returns indexes
"""
import requests


def index_range(page, page_size):
    """
    return a tuple of size two containing a start
    index and an end index corresponding to the
    range of indexes
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
