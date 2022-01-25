# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from coral.enviro.board import EnviroBoard
from coral.cloudiot.core import CloudIot
from luma.core.render import canvas
from PIL import ImageDraw
from time import sleep
import argparse
import itertools
import os
DEFAULT_CONFIG_LOCATION = os.path.join(os.path.dirname(__file__), 'cloud_config.ini')
def update_display(display, msg):
    with canvas(display) as draw:
        draw.text((0, 0), msg, fill='white')
def _none_to_nan(val):
    return float('nan') if val is None else val
def main():
    # Pull arguments from command line.
    total_display = 300
    display_duration = 5
    # Create instances of EnviroKit and Cloud IoT.
    enviro = EnviroBoard()
    with CloudIot(args.cloud_config) as cloud:
        # Indefinitely update display and upload to cloud.
        sensors = {}
        read_period = int(total_display / display_duration)
        for read_count in itertools.count():
            #dis play light sensor
            sensors['ambient_light'] = enviro.ambient_light
            msg = 'Light: %.2f lux\n' % _none_to_nan(sensors['ambient_light'])
            update_display(enviro.display, msg)
            sleep(args.display_duration)
            print(sensors['ambien_light'])
if __name__ == '__main__':
    main()