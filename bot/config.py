#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = config("APP_ID", "5009612")
    API_HASH = config("API_HASH", "999bf38a58a1332ed01591f0624b5768")
    BOT_TOKEN = config("BOT_TOKEN", "6820828774:AAEstbEZHIub8P51UqUIUQGKNoz5w-1WEf4")
    DEV = 943270135
    OWNER = config("OWNER", "943270135")
    ffmpegcode = ["-preset veryfast -c:v libx264 -s 1920x1080 -x264-params 'bframes=10:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title=Encoded By @THECIDANIME' -pix_fmt yuv420p -crf 24 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 8"]
    THUMB = config("THUMBNAIL")
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
