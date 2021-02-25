START_ID=1100
DATASET_ID=804
for j in $(seq 0 9);
do
for i in $(seq 1 9);
do
    python train.py $(($START_ID+10*$j+$i)) $i $DATASET_ID
    python test.py $((START_ID+100+10*$j+$i)) $(($START_ID+10*$j+$i))
done
done
