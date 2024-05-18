#!/bin/bash

model='TIGER-Lab/MAmmoTH2-8B-Plus'

dataset='theoremqa'

python run_open.py \
  --model $model \
  --shots 5 \
  --dataset $dataset \
  --form short

dataset='math'

python run_open.py \
  --model $model \
  --shots 4 \
  --dataset $dataset \
  --form short

dataset='gsm8k'

python run_open.py \
  --model $model \
  --shots 4 \
  --dataset $dataset \
  --form short:step

dataset='gpqa_diamond'

python run_choice.py \
  --model $model \
  --shots 5 \
  --dataset $dataset \
  --form short

dataset='mmlu_stem'

python run_choice.py \
  --model $model \
  --shots 5 \
  --dataset $dataset \
  --form short

dataset='bbh'

python run_open.py \
  --model $model \
  --shots 3 \
  --dataset $dataset \
  --form short:step

dataset='arc'

python run_choice.py \
  --model $model \
  --shots 8 \
  --dataset $dataset \
  --form short
