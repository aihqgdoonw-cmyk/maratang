import streamlit as st


def main():
    st.set_page_config(
        page_title="마라탕 축하 페이지",
        page_icon="🥳",
        layout="centered",
    )

    st.markdown("# 🥳 마라탕 축하 페이지")
    st.markdown("---")

    st.write(
        "마라탕 성공을 축하합니다! 이 페이지는 마라탕을 즐기는 특별한 순간을 기념하기 위해 만들어졌습니다."
    )
    st.balloons()

    st.image(
        "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=1200&q=80",
        caption="따끈한 마라탕과 함께하는 축하 시간",
        use_column_width=True,
    )

    with st.expander("✨ 축하 메시지 보기"):
        st.write("오늘의 마라탕은 특히 특별해요.")
        st.write("- 매운 기운이 행복으로 바뀌는 시간입니다.")
        st.write("- 함께 나누면 더 맛있는 마라탕입니다.")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.success("✅ 마라탕 주문 완료!")
        st.write("맛있는 재료와 진한 국물이 준비되어 있어요.")
    with col2:
        st.info("🔥 매운맛 추천")
        st.write("기분에 맞는 맵기 레벨로 즐겨보세요.")

    st.markdown("---")
    st.write("즐거운 마라탕 타임 되세요! 언제든 새로고침해 축하 페이지를 다시 확인할 수 있습니다.")


if __name__ == "__main__":
    main()
