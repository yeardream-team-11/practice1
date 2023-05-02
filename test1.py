
def check_result(selected_door, prize_door):
    # 게임 결과 체크.
    return selected_door == prize_door

def choose_door():
    return random.randint(1, 3)

# 팀원2
def reveal_door(selected_door, prize_door):
    # 호스트가 선택한 문을 엶.
    doors = [1, 2, 3]
    doors.remove(selected_door)
    if prize_door in doors:
        doors.remove(prize_door)
    return random.choice(doors)

