#!/usr/bin/env python

import json
import yaml
import sys

print yaml.dump(yaml.load(json.dumps(json.loads(open(sys.argv[1]).read()))),
          default_flow_style=False)

