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
