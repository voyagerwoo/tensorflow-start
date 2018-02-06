import tensorflow as tf

a = tf.placeholder('float')
b = tf.placeholder('float')

y = tf.multiply(a, b)

sess = tf.Session()

print(sess.run(y, feed_dict={a: 3, b: 3}))

"""
- tensor란 동적 크기를 갖는 다차원 데이터 배열
- 심벌릭 표현으로 된 수식을 계산하기 위해서 session 생성, session.run() 하고 나서야 실행
- 즉, 전체 알고리즘을 먼저 기술하고 그 다음 세션을 생성하여 연산을 실행
"""
