# (c) 2020 frabit-server Project maintained and limited by FrabiTech < blylei.info@gmail.com >
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#
# This file is part of frabit-server
"""
后台备份任务扫描器
"""

import os
import re
import logging

import frabitd
from frabitd.process import ProcessManager


_logger = logging.getLogger(__name__)


class Scanner:
    """
    add doc here
    """
    def __init__(self, config):
        self.config = config
        self.process_manager = ProcessManager(self.config)

    def process(self):
        pass
