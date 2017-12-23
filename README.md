# tweets-location-over-time
Show tweets location about a topic (list of keywords) in a time-series.
So showing tweets tweets location on the map animating depending on date. Example http://m-saleh.github.io/
# Phase One:
FOR A GIVEN list of keywords start pulling tweets.
+ Desing :
https://github.com/M-Saleh/tweets-location-over-time/wiki/Phase-One-Design

# Roughly TODOs for next phases:
1. Start general stream to save all geo-tagged tweets where user search inin our DB supporting historical search.
We need a time-series DB+handling queries with keywords! check : Cassandra Time Series Data Modeling and elasticsearch-as-a-time-series-data-store. others : https://misfra.me/2016/04/09/tsdb-list/
2. Handle visualization part.
