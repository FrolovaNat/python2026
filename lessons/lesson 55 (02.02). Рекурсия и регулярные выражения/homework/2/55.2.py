import re
text = "Сегодня 25.04.2024, а завтра будет 26.04.2024."
pattern = r'\b\d{2}.\d{2}.\d{4}\b'
matches = re.findall(pattern, text)
print(matches)
