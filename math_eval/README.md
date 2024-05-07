# Reproducing our results in the paper

## Enter the eval folder
```
cd math_eval
```

## To reproduce 7B-plus results
```
bash run_7B_plus.sh
```

## To reproduce 8B-plus results
```
bash run_8B_plus.sh
```

## To reproduce 8x7B-plus results
```
bash run_7B_moe_plus.sh
```

The results will fluctuate depending on the library version and devices. We run on A100 cards and use the library provided in requirements.txt.
