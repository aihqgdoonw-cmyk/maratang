(import streamlit as st)


def main():
	st.set_page_config(page_title="마라탕 단식", page_icon="🥳", layout="centered")

	st.title("🎉 축하합니다 — 마라탕 단식 16일차!")

	st.markdown("---")

	st.header("16일째를 달성하셨습니다")
	st.write(
		"정말 대단해요 — 꾸준함과 의지가 만든 성과입니다. 오늘은 자신을 위해 작은 보상을 준비해보세요!"
	)

	st.balloons()

	st.success("16일째 달성 완료 ✅")

	st.info("건강을 최우선으로 하시고, 무리가 되면 중단하세요.")

	st.markdown("---")
	st.write("원하시면 축하 메시지를 친구에게 공유할 텍스트를 생성해 드릴게요.")

	if st.button("친구에게 보낼 축하 문구 생성"):
		st.write("🎊 축하해요! 마라탕 단식 16일째를 축하합니다 — 정말 대단해요! 함께 축하하러 가요 :) ")


if __name__ == "__main__":
	main()

