# 팀원2
def reveal_door(selected_door, prize_door):
    # 호스트가 선택한 문을 엶.
    doors = [1, 2, 3]
    doors.remove(selected_door)
    if prize_door in doors:
        doors.remove(prize_door)
    return random.choice(doors)
