for i in $(seq 1 9);
do
    python train.py $((10+$i)) $i
    python test.py $((20+$i)) $((10+$i))
done

