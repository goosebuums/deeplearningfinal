import os
from sklearn.model_selection import KFold

def split_kaist_data(input_file_path, output_dir, n_splits=5):
    # 데이터 읽기
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    # KFold 객체 생성
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)

    fold_num = 1
    for train_index, val_index in kf.split(lines):
        train_lines = [lines[i] for i in train_index]
        val_lines = [lines[i] for i in val_index]

        # 각 폴드에 대한 디렉토리 생성
        fold_dir = os.path.join(output_dir, f'fold_{fold_num}')
        os.makedirs(fold_dir, exist_ok=True)

        # train 파일 생성
        train_file_path = os.path.join(fold_dir, 'train.txt')
        with open(train_file_path, 'w') as train_file:
            train_file.writelines(train_lines)

        # val 파일 생성
        val_file_path = os.path.join(fold_dir, 'val.txt')
        with open(val_file_path, 'w') as val_file:
            val_file.writelines(val_lines)

        print(f'폴드 {fold_num}에 대한 train 및 val 파일이 생성되었습니다.')
        fold_num += 1

# 파일 경로 설정
input_file_path = '/home/a/hyu/kaist-rgbt/train-all-04.txt'  # 사용자의 train.txt 파일 경로
output_dir = '/home/a/hyu/kaist-rgbt/5fold'  # 출력 디렉토리 경로

# 데이터셋 나누기
split_kaist_data(input_file_path, output_dir)
