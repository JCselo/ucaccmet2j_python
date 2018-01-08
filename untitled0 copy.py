#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

with open("precipitation.json") as file:
    rain = json.load(file)

seattle_precipitation = []

for item in rain:
    if item["station"] == "GHCND:US1WAKG0038":
        seattle_precipitation.append(item)
    
jan = [0]
feb = [0]
mar = [0]
apr = [0]
may = [0]
jun = [0]
jul = [0]
aug = [0]
sep = [0]
oct = [0]
nov = [0]
dec = [0]  

seattle_monthly = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    
   
for item in seattle_precipitation:
    if item ['date'][5:7] == "01":
       seattle_monthly[0] += item["value"]
    elif item ['date'][5:7] == "02":
        seattle_monthly[1] += item["value"]
    elif item ['date'][5:7] == "03":
        seattle_monthly[2] += item["value"]
    elif item ['date'][5:7] == "04":
        seattle_monthly[3] += item["value"]
    elif item ['date'][5:7] == "05":
        seattle_monthly[4] += item["value"]
    elif item ['date'][5:7] == "06":
        seattle_monthly[5] += item["value"]
    elif item ['date'][5:7] == "07":
        seattle_monthly[6] += item["value"]
    elif item ['date'][5:7] == "08":
        seattle_monthly[7] += item["value"]
    elif item ['date'][5:7] == "09":
        seattle_monthly[8] += item["value"]
    elif item ['date'][5:7] == "10":
        seattle_monthly[9] += item["value"]
    elif item ['date'][5:7] == "11":
        seattle_monthly[10] += item["value"]
    elif item ['date'][5:7] == "12":
        seattle_monthly[11] += item["value"]
print(seattle_monthly)

        