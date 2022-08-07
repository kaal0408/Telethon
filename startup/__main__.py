# <-- imports -->
import glob
from pathlib import Path
from startup.utils import uploadd

# <--creating path to load all modules -->
path = "codes/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        code = Path(f.name)
        cd_name = code.stem
        uploadd(cd_name.replace(".py", ""))