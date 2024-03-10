def read_sub(f_in, f_out):
  with open(f_in, 'r', encoding='UTF8') as f_in, open(f_out, 'w', encoding='UTF8') as f_out:
    line_buffer = []
    prev_line_buffer = []
    for line in f_in:
      line_buffer.append(line)
      if len(line_buffer) == 4:
        if line_buffer == prev_line_buffer:
          # 이전 4줄과 같으면 출력하지 않음
          pass
        else:
          f_out.writelines(line_buffer)
        prev_line_buffer = line_buffer
        line_buffer = []

def conver_html(txt, html):
  color = ["green", "red", "black", "blue"]
  
  with open(txt, "r", encoding='UTF8') as f_in, open(html, "w", encoding='UTF8') as f_out:
    f_out.write("""
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>텍스트 파일 변환 결과</title>
</head>
<body>
""")
    
    line_buffer = []
    for line in f_in:
      line_buffer.append(line)
      
      if len(line_buffer) == 4:
        for i, line in enumerate(line_buffer):
          f_out.write(f"<p style=\"color: {color[i]};\">{line}</p>")
          if i%4 == 3:
            f_out.write("<p></p><p></p>")
        line_buffer = []
    
    # 마지막 4줄 미만 처리
    if line_buffer:
      for i, line in enumerate(line_buffer):
        f_out.write(f"<p style=\"color: {color[i]};\">{line}</p>")    
    f_out.write("""
</body>
</html>
""")

if __name__ == "__main__":
  f_in = "google_sub.txt"
  f_out = "result.txt"
  read_sub(f_in, f_out)

  conver_html(f_out, "result.html")