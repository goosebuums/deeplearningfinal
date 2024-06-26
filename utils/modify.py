# 파일 경로 설정
file_path = '/home/a/hyu/kaist-rgbt/kaist-rgbt/train-all-04.txt'  # 실제 파일 경로로 수정 필요
output_file_path = '/home/a/hyu/kaist-rgbt/kaist-rgbt/modified_image_paths.txt'

# 파일 읽기
with open(file_path, 'r') as file:
    lines = file.readlines()

# 파일 경로 수정
modified_lines = [line.replace('{}', 'visible') for line in lines]

# 수정된 파일 저장
with open(output_file_path, 'w') as file:
    file.writelines(modified_lines)

print(f"수정된 파일이 {output_file_path}에 저장되었습니다.")
