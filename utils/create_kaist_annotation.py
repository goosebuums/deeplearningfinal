import json

# 파일 경로 설정
val_file_path = '/home/a/hyu/aue8088-pa2/utils/val.txt'
input_json_file_path = '/home/a/hyu/aue8088-pa2/datasets/kaist-rgbt/annotations/instances_val2017.json'
output_json_file_path = '/home/a/hyu/aue8088-pa2/utils/KAIST_annotation.json'
example_json_file_path = '/home/a/다운로드/(example) KAIST_annotation.json'

# 예제 JSON 파일을 참고하여 기본 구조 생성
with open(example_json_file_path, 'r') as file:
    kaist_data = json.load(file)

# 입력 JSON 파일 읽기
with open(input_json_file_path, 'r') as file:
    instances_data = json.load(file)

# images 및 annotations 리스트 초기화
kaist_data["images"] = []
kaist_data["annotations"] = []

# images 섹션 추가
image_id_map = {}
for idx, image_info in enumerate(instances_data["images"]):
    new_image_info = {
        "id": idx,
        "file_name": image_info.get("file_name", image_info.get("im_name")),  # 수정된 부분
        "height": image_info["height"],
        "width": image_info["width"]
    }
    kaist_data["images"].append(new_image_info)
    image_id_map[new_image_info["file_name"]] = idx  # 수정된 부분

# annotations 섹션 추가
annotation_id = 0
for annotation in instances_data.get("annotations", []):
    new_annotation = {
        "id": annotation_id,
        "image_id": image_id_map[annotation["image_id"]],
        "category_id": annotation["category_id"],
        "bbox": annotation["bbox"],
        "area": annotation["bbox"][2] * annotation["bbox"][3],
        "iscrowd": annotation.get("iscrowd", 0)
    }
    kaist_data["annotations"].append(new_annotation)
    annotation_id += 1

# categories 섹션 추가
kaist_data["categories"] = [
    {"id": 0, "name": "person"},
    {"id": 1, "name": "cyclist"},
    {"id": 2, "name": "people"},
    {"id": 3, "name": "person?"}
]

# JSON 파일 저장
with open(output_json_file_path, 'w') as file:
    json.dump(kaist_data, file, indent=4)

print(f"Updated JSON 파일이 {output_json_file_path}에 저장되었습니다.")

