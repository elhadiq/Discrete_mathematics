#!/bin/bash
# Build all chapter PDFs and the full book. Run from Book/.
set -e
mkdir -p build build/chapters pdf
for f in standalone/ch*.tex; do
  n=$(basename "$f" .tex)
  pdflatex -interaction=nonstopmode -output-directory=build "$f" >/dev/null
  pdflatex -interaction=nonstopmode -output-directory=build "$f" >/dev/null
  cp "build/$n.pdf" "pdf/Discrete_Mathematics_$n.pdf"
done
pdflatex -interaction=nonstopmode -output-directory=build main.tex >/dev/null
pdflatex -interaction=nonstopmode -output-directory=build main.tex >/dev/null
cp build/main.pdf pdf/Discrete_Mathematics_Book.pdf
echo "All PDFs in Book/pdf/"
