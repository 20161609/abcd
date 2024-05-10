import openpyxl

def read_value(wb, a, b):
    try:
        # 첫 번째 시트 선택
        sheet = wb.active

        # 셀 좌표로부터 값 읽기
        cell_value = sheet.cell(row=a, column=b).value
        return cell_value
    except Exception as e:
        print(f"오류 발생: {e}")
        return None

