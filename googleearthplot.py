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

    def PlotLineChartFromCSV(self, filepath, name="", color="red", width=5):
        """
        Plot Line Chart from CSVfile
        """
        print "[PlotLineChartFromCSV] plotting a line chart from csv file:"+filepath
        data=pandas.read_csv(filepath)

        if "height" in data:
            self.PlotLineChart(data["lat"],data["lon"],heightList=data["height"], name=name,color=color,width=width)
        else:
            self.PlotLineChart(data["lat"],data["lon"],name=name,color=color,width=width)
     
    def PlotLineChart(self, latList, lonList, heightList=[], name="", color="red", width=5):
        """
        Plot Line Chart
        """
        ls = self.kml.newlinestring(
                name=name,
                description=name
                )
        coords=[]
        if len(heightList)==0:
            for (lat,lon) in zip(latList,lonList):
                coords.append((lat,lon))
        else:
            for (lat,lon,height) in zip(latList, lonList, heightList):
                coords.append((lat,lon,height))
        
        ls.coords = coords
        ls.extrude = 1
        ls.altitudemode = simplekml.AltitudeMode.relativetoground
        ls.style.linestyle.width = width
        ls.style.linestyle.color = self.GetColorObject(color)

        print "[PlotLineChart]name:"+name+",color:"+color+",width:"+str(width)


    def PlotBarChart(self, lat, lon, num, size=1, name="", color="red", addLabel=False):
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
                visibility=1,
                #gxballoonvisibility=1,
                altitudemode="absolute"
                )

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

        if addLabel:
            self.PlotLabel(lat,lon,name+":"+str(num),color=color)

        print "[PlotBarChart]lat:"+str(lat)+",lon:"+str(lon)

    def PlotLabel(self,lat,lon,label,color="red",labelScale=1):
        """
        Plot only label
        """
        pnt = self.kml.newpoint(name=label)
        pnt.coords = [(lat, lon)]
        pnt.style.labelstyle.color = self.GetColorObject(color)
        pnt.style.labelstyle.scale = labelScale
        pnt.style.iconstyle.scale = 0  # hide icon
        print "[PlotLabel]"+label

    def PlotBarChartsFromCSV(self, filepath, addLabel=False):
        """
        filepath: csvfile path
        """
        print "[PlotBarChartsFromCSV]plotting bar charts from csv file:"+filepath
        data=pandas.read_csv(filepath)

        #PlotBarChart
        nbar=0
        zipdata=zip(data["lat"],data["lon"],data["num"],data["size"],data["name"],data["color"])
        for (lat, lon, num, size, name, color) in zipdata:
            self.PlotBarChart(lat,lon,num,size,name,color,addLabel=addLabel)
            nbar+=1

        print "[PlotBarChartsFromCSV]"+str(nbar)+" bars have plotted"

    def PlotOverlayImg(self, filepath, xpixel, ypixel, name="ScreenOverlay"):
        """
        filepath: file path
        xpixel
        ypixel
        name (option)
        """
        print "[PlotOverlayImg] plotting image file:"+filepath+",xpixel:"+str(xpixel)+",ypixel"+str(ypixel)

        screen = self.kml.newscreenoverlay(name=name)
        screen.icon.href = filepath
        screen.overlayxy = simplekml.OverlayXY(x=0,y=0,xunits=simplekml.Units.fraction,yunits=simplekml.Units.fraction)
        screen.screenxy = simplekml.ScreenXY(x=xpixel, y=ypixel,xunits=simplekml.Units.pixel,yunits=simplekml.Units.insetpixels)
        screen.size.x = -1
        screen.size.y = -1
        screen.size.xunits = simplekml.Units.fraction
        screen.size.yunits = simplekml.Units.fraction

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

    #bar plot from csv file
    gep=googleearthplot()
    gep.PlotBarChartsFromCSV("sampledata/barchartsampledata.csv")
    gep.GenerateKMLFile(filepath="sample2.kml")

    #Plot line chart
    gep2=googleearthplot()
    lat=[-77.6192,-77.6192,-77.6195,-77.6198,-77.6208,-77.6216,-77.6216,-77.6216]
    lon=[43.1725,43.1725,43.1728,43.173,43.1725,43.1719,43.1719,43.1719,43.1719]
    gep2.PlotLineChart(lat, lon, name="trajectory",color="pink")
    gep2.GenerateKMLFile(filepath="sample3.kml")
    
    #Plot line chart with height
    gep3=googleearthplot()
    lat=[-77.6192,-77.6192,-77.6195,-77.6198,-77.6208,-77.6216]
    lon=[43.1725,43.1725,43.1728,43.173,43.1725,43.1719,43.1719]
    height=[10,40,60,80,100,120,140]
    gep3.PlotLineChart(lat, lon, heightList=height, name="trajectory2",color="aqua")
    gep3.GenerateKMLFile(filepath="sample4.kml")
 
    #line plot from csv file
    gep4=googleearthplot()
    gep4.PlotLineChartFromCSV("sampledata/lineplotsampledata.csv", name="trajectory3", color="gold", width=10)
    gep4.GenerateKMLFile(filepath="sample5.kml")

    #line plot from csv file with height
    gep5=googleearthplot()
    gep5.PlotLineChartFromCSV("sampledata/lineplotsampledata2.csv", name="trajectory4", color="orange", width=10)
    gep5.GenerateKMLFile(filepath="sample6.kml")

    #bar plot with label from csv file
    gep7=googleearthplot()
    gep7.PlotBarChartsFromCSV("sampledata/barchartsampledata.csv",addLabel=True)
    gep7.GenerateKMLFile(filepath="sample7.kml")

    #bar plot with label from csv file
    gep8=googleearthplot()
    gep8.PlotOverlayImg("img/samplelogo.png",200,300,name="logo")
    gep8.GenerateKMLFile(filepath="sample8.kml")






