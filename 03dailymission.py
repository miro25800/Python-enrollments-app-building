########################################################
# 261119 금일 과제
# TODO: 입력 로직 구현

# MEMBER_ID = 10
# COURSE_ID = 1

# 수강 신청
# def enroll(conn, member_id, course_id):
    # TODO: 신청한 강좌의 수강료 추출
#   fee = 0

#     conn.execute(
#         "INSERT INTO enrollments (member_id, course_id, enroll_month, status, pay_amount) "
#         "VALUES (%s, %s, %s, '수강중', %s)",
#         (member_id, course_id, MONTH, 0)
#     )
#     print("수강신청 완료되었습니다.")

######################################################

# 03 데이터베이스 일일 과제 / 03dailymission

# 정의 시작점 인자시작/끝 블록시작
# def main():

#   목록_전체강좌목록(연결) 블록시작
#   list_courses(conn):
        
#       행 지정 연결.실행("선택 회원_이름, 회원_아이디, 강좌명, 수강료 그리고 전체강좌목록 제한된검색 강좌 5개").특정값 꺼내기()
#       row = conn.execute("SELECT member_name, member_id, course_name, course_id, pay_amount FROM courses LIMIT 5").fetchone()

#       "결과값 (빈칸채우기, 빈칸채우기, 빈칸채우기, 빈칸채우기, 빈칸채우기)",
#       "VALUES (%s, %s, %s, %s, %s)",

#       행 지정 연결.실행("선택 검색 강좌명, 강좌_아이디 그리고 전체강좌목록 제한된검색 강좌 5개").특정값 꺼내기()
#       row = conn.execute("SELECT SEARCH course_name, course_id FROM courses LIMIT 5").fetchone()

def main():
    list_courses(conn):
        row = conn.execute("SELECT member_name, member_id, course_name, course_id, pay_amount FROM courses LIMIT 5").fetchone()
        "VALUES (%s, %s, %s, %s, %s)",
        row = conn.execute("SELECT SEARCH course_name, course_id FROM courses LIMIT 5").fetchone()

######################################################
