# connection_finder_prague
Python implementation of troute based public transport routing algorithm - RAPTOR in form of CLI app
## Introduction
The  app implements the Raptor routing algorithm using public transit data in GTFS format.
## Algorithm
The connection search algorithm used in this project is based on RAPTOR-Round (bAsed Public Transit Optimized Router) algorithm (available at: https://renatowerneck.files.wordpress.com/2016/06/dpw14-raptor.pdf). The algorithm is NOT based on graph.
Instead, it operates in rounds, one per transfer, and computes arrival times by traversing every route (such as an underground line) at most once per round.
