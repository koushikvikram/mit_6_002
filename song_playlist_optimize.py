#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 13:09:42 2017

@author: koushikvikram
"""

def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    songs_copy = sorted(songs[1:], key = lambda x:x[2])
    result = []
    totalSize = 0.0
    
    if (songs[0][2] <= max_size):
        totalSize = songs[0][2]
        result.append(songs[0][0])
    else:
        return []
        
    for i in range(len(songs_copy)):
        if (totalSize + songs_copy[i][2]) <= max_size:
            result.append(songs_copy[i][0])
            totalSize += songs_copy[i][2]
    
    return result


        
                     