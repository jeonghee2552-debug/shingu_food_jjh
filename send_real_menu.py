import urllib.request
import json
import os

# -----------------------------------------------------------------------------
# 설정 / Configuration
# -----------------------------------------------------------------------------
TELEGRAM_BOT_TOKEN = '8659133620:AAEwe-dvhEyAFCxBoA6WaGzzYjlMBQRV3Sk'
TELEGRAM_CHAT_ID = '8582454653'

def send_to_telegram(text):
    """텔레그렘으로 메시지를 전송합니다."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }
    data_json = json.dumps(data).encode('utf-8')
    req = urllib.request.Request(url, data=data_json, headers={'Content-Type': 'application/json'})
    
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode())
            return result.get("ok", False)
    except Exception as e:
        print(f"전송 중 오류 발생: {e}")
        return False

# 실시간 추출된 식단 데이터
menu_text = """🏫 <b>신구대학교 오늘의 식단 (실시간)</b>
📅 2026년 4월 8일 (수요일)

🍱 <b>학생식당 (서관)</b>
• <b>한식:</b> 돼지짜글이덮밥, 유부장국, 해쉬브라운*케찹, 메란볼어묵장조림, 동부묵김가루무침, 깍두기
• <b>양식:</b> 수제))양념치킨, 유부장국, 후리가케볶음밥, 김치비빔국수, 샐러드*드레싱, 단무지
• <b>분식:</b> 짜장면, 튀김, 단무지

🏢 <b>미래창의관 식당</b>
• <b>중식:</b> 떡갈비스테이크, 사골칼국수, 쌀밥, 명엽채볶음, 치커리오이무침, 배추김치
• <b>분식:</b> 콩나물라면, 쌀밥, 생선까스*타르타르, 단무지/배추김치

☕ <b>교직원식당</b>
• <b>중식:</b> 마일드볼카츠*머스타드, 김치콩나물국, 베이컨알리오올리오, 어묵피망볶음, 시금치겉절이, 깍두기

맛있게 드세요! 😋"""

if __name__ == "__main__":
    print("🚀 실시간 식단 정보를 텔레그램으로 전송합니다...")
    if send_to_telegram(menu_text):
        print("✅ 성공: 실시간 식단이 전송되었습니다!")
    else:
        print("❌ 실패: 메시지 전송에 실패했습니다.")
