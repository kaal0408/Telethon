
import sys
import logging
import importlib
from pathlib import Path

def uploadd(cd_name):
    path = Path(f"codes/{cd_name}.py")
    name = "codes.{}".format(cd_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(cd_name)
    spec.loader.exec_module(load)
    sys.modules["codes." + cd_name] = load
    print("Bot has Imported " + cd_name)