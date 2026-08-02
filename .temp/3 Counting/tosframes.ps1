param($Directory, $Filename)

ffmpeg -i "$Directory\$Filename" -vf fps=1/10 "$Directory\slide_%04d.png"