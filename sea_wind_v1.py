import pandas as pd
import matplotlib.pyplot as plt

# csv 파일 읽기
df = pd.read_csv(r'e:\py\b.csv')

# 상관관계 파악
corr = df.corr()

# 산점도 그래프
plt.scatter(df['temp'], df['height'])
plt.xlabel('Sea Temperature')
plt.ylabel('Average Wave Height')
plt.title('Correlation between Sea Temperature and Average Wave Height')
plt.show()

# 일반적으로 pandas 에서 파일 관리를 하기 때문에 close 명령을 사용할 필요는 없지만
# 파일을 여러번 열어야 하는 경우나 큰 파일을 사용하는 경우 메모리 부족 현상이 발생할 수 있는 경우에는
# close 를 해주도록 하자

df.close()
