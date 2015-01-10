# -*- coding: utf-8 -*-
import json

json_data = b'{"SSIDs":["CPSLab_ng","TDU_MRCL_WLAN_DOT1X","TDU_MRCL_WLAN","CGL","CPSLab_nac","smrl","ASL-A","isl-11a","SETUP","aterm-7ad9e6-a","WEL_n","CDL_g","40814A-an","eduroam","aterm-df4cd9-aw","BIL-106F3F789B93-1","Office-K 5GHz","Stream22080","TDU_MRCL_GUEST","4CE676FAB398_A","106F3F7F567C_A","aterm-7ad9e6-aw","BIL","BIL-1","106F3F29D544_G","DY-RS10_E7314C","001D73B32950-2"],"twitterID":"\xe3\x81\xbb\xe3\x81\x92"}'

data = json.loads(json_data.decode('UTF-8'))
data = '{"SSIDs":["TDU_MRCL_WLAN_DOT1X","","TDU_MRCL_WLAN","eduroam","TDU_MRCL_GUEST","Buffalo-G-3658"], "twitterID":"ざっぷ"}'
print(data)
print(json.loads(data))
