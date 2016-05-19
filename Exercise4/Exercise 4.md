# Exercise 4: Finally, some GIS
##### In this exercise we will finally connect our interface with additional modules that do the "work" for our tool

## CSV 2 SHP
At this point, our lovely tool contains two entry boxes: one for an input CSV file, and the other for an output shapefile.

The data processing folder contains a couple of csv2shp converters (both esri and OS are repping here).  Your task in this exercise is to plug one of these modules into our existing App script.

Some tips:
  - think about what `imports` you may need to make
  - you'll need to pass our input/output paths to the data_processing script in some way
  - have fun



## Bonus Round 1: Charts!
If you're so inclined an additional task is available.  
The data processing folder contains another module that generates a summary graph of a given field from the incident table. 

Your task is to plug this module into our interface App script.

Tip: Look carefully at the graphing module to determine what arguements are necessary to execute the tool--you may have to garner additional user input (ie. more widgets!).
![all of the widgets!](https://cdn.meme.am/instances/57077789.jpg)


## Bonus Round 2:
