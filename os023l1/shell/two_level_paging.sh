echo "Please input a logical address: "
read la
d=$((la & 2#1111111111))
p2=$((la >> 10))
p2=$((p2 & 2#1111111111))
p1=$((la >> 20))
echo "p1: $p1"
echo "p2: $p2"
echo "d: $d"

