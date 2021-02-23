for i in $(seq 1 9);
do
    echo $((50+$i))
    python train.py $((50+$i)) $i
    python test.py $((60+$i)) $((50+$i))
done

