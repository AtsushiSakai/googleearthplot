googleearthplot
===============

Python library for plotting on google earth

## Galleries

![barchartssample.png](https://github.com/AtsushiSakai/googleearthplot/blob/master/img/barchartssample.png)

![barchartsample.png](https://github.com/AtsushiSakai/googleearthplot/blob/master/img/barchartsample.png)

![linechartsample.png](https://github.com/AtsushiSakai/googleearthplot/blob/master/img/linechartsample.png)

![linechartwithheightsample.png](https://github.com/AtsushiSakai/googleearthplot/blob/master/img/linechartwithheightsample.png)


## Requirements

### simplekml

- [Overview SIMPLEKML 1.2.8 documentation](http://www.simplekml.com/en/latest/index.html)

install:

> $ pip install simplekml

### pandas

- [Python Data Analysis Library  pandas: Python Data Analysis Library](http://pandas.pydata.org/)

install:

> $ pip install pandas

### Google Earth (Pro)

- [Google Earth](http://www.google.com/earth/download/ge/agree.html)

install:

from the upper link

## Install

Download this repository,

> $ git clone https://github.com/AtsushiSakai/googleearthplot.git

import the library in your python code.

> import googleearthplot

## Usages

This library generates a kml file for plot as below.

### A bar plot 

You can plot a bar chart like:

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

If you click the generated kml file,

you can see the plot on Google Earth.

![barchartsample.png](https://github.com/AtsushiSakai/googleearthplot/blob/master/img/barchartsample.png)


### Bar plots from csv data

You can plot bar charts from a csv file like:

    #bar plot from csv
    gep=googleearthplot()
    gep.PlotBarChartsFromCSV("barchartsampledata.csv")
    gep.GenerateKMLFile(filepath="sample2.kml")
    

you can see plots when you click the generated kml file.

![barchartssample.png](https://github.com/AtsushiSakai/googleearthplot/blob/master/img/barchartssample.png)

The CSV file format should be like the sample file:

- [barchartsampledata.csv](https://github.com/AtsushiSakai/googleearthplot/blob/master/barchartsampledata.csv)


### Line plot

You can plot a line chart:

    #Plot line chart
    gep2=googleearthplot()
    lat=[-77.6192,-77.6192,-77.6195,-77.6198,-77.6208,-77.6216,-77.6216,-77.6216]
    lon=[43.1725,43.1725,43.1728,43.173,43.1725,43.1719,43.1719,43.1719,43.1719]
    gep2.PlotLineChart(lat, lon, name="trajectory",color="pink")
    gep2.GenerateKMLFile(filepath="sample3.kml")
    
Then, you can see:

![linechartsample.png](https://github.com/AtsushiSakai/googleearthplot/blob/master/img/linechartsample.png)

### Line plot with height 

You can plot a line chart with height data:

    #Plot line chart with height
    gep3=googleearthplot()
    lat=[-77.6192,-77.6192,-77.6195,-77.6198,-77.6208,-77.6216]
    lon=[43.1725,43.1725,43.1728,43.173,43.1725,43.1719,43.1719]
    height=[10,40,60,80,100,120,140]
    gep3.PlotLineChart(lat, lon, heightList=height, name="trajectory2",color="aqua")
    gep3.GenerateKMLFile(filepath="sample4.kml")
 

you can see:

![linechartwithheightsample.png](https://github.com/AtsushiSakai/googleearthplot/blob/master/img/linechartwithheightsample.png)


## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Author

[AtsushiSakai](http://atsushisakai.github.io/)


