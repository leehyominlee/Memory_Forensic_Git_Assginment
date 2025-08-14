def main():
    
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 파일에서 데이터 읽기 (쉼표 구분 처리)
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
    data = [int(x.strip()) for x in content.split(",")]

print("정렬 전:", data)
sorted_data = merge_sort(data)
print("정렬 후:", sorted_data)

if __name__ == "__main__":
    main()
