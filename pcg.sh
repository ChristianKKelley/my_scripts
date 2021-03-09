#/bin/bash

read AUTHYR
read PAPER
VARIABLE=$(echo "_$PAPER" | tr '\ ' '\_' | sed 's/://' | sed 's/,//' | sed 's/,//' | sed 's/,//' | tr '\/' '\_' | tr '\.' 'p') 
echo $VARIABLE
FIN="$AUTHYR$VARIABLE"
FIN2="${FIN}.pdf"
echo $FIN2 | xclip -selection clipboard

