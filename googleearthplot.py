#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# python library for google earth plot 
#
# author: Atsushi Sakai
# 
# Copyright (c): 2015 Atsushi Sakai
#
# License : GPL Software License Agreement

import simplekml
import pandas
import math

class googleearthplot:
    def __init__(self):
        self.kml = simplekml.Kml()

    def PlotBarChart(self, lat, lon, num, size=1, name="", color="red"):
        """
        Add Bar Chart
        size: unit:meterm, defalut:1m
        name: data name, default:""(empty string)
        color: bar chart color, default:red

        """
        pol = self.kml.newpolygon(
                name=name,
                extrude=1,
                tessellate=1,
                description=str(num),
                altitudemode="absolute")

        latShift=self.CalcLatFromMeter(size)
        lonShift=self.CalcLonFromMeter(size, lat)

        boundary=[]
        boundary.append((lat+latShift,lon+lonShift,num))
        boundary.append((lat-latShift,lon+lonShift,num))
        boundary.append((lat-latShift,lon-lonShift,num))
        boundary.append((lat+latShift,lon-lonShift,num))
        boundary.append((lat+latShift,lon+lonShift,num))
        pol.outerboundaryis=boundary

        #Set Color
        colorObj=self.GetColorObject(color)
        pol.style.linestyle.color = colorObj
        pol.style.polystyle.color = colorObj

        print "[PlotBarChart]lat:"+str(lat)+",lon:"+str(lon)

    def PlotBarChartsFromCSV(self, filepath):
        """
        filepath: csvfile path
        """
        print "[PlotBarChartsFromCSV]plotting bar charts from csv file:"+filepath
        data=pandas.read_csv(filepath)

        #PlotBarChart
        nbar=0
        zipdata=zip(data["lat"],data["lon"],data["num"],data["size"],data["name"],data["color"])
        for (lat, lon, num, size, name, color) in zipdata:
            self.PlotBarChart(lat,lon,num,size,name,color)
            nbar+=1

        print "[PlotBarChartsFromCSV]"+str(nbar)+" bars have plotted"


    def GetColorObject(self, color):
        valiableStr="simplekml.Color."+color
        colorObj=eval(valiableStr)
        return colorObj

    def CalcLatFromMeter(self, shift):
        return shift/111263.283  #degree

    def CalcLonFromMeter(self, shift, lon):
        const=6378150*math.cos(lon/180*math.pi)*2*math.pi/360
        return shift/const  #degree

    def GenerateKMLFile(self, filepath="sample.kml"):
        """Generate KML File"""
        self.kml.save(filepath)

if __name__ == '__main__':

    #A bar plot 
    gep1=googleearthplot()
    lat=18.333868#degree
    lon=-34.038274#degree
    num=100 #bar height size
    size=1  #meter
    name="barsample"
    color="red"
    gep1.PlotBarChart(lat,lon,num,size,name,color);
    gep1.GenerateKMLFile(filepath="sample1.kml")

    #bar plot from csv
    gep=googleearthplot()
    gep.PlotBarChartsFromCSV("barchartsampledata.csv")
    gep.GenerateKMLFile(filepath="sample2.kml")
    
    

