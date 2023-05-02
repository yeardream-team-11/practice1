# 팀원3
def switch_door(selected_door, revealed_door):
    # 선택한 문 바꾸기.
    doors = [1, 2, 3]
    doors.remove(selected_door)
    doors.remove(revealed_door)
    return doors[0]
