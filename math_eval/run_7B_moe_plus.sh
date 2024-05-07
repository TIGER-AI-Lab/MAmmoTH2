#!/bin/bash

model='TIGER-Lab/MAmmoTH2-8x7B-Plus'

dataset='theoremqa'

python run_open.py \
  --model $model \
  --shots 5 \
  --dataset $dataset \
  --form short:step

dataset='math'

python run_open.py \
  --model $model \
  --shots 4 \
  --dataset $dataset \
  --form short:step

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
  --use_vllm \
  --form short

dataset='mmlu_stem'

python run_choice.py \
  --model $model \
  --shots 5 \
  --dataset $dataset \
  --use_vllm \
  --form short:step

dataset='bbh'

python run_open.py \
  --model $model \
  --shots 3 \
  --dataset $dataset \
  --use_vllm \
  --form short:step

dataset='arc'

python run_choice.py \
  --model $model \
  --shots 8 \
  --dataset $dataset \
  --use_vllm \
  --form short
