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
import numpy as np
import time

DEFAULT_CONFIG_LOCATION = os.path.join(os.path.dirname(__file__), 'cloud_config.ini')


def update_display(display, msg):
    with canvas(display) as draw:
        draw.text((0, 0), msg, fill='white')


def _none_to_nan(val):
    return float('nan') if val is None else val


def main():
    # Pull arguments from command line.
    total_display = 10
    display_duration = 0.2
    # Create instances of EnviroKit and Cloud IoT.
    enviro_sensor = EnviroBoard()
    start = time.time()

    # Indefinitely update display and upload to cloud.
    sensors = {'ambient_light': []}
    read_period = int(total_display / display_duration)
    light_value = 0
    for read_count in range(read_period):
        # dis play light sensor
        light_value = enviro_sensor.ambient_light
        sensors['ambient_light'].append(light_value)
        msg = 'Light: %.2f lux\n' % _none_to_nan(light_value)
        # update_display(enviro_sensor.display, msg)

        # print log
        real_time = time.time() - start
        print(light_value, read_count, real_time)
        # sleep(display_duration)

    # write value to file
    value_to_file = np.array(sensors['ambient_light'])
    write_file = open("sensor_value.txt", "w")
    np.savetxt(write_file, value_to_file)
    write_file.close()


if __name__ == '__main__':
    main()
