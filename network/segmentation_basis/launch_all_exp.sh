for i in $(seq 1 9);
do
    python train.py $((30+$i)) $i
    python test.py $((40+$i)) $((30+$i))
done

