import random

# train-all-04.txt 파일 읽기
with open('train-all-04.txt', 'r') as f:
    lines = f.readlines()

# 데이터 섞기
random.shuffle(lines)

# 데이터 분할 (80% 훈련, 20% 검증)
split_index = int(0.8 * len(lines))
train_lines = lines[:split_index]
val_lines = lines[split_index:]

# train.txt와 val.txt 파일로 저장
with open('train.txt', 'w') as f:
    f.writelines(train_lines)

with open('val.txt', 'w') as f:
    f.writelines(val_lines)
