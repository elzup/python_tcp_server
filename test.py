# -*- coding: utf-8 -*-
import json

json_data = '{"SSIDs":["TDU_MRCL_WLAN_DOT1X","TDU_MRCL_WLAN","eduroam","TDU_MRCL_GUEST","Buffalo-G-3658"], "twitterID":"hoge"}'
data = json.loads(json_data)
print(data)
