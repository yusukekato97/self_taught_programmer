# Challenge 2

answer = input("あなたの好きな映画は何ですか？：")

answer_file = open("fav_movie.txt", "w", encoding="utf-8")
answer_file.write(answer)
answer_file.close()
