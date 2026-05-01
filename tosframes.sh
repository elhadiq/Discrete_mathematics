#!/bin/bash
ffmpeg -i $1/$2 -vf fps=1/10 $1/slide_%04d.png
